#!/usr/bin/env python3

#################################################################################################
## RGB Config (acer-gkbbl-0) - https://github.com/x211321/Acer-RGB-Keyboard-Config-Linux           
##
## A graphical user interface to interact with the RGB controls of the acer-gkbbl-0 Kernel module 
## by JafarAkhondali. The kernel module must be installed seperatly for this application to work 
##
## Visit https://github.com/JafarAkhondali/acer-predator-turbo-and-rgb-keyboard-linux-module
## for additional information regarding the kernel module
#################################################################################################
## MIT License
## Copyright 2022 x211321 (https://github.com/x211321)
## View the acompaning LICENSE file for additional licensing information
#################################################################################################

# Error message if wxPython is not available
WXPYTHON_NOT_AVAILABLE = "wxPython not available\n\n" \
                         "Please install wxPython via your distributions package manager or python3 pip.\n\n" \
                         "e.g.\napt install python3-wxgtk4.0\n\n" \
                         "Visit\nhttps://wxpython.org/\nfor more information"

# Try importing wxPython
# give error message if not available
try:
    import wx
except ImportError:
    # Print error to console
    print("Error", WXPYTHON_NOT_AVAILABLE)

    try:
        # Try importing tkinter to show error messagebox
        from tkinter import Tk
        from tkinter import messagebox
        tk = Tk()
        tk.withdraw()
        messagebox.showerror("Error", WXPYTHON_NOT_AVAILABLE)
        tk.destroy()
    except ImportError:
        # If tkinter is also not available: hope the user
        # has seen the above console message
        pass

    exit()

# Imports without external dependencies
import os
import json
import pathlib
import webbrowser
import subprocess

# App GUI managed by wxFormBuilder
import acer_rgb_keyboard_config_wx

# Advanced wxPython imports
from wx.adv import TaskBarIcon

# RGB-Mode constants
RGB_MODE_STATIC   = 0
RGB_MODE_BREATH   = 1
RGB_MODE_NEON     = 2
RGB_MODE_WAVE     = 3
RGB_MODE_SHIFTING = 4
RGB_MODE_ZOOM     = 5

# Payload sizes
RGB_PAYLOAD_SIZE         = 16
RGB_STATIC_PAYLOAD_SIZE  = 4

# RGB kernel devices
RGB_DEVICE        = "/dev/acer-gkbbl-0"
RGB_DEVICE_STATIC = "/dev/acer-gkbbl-static-0"

# Profile directory
#   profiles are ment to be compatible with the facer_rgb.py script
#   that comes with JafarAkhondali's kernel module
#   https://github.com/JafarAkhondali/acer-predator-turbo-and-rgb-keyboard-linux-module
PROFILE_DIR = str(pathlib.Path.home()) + "/.config/predator/saved profiles"

# Miscellaneous constants
DYNAMIC_TRAY_START = 5
ACTIVE_PROFILE     = "[ACTIVE]"
PROFILE_EXTENSION  = ".json"
PREFERENCE_DIR     = str(pathlib.Path.home()) + "/.config/acer_rgb_config"
PREFERENCE_FILE    = "preferences.json"


####################
# class AcerRGBGUI_Tray
#-------------------
# Handles tray icon
class AcerRGBGUI_Tray(TaskBarIcon):
    def __init__(self, parent):
        TaskBarIcon.__init__(self)

        self.parent = parent

        # Set tray icon
        self.SetIcon(wx.Icon('./icon.png', wx.BITMAP_TYPE_PNG), "RGB Config")

        # Static bindings for hide / restore and quit
        self.Bind(wx.EVT_MENU, self.on_toggle_gui        , id=1)
        self.Bind(wx.EVT_MENU, self.parent.on_force_close, id=2)

        # Hide / restore main window on left click
        self.Bind(wx.adv.EVT_TASKBAR_LEFT_DOWN, self.on_toggle_gui)

    def CreatePopupMenu(self):
        menu   = wx.Menu()
        menuID = DYNAMIC_TRAY_START

        # Add available profiles dynamically
        for profile in self.parent.profiles:
            menu.Append(menuID, profile)
            self.Bind(wx.EVT_MENU, self.on_quick_profile, id=menuID)

            menuID += 1

        # Separate profiles from static menu items
        menu.AppendSeparator()

        # Add static menu items
        menu.Append(1, "RGB Config")
        menu.Append(2, "Close")

        return menu

    def on_toggle_gui(self, event):
        if self.parent.IsShown():
            self.parent.Hide()
        else:
            self.parent.Show()

    def on_quick_profile(self, event):
        self.parent.loadProfile(self.parent.profiles[event.Id-DYNAMIC_TRAY_START])
        self.parent.apply()


