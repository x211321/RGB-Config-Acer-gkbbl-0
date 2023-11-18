#!/usr/bin/env python3

#################################################################################################
## RGB Config (acer-gkbbl-0) - https://github.com/x211321/RGB-Config-Acer-gkbbl-0     
##
## A graphical user interface to interact with the RGB controls of the acer-gkbbl-0 character device 
## provided by JafarAkhondali's kernel module.
## 
## The kernel module must be installed seperatly for this application to work 
##
## Visit https://github.com/JafarAkhondali/acer-predator-turbo-and-rgb-keyboard-linux-module
## for additional information regarding the kernel module
#################################################################################################
## MIT License
## Copyright 2022 x211321 (https://github.com/x211321)
## View the acompaning LICENSE file for additional licensing information
#################################################################################################

import os
import sys
import json
import pathlib
import webbrowser
import subprocess

import lib.ui as ui
import lib.var as var
from lib.prefs import app_preferences
from lib.version import VERSION

APP_NAME = "rgb_config_acer_gkbbl_0"

APP_DIR  = os.path.abspath(os.path.dirname(__file__))
LANG_DIR = os.path.join(APP_DIR, "assets", "locale")

# Set app language
if len(app_preferences["language"]):
    os.environ["LANGUAGE"]=app_preferences["language"]

# Settup gettext
import gettext
gettext.bindtextdomain(APP_NAME, LANG_DIR)
gettext.textdomain(APP_NAME)
_ = gettext.gettext

# Get the active language from gettext language file path
if gettext.find(APP_NAME, LANG_DIR): 
    ACTIVE_LANG = gettext.find(APP_NAME, LANG_DIR).replace(LANG_DIR, "")[1:3]
else:
    ACTIVE_LANG = "en"


# Error message if wxPython is not available
WXPYTHON_NOT_AVAILABLE = _("wxPython not available\n\n" \
                           "Please install wxPython via your distributions package manager or python3 pip.\n\n" \
                           "e.g.\napt install python3-wxgtk4.0\n\n" \
                           "Visit\nhttps://wxpython.org/\nfor more information")


# Try importing wxPython
# give error message if not available
try:
    import wx
except ImportError:
    # Print error to console
    print(_("Error"), WXPYTHON_NOT_AVAILABLE)

    try:
        # Try importing tkinter to show error messagebox
        from tkinter import Tk
        from tkinter import messagebox
        tk = Tk()
        tk.withdraw()
        messagebox.showerror(_("Error"), WXPYTHON_NOT_AVAILABLE)
        tk.destroy()
    except ImportError:
        # If tkinter is also not available: hope the user
        # has seen the above console message
        pass

    exit()

# Must be importet after wx
from lib.tray import AcerRGBGUI_Tray


####################
# class AcerRGBGUI_About
#-------------------
# Extend wx wxPython About dialog
class AcerRGBGUI_About(ui.dialog_about):
    def __init__(self, parent):
        ui.dialog_about.__init__(self, parent)

    def on_button_about_close_click(self, event):
        self.Destroy()