####################
# class AcerRGBGUI_About
#-------------------
# Extend wx wxPython About dialog
class AcerRGBGUI_About(acer_rgb_keyboard_config_wx.dialog_about):
    def __init__(self, parent):
        acer_rgb_keyboard_config_wx.dialog_about.__init__(self, parent)

    def on_button_about_close_click(self, event):
        self.Destroy()


####################
# class AcerRGBGUI_Frame
#-------------------
# Extend wx wxPython Frame
class AcerRGBGUI_Frame(acer_rgb_keyboard_config_wx.frame_main):

    #########################################
    ## MAIN WINDOW INIT
    #########################################

    ####################
    # __init__
    #-------------------
    def __init__(self, parent, title):
        acer_rgb_keyboard_config_wx.frame_main.__init__(self, parent)

        # Set app icon
        self.SetIcon(wx.Icon('./icon.png', wx.BITMAP_TYPE_PNG))

        # Defince color widgets
        self.colorWidgets = [
            {"widget": self.color_color0, "label": self.label_color0},
            {"widget": self.color_color1, "label": self.label_color1},
            {"widget": self.color_color2, "label": self.label_color2},
            {"widget": self.color_color3, "label": self.label_color3}
        ]

        # Define the different widget states in regard to the selected RGB mode
        self.widgetStates = [
            {"mode": RGB_MODE_STATIC  , "speed": 0, "direction": 0, "colors": (1,1,1,1), "animation": "preview_static"},
            {"mode": RGB_MODE_BREATH  , "speed": 1, "direction": 0, "colors": (1,0,0,0), "animation": "preview_breath"},
            {"mode": RGB_MODE_NEON    , "speed": 1, "direction": 0, "colors": (0,0,0,0), "animation": "preview_neon"},
            {"mode": RGB_MODE_WAVE    , "speed": 1, "direction": 1, "colors": (0,0,0,0), "animation": "preview_wave"},
            {"mode": RGB_MODE_SHIFTING, "speed": 1, "direction": 1, "colors": (1,0,0,0), "animation": "preview_shifting"},
            {"mode": RGB_MODE_ZOOM    , "speed": 1, "direction": 0, "colors": (1,0,0,0), "animation": "preview_zoom"}
        ]

        # Create config directories
        if not os.path.exists(PROFILE_DIR):
            os.makedirs(PROFILE_DIR)

        if not os.path.exists(PREFERENCE_DIR):
            os.makedirs(PREFERENCE_DIR)

        # Load app preferences
        self.preferences = {}
        self.loadPreferences()

        # List profiles
        self.profiles = []
        self.listProfiles()

        # Load last applied settigs
        self.loadProfile(ACTIVE_PROFILE)

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

        # Check RGB Devices available
        # - show error message in log when device not found
        if os.path.exists(RGB_DEVICE):
            self.appLog("RGB device " + RGB_DEVICE + " detected")
        else:
            self.errLog("ERROR: RGB device " + RGB_DEVICE + " not found")
            self.appLog("Install instructions:")
            self.urlLog("https://github.com/JafarAkhondali/acer-predator-turbo-and-rgb-keyboard-linux-module")

        if os.path.exists(RGB_DEVICE_STATIC):
            self.appLog("Static RGB device " + RGB_DEVICE_STATIC + " detected")
        else:
            self.errLog("ERROR: Static RGB device " + RGB_DEVICE_STATIC + " not found")
            self.appLog("Install instructions:")
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
        self.trayIcon.Destroy()
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
    # on_apply_click
    #-------------------
    # Event handler - apply RGB settings click
    def on_apply_click(self, event):
        self.apply()


    ####################
    # on_refresh_click
    #-------------------
    # Event handler - profiles refresh button click
    def on_refresh_click(self, event):
        self.listProfiles()


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
    # on_menu_openProfileFolder
    #-------------------
    # Event handler - open profile folder
    def on_menu_openProfileFolder(self, event):
        subprocess.Popen(["xdg-open", PROFILE_DIR])


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
            dlg = wx.MessageDialog(self, "Offical Acer software only allows speed values between 0 and 9.\n\n" \
                                        "In theory the acer-gkbbl-0 kernel module accepts speed values between 0 and 255. " \
                                        "Values above the standard limit of 9 might yield undesired results.\n\n" \
                                        "It is advised to proceed with caution.\n\n" \
                                        "Are you sure you want to extend the speed limit?"
                                        , "Extend max speed", wx.YES_NO)
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
            self.splitter_main_horizonzal.SetSashPosition(460)
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
            self.splitter_main_vertical.SetSashPosition(500)
        else:
            self.panel_right.Hide()
            self.splitter_main_vertical.Unsplit()

        self.preferences["profiles"] = self.menuItem_log.IsChecked()
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
        dlg = AcerRGBGUI_About(self)
        dlg.ShowModal()


    #########################################
    ## DIALOG INTERACTION
    #########################################

    ####################
    # createTrayIcon
    #-------------------
    # Create the tray icon
    def createTrayIcon(self):
        self.trayIcon = AcerRGBGUI_Tray(self)
        self.Bind(wx.EVT_CLOSE, self.on_close)


    ####################
    # setPreviewAnimation
    #-------------------
    # Plays preview animation according to the selected RGB mode
    def setPreviewAnimation(self):
        # Default none-preview
        file = "./preview_gif/preview_none.gif"

        # Set specific preview when previews enabled
        if self.preferences["preview"]:
            file = os.path.join("./preview_gif/", self.widgetStates[self.choise_mode.GetSelection()]["animation"]) + ".gif"

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
                self.colorWidgets[index]["label"].Enable()
            else:
                self.colorWidgets[index]["widget"].Disable()
                self.colorWidgets[index]["label"].Disable()


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


    #########################################
    ## PREFERENCES
    #########################################

    ####################
    # loadPreferences
    #-------------------
    # Load app preferences
    def loadPreferences(self):
        # Set default preferences
        self.preferences = {
            "tray"          : False,
            "log"           : True,
            "profiles"      : True,
            "preview"       : True,
            "startMinimized": False,
            "closeToTray"   : False,
            "applyStart"    : False,
            "extendSpeed"   : False
        }

        # Get path to preference file
        pref_file = os.path.join(PREFERENCE_DIR, PREFERENCE_FILE)

        if os.path.isfile(pref_file):
            # Read preferences from file and merge with default preferences
            with open(f"{pref_file}", 'rt') as file:
                self.preferences = {**self.preferences, **json.load(file)}

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

            self.appLog("Preferences loaded: " + pref_file, (0, 190, 0))


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
        with open(os.path.join(PREFERENCE_DIR, PREFERENCE_FILE), "w") as file:
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
        for file in os.listdir(PROFILE_DIR):
            if os.path.isfile(os.path.join(PROFILE_DIR, file)):
                # Add profile to listbox
                self.list_profiles.Append(pathlib.Path(file).stem)

                # Add profile to internal list (used for tray menu)
                self.profiles.append(pathlib.Path(file).stem)

                # Sort profiles alphabetically
                self.profiles.sort(reverse=True)
            
        self.appLog("Profiles listed")


    ####################
    # loadProfile
    #-------------------
    # Load given profile
    # - arg profile: string - profile name without path and extension
    def loadProfile(self, profile):
        if len(profile):
            # Generate default RGB settings
            self.settings = {
                "mode" : RGB_MODE_WAVE,
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
            profile = os.path.join(PROFILE_DIR, profile) + PROFILE_EXTENSION

            # Check if profile available
            if os.path.isfile(profile):
                # Load profile and merge with default settings
                with open(f"{profile}", 'rt') as file:
                    self.settings = {**self.settings, **json.load(file)}

                self.appLog("Profile loaded: " + profile, (0, 190, 0))

        # Restore RGB settings in dialog
        self.restoreRGBSettings()


    ####################
    # deleteProfile
    #-------------------
    # Delete selected profile
    # - arg profile: string - profile name without path and extension
    def deleteProfile(self, profile):

        # Confirm profile deletion with user
        dlg = wx.MessageDialog(self, "Delete \"" + profile + "\"?", "Delete profile", wx.YES_NO)
        res = dlg.ShowModal()

        if res == wx.ID_YES:
            # Get profile path
            profile = os.path.join(PROFILE_DIR, profile) + PROFILE_EXTENSION

            # Delete profile
            if os.path.isfile(profile):
                os.remove(profile)

            self.appLog("Profile deleted: " + profile, (0, 190, 0))

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
            dlg = wx.TextEntryDialog(self, "Profile name", "Save profile")
            res = dlg.ShowModal()

        if res == wx.ID_OK or len(profile):
            # Get user input if no name was provided
            if not len(profile):
                profile = str(dlg.GetValue())
            
            # Save profile to file
            if len(profile):
                with open(os.path.join(PROFILE_DIR, profile) + PROFILE_EXTENSION, "w") as file:
                    json.dump(self.settings, file, indent=4)

            self.appLog("Profile saved: " + profile, (0, 190, 0))

            # Refresh profile list
            self.listProfiles()


    #########################################
    ## COMMUNICATION WITH KERNEL MODULE
    #########################################

    ####################
    # apply
    #-------------------
    # Apply current settings to kernel device
    def apply(self):
        # Check RGB device available
        if not os.path.exists(RGB_DEVICE):
            self.errLog("RGB Device " + RGB_DEVICE + " not available")
            return 

        # Get current settings from dialog
        self.getRGBSettings()

        # Save current settings as [ACTIVE] profile
        self.saveProfile(ACTIVE_PROFILE)

        if self.settings["mode"] == RGB_MODE_STATIC:
            # Check if static device available
            if not os.path.exists(RGB_DEVICE_STATIC):
                self.errLog("RGB Device " + RGB_DEVICE_STATIC + " not available")
                return 

            # Write RGB Settings for each zone to static device
            for zone, color in enumerate(self.settings["colors"]):

                # Set zone coloring
                pload = [0] * RGB_STATIC_PAYLOAD_SIZE

                pload[0] = zone + 1
                pload[1] = color["red"]
                pload[2] = color["green"]
                pload[3] = color["blue"]

                # Write to Static device
                self.writePayload(RGB_DEVICE_STATIC, pload)

            # Activate Static mode
            pload = [0] * RGB_PAYLOAD_SIZE
            pload[2] = self.settings["brightness"]

            # Write to RGB device
            self.writePayload(RGB_DEVICE, pload)
        else:
            # Dynamic RGB mode
            pload = [0] * RGB_PAYLOAD_SIZE
            pload[0] = self.settings["mode"]
            pload[1] = self.settings["speed"]
            pload[2] = self.settings["brightness"]
            pload[3] = 8 if self.settings["mode"] == RGB_MODE_WAVE else 0
            pload[4] = self.settings["direction"]
            pload[5] = self.settings["red"]
            pload[6] = self.settings["green"]
            pload[7] = self.settings["blue"]

            # Write to RGB device
            self.writePayload(RGB_DEVICE, pload)

        self.appLog("Settings applied", (0, 190, 0))


    ####################
    # writePayload
    #-------------------
    # Write given payload to kernel device
    # - arg device: string - path to kernel device
    # - arg pload: bytearray - payload
    def writePayload(self, device, pload):
        with open(device, "wb") as d:
            d.write(bytes(pload))
            self.appLog("Payload written to " + device + ": " + str(pload))


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
        self.mainFrame = AcerRGBGUI_Frame(None, "Acer RGB Settings")
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