####################
# class AcerRGBGUI_Frame
#-------------------
# Extend wx wxPython Frame
class AcerRGBGUI_Frame(ui.frame_main):

    #########################################
    ## MAIN WINDOW INIT
    #########################################

    ####################
    # __init__
    #-------------------
    def __init__(self, parent, title):
        ui.frame_main.__init__(self, parent)

        self.aboutDlg = None

        # Set app icon
        self.SetIcon(wx.Icon('./assets/icon.png', wx.BITMAP_TYPE_PNG))

        # Set app title
        self.SetTitle(_("RGB Config (acer-gkbbl-0) ") + VERSION)

        # Defince color widgets
        self.colorWidgets = [
            {"widget": self.color_color0, "label": self.label_colors},
            {"widget": self.color_color1},
            {"widget": self.color_color2},
            {"widget": self.color_color3}
        ]

        # Define the different widget states in regard to the selected RGB mode
        self.widgetStates = [
            {"mode": var.RGB_MODE_STATIC  , "speed": 0, "direction": 0, "colors": (1,1,1,1), "animation": "preview_static"},
            {"mode": var.RGB_MODE_BREATH  , "speed": 1, "direction": 0, "colors": (1,0,0,0), "animation": "preview_breath"},
            {"mode": var.RGB_MODE_NEON    , "speed": 1, "direction": 0, "colors": (0,0,0,0), "animation": "preview_neon"},
            {"mode": var.RGB_MODE_WAVE    , "speed": 1, "direction": 1, "colors": (0,0,0,0), "animation": "preview_wave"},
            {"mode": var.RGB_MODE_SHIFTING, "speed": 1, "direction": 1, "colors": (1,0,0,0), "animation": "preview_shifting"},
            {"mode": var.RGB_MODE_ZOOM    , "speed": 1, "direction": 0, "colors": (1,0,0,0), "animation": "preview_zoom"}
        ]

        # Create config directories
        if not os.path.exists(var.PROFILE_DIR):
            os.makedirs(var.PROFILE_DIR)

        # Load app preferences
        self.preferences = {}
        self.loadPreferences()

        # Generate language menu
        self.generateLanguageMenu()

        # Generate tray icon style menu
        self.generateTrayIconStyleMenu()

        # List profiles
        self.profiles = []
        self.listProfiles()

        # Load last applied settigs
        self.loadProfile(var.ACTIVE_PROFILE)

        # Create tray icon
        if self.preferences["tray"]:
            self.createTrayIcon()

        # Apply log preference
        # - hide log widget when not active
        if not self.preferences["log"]:
            self.panel_bottom.Hide()
            self.splitter_main_horizonzal.Unsplit()

        # Apply profiles preference
        # - hide profiles widged when not active
        if not self.preferences["profiles"]:
            self.panel_right.Hide()
            self.splitter_main_vertical.Unsplit()

        # Apply [ACTIVE] profile on startup when enabled
        if self.preferences["applyStart"]:
            self.apply()

        # Extend speed limit when enabled
        if self.preferences["extendSpeed"]:
            self.slider_speed.SetRange(0, 255)

        # Set button icons
        self.button_save.SetBitmap(wx.ArtProvider.GetBitmap("document-save", wx.ART_MENU))
        self.button_delete.SetBitmap(wx.ArtProvider.GetBitmap("edit-delete", wx.ART_MENU))
        self.button_load.SetBitmap(wx.ArtProvider.GetBitmap("document-open", wx.ART_MENU))

        # Check RGB Devices available
        # - show error message in log when device not found
        if os.path.exists(var.RGB_DEVICE):
            self.appLog(_("RGB device %s detected") % var.RGB_DEVICE)
        else:
            self.errLog(_("ERROR: RGB device %s not found") % var.RGB_DEVICE)
            self.appLog(_("Install instructions:"))
            self.urlLog("https://github.com/JafarAkhondali/acer-predator-turbo-and-rgb-keyboard-linux-module")

        if os.path.exists(var.RGB_DEVICE_STATIC):
            self.appLog(_("Static RGB device %s detected") % var.RGB_DEVICE_STATIC)
        else:
            self.errLog(_("ERROR: Static RGB device %s not found") % var.RGB_DEVICE_STATIC)
            self.appLog(_("Install instructions:"))
            self.urlLog("https://github.com/JafarAkhondali/acer-predator-turbo-and-rgb-keyboard-linux-module")


    #########################################
    ## Event handler
    #########################################


    ####################
    # on_close
    #-------------------
    # Event handler - close
    def on_close(self, event):
        if self.preferences["closeToTray"]:
            # Hide to tray instead of close when configured that way
            self.Hide()
        else:
            self.on_force_close(event)


    ####################
    # on_force_close
    #-------------------
    # Event handler - force close
    # ignores "close to tray" preference
    def on_force_close(self, event):
        if hasattr(self, 'trayIcon'):
            self.trayIcon.Destroy()

        # Remember window position and size
        self.preferences["windowWidth"]  = self.GetSize().GetWidth()
        self.preferences["windowHeight"] = self.GetSize().GetHeight()
        self.preferences["windowPosX"]   = self.GetPosition().x
        self.preferences["windowPosY"]   = self.GetPosition().y

        # Remember sash positions
        self.preferences["sashPosVertical"]   = self.splitter_main_vertical.GetSashPosition()
        self.preferences["sashPosHorizontal"] = self.splitter_main_horizonzal.GetSashPosition()

        self.savePreferences()

        self.Destroy()


    ####################
    # on_rgb_mode_select
    #-------------------
    # Event handler - RGB mode select
    def on_rgb_mode_select(self, event):
        self.setWidgetState()


    ####################
    # on_direction_select
    #-------------------
    # Event handler - direction select
    def on_direction_select(self, event):
        self.setWidgetState()


    ####################
    # on_menu_click
    #-------------------
    # Event handler - open button menu
    def on_menu_click(self, event):
        self.PopupMenu(self.button_Menu)


    ####################
    # on_apply_click
    #-------------------
    # Event handler - apply RGB settings click
    def on_apply_click(self, event):
        self.apply()


    ####################
    # on_delete_click
    #-------------------
    # Event handler - profile delete button click
    def on_delete_click(self, event):
        profile = self.list_profiles.GetStringSelection()
        self.deleteProfile(profile)


    ####################
    # on_load_click
    #-------------------
    # Event handler - profile load button click
    def on_load_click(self, event):
        profile = self.list_profiles.GetStringSelection()
        self.loadProfile(profile)


    ####################
    # on_save_click
    #-------------------
    # Event handler - profile save button click
    def on_save_click(self, event):
        self.saveProfile()


    ####################
    # on_log_url_click
    #-------------------
    # Event handler - url click in log widget
    def on_log_url_click(self, event):
        webbrowser.open(self.rich_log.GetValue()[event.GetURLStart():event.GetURLEnd()+1], new=0, autoraise=True)


    ####################
    # on_idle_set_sash_pos
    #-------------------
    # Workaround to set sash position after sizing
    def on_idle_set_horizontal_sash_pos(self, event):
        if "sashPosHorizontal" in self.preferences:
            self.splitter_main_horizonzal.SetSashPosition(self.preferences["sashPosHorizontal"])
            self.splitter_main_horizonzal.Unbind(wx.EVT_IDLE)


    ####################
    # on_idle_set_vertical_sash_pos
    #-------------------
    # Workaround to set sash position after sizing
    def on_idle_set_vertical_sash_pos(self, event):
        if "sashPosVertical" in self.preferences:
            self.splitter_main_vertical.SetSashPosition(self.preferences["sashPosVertical"])
            self.splitter_main_vertical.Unbind(wx.EVT_IDLE) 


    ####################
    # on_menu_openProfileFolder
    #-------------------
    # Event handler - open profile folder
    def on_menu_openProfileFolder(self, event):
        subprocess.Popen(["xdg-open", var.PROFILE_DIR])


    ####################
    # on_menu_refreshProfileList
    #-------------------
    # Event handler - refresh profile list
    def on_menu_refreshProfileList(self, event):
        self.listProfiles()


    ####################
    # on_menu_tray
    #-------------------
    # Event handler - show tray
    def on_menu_tray(self, event):
        if self.menuItem_tray.IsChecked():
            self.createTrayIcon()
        else:
            self.trayIcon.RemoveIcon()

        self.preferences["tray"] = self.menuItem_tray.IsChecked()
        self.savePreferences()


    ####################
    # on_menu_startMinimized
    #-------------------
    # Event handler - start minimized
    def on_menu_startMinimized(self, event):
        self.preferences["startMinimized"] = self.menuItem_startMinimized.IsChecked()
        self.savePreferences()


    ####################
    # on_menu_closeToTray
    #-------------------
    # Event handler - close to tray
    def on_menu_closeToTray(self, event):
        self.preferences["closeToTray"] = self.menuItem_closeToTray.IsChecked()
        self.savePreferences()


    ####################
    # on_menu_applyStart
    #-------------------
    # Event handler - menu apply on startup
    def on_menu_applyStart(self, event):
        self.preferences["applyStart"] = self.menuItem_applyStart.IsChecked()
        self.savePreferences()


    ####################
    # on_menu_extendSpeed
    #-------------------
    # Event handler - menu extend speed
    def on_menu_extendSpeed(self, event):
        # Confirm speed extension with user
        if self.menuItem_extendSpeed.IsChecked():
            dlg = wx.MessageDialog(self, _("Offical Acer software only allows speed values between 0 and 9.\n\n" \
                                           "In theory the acer-gkbbl-0 character device accepts speed values between 0 and 255. " \
                                           "Values above the standard limit of 9 might yield undesired results.\n\n" \
                                           "It is advised to proceed with caution.\n\n" \
                                           "Are you sure you want to extend the speed limit?")
                                           , _("Extend max speed"), wx.YES_NO)
            res = dlg.ShowModal()

            if not res == wx.ID_YES:
                self.menuItem_extendSpeed.Check(False)

        self.preferences["extendSpeed"] = self.menuItem_extendSpeed.IsChecked()
        self.savePreferences()

        if self.preferences["extendSpeed"]:
            self.slider_speed.SetRange(0, 255)
        else:
            self.slider_speed.SetRange(0, 9)

    ####################
    # on_menu_log
    #-------------------
    # Event handler - menu show log
    def on_menu_log(self, event):
        if self.menuItem_log.IsChecked():
            self.panel_bottom.Show()
            self.splitter_main_horizonzal.SplitHorizontally(self.panel_top, self.panel_bottom)
            self.splitter_main_horizonzal.SetSashPosition(400)
        else:
            self.panel_bottom.Hide()
            self.splitter_main_horizonzal.Unsplit()

        self.preferences["log"] = self.menuItem_log.IsChecked()
        self.savePreferences()


    ####################
    # on_menu_profiles
    #-------------------
    # Event handler - menu show profiles
    def on_menu_profiles(self, event):
        if self.menuItem_profiles.IsChecked():
            self.panel_right.Show()
            self.splitter_main_vertical.SplitVertically(self.panel_left, self.panel_right)
            self.splitter_main_vertical.SetSashPosition(600)
            self.button_menu_left.Hide()
            self.button_menu_right.Show()
        else:
            self.panel_right.Hide()
            self.splitter_main_vertical.Unsplit()
            self.button_menu_left.Show()
            self.button_menu_right.Hide()

        self.button_menu_left.GetParent().Layout()
        self.button_menu_right.GetParent().Layout()

        self.preferences["profiles"] = self.menuItem_profiles.IsChecked()
        self.savePreferences()


    ####################
    # on_menu_preview
    #-------------------
    # Event handler - menu show preview
    def on_menu_preview(self, event):
        self.preferences["preview"] = self.menuItem_preview.IsChecked()
        self.savePreferences()
        self.setPreviewAnimation()


    ####################
    # on_menu_about
    #-------------------
    # Event handler - menu about
    def on_menu_about(self, event):
        self.aboutDlg = AcerRGBGUI_About(self)
        self.aboutDlg.SetTitle(_("About RGB Config (acer-gkbbl-0) ") + VERSION)
        self.aboutDlg.ShowModal()
        self.aboutDlg = None


    ####################
    # on_menu_change_language
    #-------------------
    # Event handler - menu change language
    def on_menu_change_language(self, event):

        # Get menu item of event
        menuItem = event.GetEventObject().MenuItems[event.Id]

        # Get langujage from item label
        language = menuItem.GetItemLabel()

        # Save new preferences
        self.preferences["language"] = language
        self.savePreferences()

        # Language change requies app restart - ask user
        dlg = wx.MessageDialog(self, _("The application must be restartet to apply the language change.\n\n" \
                                       "Do you want to restart now?"), _("Change language"), wx.YES_NO)
        res = dlg.ShowModal()

        if res == wx.ID_YES:
            os.execv(sys.executable, ['python3'] + sys.argv)


    ####################
    # on_menu_change_trayIconStyle
    #-------------------
    # Event handler - menu change tray icon style
    def on_menu_change_trayIconStyle(self, event):

        # Get menu item of event
        menuItem = event.GetEventObject().MenuItems[event.Id-var.TRAY_ICON_STYLE_MENU_OFFSET]

        # Get style from item label
        trayIconStyle = menuItem.GetItemLabel().replace(" ", "_")

        # Save new preferences
        self.preferences["trayIconStyle"] = trayIconStyle
        self.savePreferences()

        # Apply new icon style
        if self.preferences["tray"]:
            self.trayIcon.UpdateIcon()

        


    #########################################
    ## DIALOG INTERACTION
    #########################################

    ####################
    # createTrayIcon
    #-------------------
    # Create the tray icon
    def createTrayIcon(self):
        self.trayIcon = AcerRGBGUI_Tray(self)


    ####################
    # setPreviewAnimation
    #-------------------
    # Plays preview animation according to the selected RGB mode
    def setPreviewAnimation(self):
        # Default none-preview
        file = "./assets/preview_gif/preview_none.gif"

        # Set specific preview when previews enabled
        if self.preferences["preview"]:
            file = os.path.join("./assets/preview_gif/", self.widgetStates[self.choise_mode.GetSelection()]["animation"]) + ".gif"

        # Load animation and play
        self.animation_preview.LoadFile(file, wx.adv.ANIMATION_TYPE_GIF)
        self.animation_preview.Play()


    ####################
    # setWidgetState
    #-------------------
    # Aranges the RGB settings widgets according to the selected RGB mode
    # so that options that have no effect in the selected RGB mode are disabled
    def setWidgetState(self):
        selection = self.choise_mode.GetSelection()

        self.enableSpeed(self.widgetStates[selection]["speed"])
        self.enableDirection(self.widgetStates[selection]["direction"])
        self.enableColors(self.widgetStates[selection]["colors"])

        self.setPreviewAnimation()


    ####################
    # enableSpeed
    #-------------------
    # Enable or disable the speed widget
    # - arg enabled: bool 0/1
    def enableSpeed(self, enabled):
        if enabled:
            self.label_speed.Enable()
            self.slider_speed.Enable()
        else:
            self.label_speed.Disable()
            self.slider_speed.Disable()


    ####################
    # enableColors
    #-------------------
    # Enable or disable the color widgets
    # - arg enabled: bool tuple (c1, c2, c3, c4) (0/1)
    def enableColors(self, enabled):
        for index in range(4):
            if enabled[index]:
                self.colorWidgets[index]["widget"].Enable()
                self.colorWidgets[index]["widget"].Show()

                if "label" in self.colorWidgets[index]:
                    self.colorWidgets[index]["label"].Enable()
                    self.colorWidgets[index]["label"].Show()

            else:
                self.colorWidgets[index]["widget"].Disable()
                self.colorWidgets[index]["widget"].Hide()
                
                if "label" in self.colorWidgets[index]:
                    self.colorWidgets[index]["label"].Disable()
                    self.colorWidgets[index]["label"].Hide()

            self.colorWidgets[index]["widget"].GetParent().Layout()


    ####################
    # enableDirection
    #-------------------
    # Enable or disable the direction widget
    # - arg enabled: bool 1/0
    def enableDirection(self, enabled):
        if enabled:
            self.label_direction.Enable()
            self.radio_left_right.Enable()
            self.radio_right_left.Enable()
        else:
            self.label_direction.Disable()
            self.radio_left_right.Disable()
            self.radio_right_left.Disable()


    ####################
    # getRGBSettings
    #-------------------
    # Get RGB settings from dialog
    def getRGBSettings(self):
        self.settings["mode"]       = self.choise_mode.GetSelection()
        self.settings["speed"]      = self.slider_speed.GetValue()
        self.settings["brightness"] = self.slider_brightness.GetValue()
        self.settings["direction"]  = 1 if self.radio_left_right.GetValue() else 2

        for i, widget in enumerate(self.colorWidgets):
            self.settings["colors"][i] = self.getColor(widget["widget"])

        self.settings["red"]   = self.settings["colors"][0]["red"]
        self.settings["green"] = self.settings["colors"][0]["green"]
        self.settings["blue"]  = self.settings["colors"][0]["blue"]


    ####################
    # restoreRGBSettings
    #-------------------
    # Restore RGB settings in dialog
    def restoreRGBSettings(self):
        self.choise_mode.SetSelection(self.settings["mode"])
        self.slider_speed.SetValue(self.settings["speed"])
        self.slider_brightness.SetValue(self.settings["brightness"])

        if self.settings["direction"] == 1:
            self.radio_left_right.SetValue(True)
        else:
            self.radio_right_left.SetValue(True)

        for i, widget in enumerate(self.colorWidgets):
            self.setColor(widget["widget"], self.settings["colors"][i])

        self.setWidgetState()


    ####################
    # getColor
    #-------------------
    # Retrieve color from the given color widget
    # - arg widget: wxColorPickerCtrl to retriev the active color from
    # - return: dict with keys red, green and blue (0-255)
    def getColor(self, widget):
        color = widget.GetColour()
        return {"red": color.Red(), "green": color.Green(), "blue": color.Blue()}


    ####################
    # setColor
    #-------------------
    # Write the given color to the given color widget
    # - arg widget: wxColorPickerCtrl to apply the active color on
    # - arg color: dict with keys red, green and blue (0-255)
    def setColor(self, widget, color):
        widget.SetColour(wx.Colour(color["red"], color["green"], color["blue"]))


    ####################
    # generateLanguageMenu
    #-------------------
    # Searches for translation files for the application 
    # and lists them in the options menu
    def generateLanguageMenu(self):
        menuID = 0

        for language in os.listdir(LANG_DIR):
            if os.path.isdir(os.path.join(LANG_DIR, language)):
                item = self.subMenu_language.AppendRadioItem(menuID, language)
                self.Bind(wx.EVT_MENU, self.on_menu_change_language, id=menuID)

                menuID += 1

                # Check active language
                if language == ACTIVE_LANG:
                    item.Check()


    ####################
    # generateTrayIconStyleMenu
    #-------------------
    # Searches for tray icon styles 
    # and lists them in the options menu
    def generateTrayIconStyleMenu(self):
        menuID = var.TRAY_ICON_STYLE_MENU_OFFSET

        for trayIconStyle in os.listdir(var.TRAY_ICON_STYLE_DIR):
            if os.path.isfile(os.path.join(var.TRAY_ICON_STYLE_DIR, trayIconStyle)):

                trayIconStyle = pathlib.Path(trayIconStyle).stem.replace("_", " ")

                item = self.subMenu_trayIconStyle.AppendRadioItem(menuID, trayIconStyle)
                self.Bind(wx.EVT_MENU, self.on_menu_change_trayIconStyle, id=menuID)

                menuID += 1

                # Check active style
                if trayIconStyle == self.preferences["trayIconStyle"].replace("_", " "):
                    item.Check()


    #########################################
    ## PREFERENCES
    #########################################

    ####################
    # loadPreferences
    #-------------------
    # Load app preferences
    def loadPreferences(self):
        # Get global app preferences
        global app_preferences
        self.preferences = app_preferences

        # Create menu
        self.createMenu()

        # Restore preferences
        if self.preferences["tray"]:
            self.menuItem_tray.Check()

            if self.preferences["startMinimized"]:
                self.menuItem_startMinimized.Check()
            if self.preferences["closeToTray"]:
                self.menuItem_closeToTray.Check()
        else:
            # Make sure preferences that depend on "tray"
            # are disabled when "tray" is disabled
            self.menuItem_startMinimized.Check(False)
            self.menuItem_startMinimized.Enable(False)
            self.menuItem_closeToTray.Check(False)
            self.menuItem_closeToTray.Enable(False)

        if self.preferences["log"]:
            self.menuItem_log.Check()
        if self.preferences["profiles"]:
            self.menuItem_profiles.Check()
        if self.preferences["preview"]:
            self.menuItem_preview.Check()
        if self.preferences["applyStart"]:
            self.menuItem_applyStart.Check()
        if self.preferences["extendSpeed"]:
            self.menuItem_extendSpeed.Check()


        # Restore window position and size
        display     = wx.Display(self) # Get the display the application is shown on
        displayRect = display.GetClientArea()
        x = wx.DefaultCoord
        y = wx.DefaultCoord
        w = wx.DefaultSize.GetWidth()
        h = wx.DefaultSize.GetHeight()

        if "windowWidth" in self.preferences:
            if self.preferences["windowWidth"] > displayRect.Width:
                w = displayRect.Width
            else:
                w = self.preferences["windowWidth"]

        if "windowHeight" in self.preferences:
            if self.preferences["windowHeight"] > displayRect.Height:
                h = displayRect.Height
            else:
                h = self.preferences["windowHeight"]

        if "windowPosX" in self.preferences:
            # Not yet implemented because of 
            # concerns with multi monitor setups
            x = wx.DefaultCoord

        if "windowPosY" in self.preferences:
            # Not yet implemented because of 
            # concerns with multi monitor setups
            y = wx.DefaultCoord


        self.SetSize(x, y, w, h)


        # Restore sash positions
        if "sashPosHorizontal" in self.preferences:
            # Unbind from default wxFormBuilder idle event that would overwrite the position
            self.splitter_main_horizonzal.Unbind(wx.EVT_IDLE)

            # Bind to custom idle event to set sash pos after sizing
            self.splitter_main_horizonzal.Bind(wx.EVT_IDLE, self.on_idle_set_horizontal_sash_pos)

        # Restore sash positions
        if "sashPosVertical" in self.preferences:
            # Unbind from default wxFormBuilder idle event that would overwrite the position
            self.splitter_main_vertical.Unbind(wx.EVT_IDLE) 

            # Bind to custom idle event to set sash pos after sizing
            self.splitter_main_vertical.Bind(wx.EVT_IDLE, self.on_idle_set_vertical_sash_pos)


    ####################
    # createMenu
    #-------------------
    # Create submenus and menu entries
    def createMenu(self):
        # Show menu
        if self.preferences["menu"]:
            self.button_menu_left.Hide()
            self.button_menu_right.Hide()
        else:
            self.menubar_main.Hide()

            icon = wx.Image("./assets/menu.png")
            icon = icon.Scale(32, 32, wx.IMAGE_QUALITY_HIGH)
            self.button_menu_left.SetBitmap(icon)
            self.button_menu_right.SetBitmap(icon)

            self.button_menu_left.SetLabelText("")
            self.button_menu_right.SetLabelText("")

            if self.preferences["profiles"]:
                self.button_menu_left.Hide()
            else:
                self.button_menu_right.Hide()


        # Create submenus
        self.button_Menu = wx.Menu()

        # "File" menu
        self.menu_file = wx.Menu()
        self.menuItem_openProfileFolder = wx.MenuItem( self.menu_file, wx.ID_ANY, 
                                                       _(u"Open profile folder"), 
                                                       wx.EmptyString, wx.ITEM_NORMAL )

        
        self.menuItem_refreshProfileList = wx.MenuItem( self.menu_file, wx.ID_ANY, 
                                                        _(u"Refresh profile list"), 
                                                        wx.EmptyString, wx.ITEM_NORMAL )
        
        self.menuItem_quit = wx.MenuItem( self.menu_file, wx.ID_ANY, 
                                          _(u"Quit"), 
                                          wx.EmptyString, wx.ITEM_NORMAL )

        self.menu_file.Append( self.menuItem_openProfileFolder )
        self.menu_file.Append( self.menuItem_refreshProfileList )
        self.menu_file.Append( self.menuItem_quit )

        
        # "Options" menu
        self.menu_options = wx.Menu()
        self.menuItem_tray = wx.MenuItem( self.menu_options, wx.ID_ANY, 
                                          _(u"Show tray icon"), 
                                          wx.EmptyString, wx.ITEM_CHECK )

        self.menuItem_startMinimized = wx.MenuItem( self.menu_options, wx.ID_ANY, 
                                                    _(u"Start minimized"), 
                                                    wx.EmptyString, wx.ITEM_CHECK )

        self.menuItem_closeToTray = wx.MenuItem( self.menu_options, wx.ID_ANY, 
                                                 _(u"Close to tray"), 
                                                 wx.EmptyString, wx.ITEM_CHECK )
        
        self.menuItem_applyStart = wx.MenuItem( self.menu_options, wx.ID_ANY, 
                                                _(u"Apply [ACTIVE] on startup"), 
                                                wx.EmptyString, wx.ITEM_CHECK )
        
        self.menuItem_extendSpeed = wx.MenuItem( self.menu_options, wx.ID_ANY, 
                                                 _(u"Extend max speed"), 
                                                 wx.EmptyString, wx.ITEM_CHECK )
        
        self.subMenu_trayIconStyle = wx.Menu()
        self.subMenu_language = wx.Menu()

        self.menu_options.Append( self.menuItem_tray )
        self.menu_options.Append( self.menuItem_startMinimized )
        self.menu_options.Append( self.menuItem_closeToTray )
        self.menu_options.AppendSubMenu( self.subMenu_trayIconStyle, _(u"Tray icon style") )
        self.menu_options.AppendSeparator()
        self.menu_options.Append( self.menuItem_applyStart )
        self.menu_options.Append( self.menuItem_extendSpeed )
        self.menu_options.AppendSubMenu( self.subMenu_language, _(u"Language") )


        # "View" menu
        self.menu_view = wx.Menu()
        self.menuItem_log = wx.MenuItem( self.menu_view, wx.ID_ANY, 
                                         _(u"Show log"), 
                                         wx.EmptyString, wx.ITEM_CHECK )

        self.menuItem_profiles = wx.MenuItem( self.menu_view, wx.ID_ANY, 
                                              _(u"Show profiles"), 
                                              wx.EmptyString, wx.ITEM_CHECK )
        

        self.menuItem_preview = wx.MenuItem( self.menu_view, wx.ID_ANY, 
                                             _(u"Show preview"), 
                                             wx.EmptyString, wx.ITEM_CHECK )

        self.menu_view.Append( self.menuItem_log )
        self.menu_view.Append( self.menuItem_profiles )
        self.menu_view.Append( self.menuItem_preview )

        
        # "About" menu
        self.menu_about = wx.Menu()
        self.menuItem_about = wx.MenuItem( self.menu_about, wx.ID_ANY, 
                                           _(u"About RGB Config (acer-gkbbl-0)"), 
                                           wx.EmptyString, wx.ITEM_NORMAL )

        self.menu_about.Append( self.menuItem_about )


        # Bind menu events
        self.Bind( wx.EVT_MENU, self.on_menu_openProfileFolder, id = self.menuItem_openProfileFolder.GetId() )
        self.Bind( wx.EVT_MENU, self.on_menu_refreshProfileList, id = self.menuItem_refreshProfileList.GetId() )
        self.Bind( wx.EVT_MENU, self.on_force_close, id = self.menuItem_quit.GetId() )
        self.Bind( wx.EVT_MENU, self.on_menu_tray, id = self.menuItem_tray.GetId() )
        self.Bind( wx.EVT_MENU, self.on_menu_startMinimized, id = self.menuItem_startMinimized.GetId() )
        self.Bind( wx.EVT_MENU, self.on_menu_closeToTray, id = self.menuItem_closeToTray.GetId() )
        self.Bind( wx.EVT_MENU, self.on_menu_applyStart, id = self.menuItem_applyStart.GetId() )
        self.Bind( wx.EVT_MENU, self.on_menu_extendSpeed, id = self.menuItem_extendSpeed.GetId() )
        self.Bind( wx.EVT_MENU, self.on_menu_log, id = self.menuItem_log.GetId() )
        self.Bind( wx.EVT_MENU, self.on_menu_profiles, id = self.menuItem_profiles.GetId() )
        self.Bind( wx.EVT_MENU, self.on_menu_preview, id = self.menuItem_preview.GetId() )
        self.Bind( wx.EVT_MENU, self.on_menu_about, id = self.menuItem_about.GetId() )


        if self.preferences["menu"]:
            self.menubar_main.Append( self.menu_file, _(u"File") )
            self.menubar_main.Append( self.menu_options, _(u"Options") )
            self.menubar_main.Append( self.menu_view, _(u"View") )
            self.menubar_main.Append( self.menu_about, _(u"About") )
        else:
            self.button_Menu.AppendSubMenu( self.menu_file, _(u"File") )
            self.button_Menu.AppendSubMenu( self.menu_options, _(u"Options") )
            self.button_Menu.AppendSubMenu( self.menu_view, _(u"View") )
            self.button_Menu.AppendSubMenu( self.menu_about, _(u"About") )


    ####################
    # savePreferences
    #-------------------
    # Save app preferences
    def savePreferences(self):
        if not self.preferences["tray"]:
            # Make sure preferences that depend
            # on the tray are not enabled when tray is disabled
            self.preferences["startMinimized"] = False
            self.menuItem_startMinimized.Check(False)
            self.menuItem_startMinimized.Enable(False)

            self.preferences["closeToTray"] = False
            self.menuItem_closeToTray.Check(False)
            self.menuItem_closeToTray.Enable(False)
        else:
            self.menuItem_startMinimized.Enable()
            self.menuItem_closeToTray.Enable()

        # Save preferences to file
        with open(os.path.join(var.PREFERENCE_DIR, var.PREFERENCE_FILE), "w") as file:
            json.dump(self.preferences, file, indent=4)


    #########################################
    ## PROFILES
    #########################################

    ####################
    # listProfiles
    #-------------------
    # List available profiles
    def listProfiles(self):
        self.list_profiles.Clear()
        self.profiles = []

        # Search for profiles in profile dir
        for file in os.listdir(var.PROFILE_DIR):
            if os.path.isfile(os.path.join(var.PROFILE_DIR, file)):
                # Add profile to listbox
                self.list_profiles.Append(pathlib.Path(file).stem)

                # Add profile to internal list (used for tray menu)
                self.profiles.append(pathlib.Path(file).stem)

                # Sort profiles alphabetically
                self.profiles.sort(reverse=True)
            
        self.appLog(_("Profiles listed"))


    ####################
    # loadProfile
    #-------------------
    # Load given profile
    # - arg profile: string - profile name without path and extension
    def loadProfile(self, profile):
        if len(profile):
            # Generate default RGB settings
            self.settings = {
                "mode" : var.RGB_MODE_WAVE,
                "zone" : 1,
                "speed": 3,
                "brightness": 100,
                "direction" : 1,
                "red"  : 000,
                "green": 000,
                "blue" : 000,
                "colors": [
                    {"red": 000, "green": 000, "blue": 000},
                    {"red": 000, "green": 000, "blue": 000},
                    {"red": 000, "green": 000, "blue": 000},
                    {"red": 000, "green": 000, "blue": 000}
                ]
            }

            # Get profile path
            profile = os.path.join(var.PROFILE_DIR, profile) + var.PROFILE_EXTENSION

            # Check if profile available
            if os.path.isfile(profile):
                # Load profile and merge with default settings
                with open(f"{profile}", 'rt') as file:
                    self.settings = {**self.settings, **json.load(file)}

                self.appLog(_("Profile loaded: ") + profile, (0, 190, 0))

        # Restore RGB settings in dialog
        self.restoreRGBSettings()


    ####################
    # deleteProfile
    #-------------------
    # Delete selected profile
    # - arg profile: string - profile name without path and extension
    def deleteProfile(self, profile):

        # Confirm profile deletion with user
        dlg = wx.MessageDialog(self, _("Delete \"%s\"?")  % profile, _("Delete profile"), wx.YES_NO)
        res = dlg.ShowModal()

        if res == wx.ID_YES:
            # Get profile path
            profile = os.path.join(var.PROFILE_DIR, profile) + var.PROFILE_EXTENSION

            # Delete profile
            if os.path.isfile(profile):
                os.remove(profile)

            self.appLog(_("Profile deleted: ") + profile, (0, 190, 0))

            # Refresh profile list
            self.listProfiles()


    ####################
    # saveProfile
    #-------------------
    # Save current settings to profile
    # - arg profile (optional): string - profile name without path and extension
    def saveProfile(self, profile=""):
        self.getRGBSettings()

        res = 0

        # Ask user for profile name if no name was provided
        if not len(profile):
            dlg = wx.TextEntryDialog(self, _("Profile name"), _("Save profile"))
            res = dlg.ShowModal()

        if res == wx.ID_OK or len(profile):
            # Get user input if no name was provided
            if not len(profile):
                profile = str(dlg.GetValue())
            
            # Save profile to file
            if len(profile):
                with open(os.path.join(var.PROFILE_DIR, profile) + var.PROFILE_EXTENSION, "w") as file:
                    json.dump(self.settings, file, indent=4)

            self.appLog(_("Profile saved: ") + profile, (0, 190, 0))

            # Refresh profile list
            self.listProfiles()


    #########################################
    ## COMMUNICATION WITH CHARACTER DEVICE
    #########################################

    ####################
    # apply
    #-------------------
    # Apply current settings to character device
    def apply(self):
        # Check RGB device available
        if not os.path.exists(var.RGB_DEVICE):
            self.errLog(_("RGB Device %s not available") % var.RGB_DEVICE)
            return 

        # Get current settings from dialog
        self.getRGBSettings()

        # Save current settings as [ACTIVE] profile
        self.saveProfile(var.ACTIVE_PROFILE)

        if self.settings["mode"] == var.RGB_MODE_STATIC:
            # Check if static device available
            if not os.path.exists(var.RGB_DEVICE_STATIC):
                self.errLog(_("RGB Device %s not available") % var.RGB_DEVICE_STATIC)
                return 

            # Write RGB Settings for each zone to static device
            for zone, color in enumerate(self.settings["colors"]):

                # Set zone coloring
                pload = [0] * var.RGB_STATIC_PAYLOAD_SIZE

                pload[0] = 1 << zone
                pload[1] = color["red"]
                pload[2] = color["green"]
                pload[3] = color["blue"]

                # Write to Static device
                self.writePayload(var.RGB_DEVICE_STATIC, pload)

            # Activate Static mode
            pload = [0] * var.RGB_PAYLOAD_SIZE
            pload[2] = self.settings["brightness"]
            pload[9] = 1

            # Write to RGB device
            self.writePayload(var.RGB_DEVICE, pload)
        else:
            # Dynamic RGB mode
            pload = [0] * var.RGB_PAYLOAD_SIZE
            pload[0] = self.settings["mode"]
            pload[1] = self.settings["speed"]
            pload[2] = self.settings["brightness"]
            pload[3] = 8 if self.settings["mode"] == var.RGB_MODE_WAVE else 0
            pload[4] = self.settings["direction"]
            pload[5] = self.settings["red"]
            pload[6] = self.settings["green"]
            pload[7] = self.settings["blue"]
            pload[9] = 1

            # Write to RGB device
            self.writePayload(var.RGB_DEVICE, pload)

        self.appLog(_("Settings applied"), (0, 190, 0))


    ####################
    # writePayload
    #-------------------
    # Write given payload to character device
    # - arg device: string - path to character device
    # - arg pload: bytearray - payload
    def writePayload(self, device, pload):
        with open(device, "wb") as d:
            d.write(bytes(pload))
            self.appLog(_("Payload written to %s") % device + ": " + str(pload))


    #########################################
    ## LOGS
    #########################################

    ####################
    # appLog
    #-------------------
    # Output message in log widget
    # - arg message: string - message to output in log widget
    # - arg color (optional): byte tuple (r, g, b) (0-255)
    def appLog(self, message, color = False):
        # Print log message to console
        print(message)

        # Append log message to log widget
        self.rich_log.AppendText(message + "\n")

        # Apply color to length of message if provided
        if color:
            self.setLogTailStyle(len(message), {"color": color})

        # Scroll to end of log
        self.rich_log.ShowPosition(len(self.rich_log.GetValue()))


    ####################
    # urlLog
    #-------------------
    # Output message in log widget, formated as an URL
    # - arg url: string - url to output in log widget
    def urlLog(self, url):
        # Write log message to log widget
        self.appLog(url)

        # Apply url style to length of message
        self.setLogTailStyle(len(url), {"url": url})


    ####################
    # errLog
    #-------------------
    # Output error message in log widget
    # - arg message: string - error message to output in log window
    def errLog(self, message):
        # Write log message to log widget
        self.appLog(message)

        # Apply error color to length of message
        self.setLogTailStyle(len(message), {"color": (255, 0, 0)})


    ####################
    # setLogTailStyle
    #-------------------
    # Format last n characters of log
    # - arg tailLen: number of characters to style, counting from the end of the log widgets content
    # - arg styles: dict - members "color" as byte tuple (r, g, b) (0-255), "url" as string 
    def setLogTailStyle(self, tailLen, styles):
        logTextLen = len(self.rich_log.GetValue())

        # Increase tail length by 1 to
        # accommodate the new line character
        # that is automatically inserted by appLog()
        tailLen += 1

        textAttr = wx.TextAttr()

        # Set color style if provided
        if "color" in styles:
            textAttr.SetTextColour(wx.Colour(styles["color"]))

        # Set URL style if provided
        if "url" in styles and len(styles["url"]):
            textAttr.SetURL(styles["url"])

        # Apply style to the end of the text contained in the log widget
        # The length of text to style is determined be the tailLen argument
        self.rich_log.SetStyle(logTextLen - tailLen, logTextLen, textAttr)
        


####################
# class AcerRGBGUI
#-------------------
# Create wxpython application
class AcerRGBGUI(wx.App):
    def OnInit(self):
        self.mainFrame = AcerRGBGUI_Frame(None, _("Acer RGB Settings"))
        self.SetTopWindow(self.mainFrame)

        # Don't show the main windows when preferences set to start minimized
        if not self.mainFrame.preferences["startMinimized"] or not self.mainFrame.preferences["tray"]:
            self.mainFrame.Show(True)

        return True


# Main entry point
if __name__ == "__main__":
    # Create main window class
    app = AcerRGBGUI(redirect=False)

    # Run application
    app.MainLoop()
