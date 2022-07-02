#!/usr/bin/env python3

WXPYTHON_NOT_AVAILABLE = "wxPython not available\n\n" \
                         "Please install wxPython via your distributions package manager or python3 pip.\n\n" \
                         "e.g.\napt install python3-wxgtk4.0\n\n" \
                         "Visit\nhttps://wxpython.org/\nfor more information"

try:
    import wx
except ImportError:
    print("Error", WXPYTHON_NOT_AVAILABLE)

    try:
        from tkinter import Tk
        from tkinter import messagebox
        tk = Tk()
        tk.withdraw()
        messagebox.showerror("Error", WXPYTHON_NOT_AVAILABLE)
        tk.destroy()
    except ImportError:
        pass

    exit()

import os
import json
import pathlib
import webbrowser
import subprocess
import acer_rgb_keyboard_config_wx

from wx.adv import TaskBarIcon

FACER_RGB = "facer_rgb.py"

RGB_MODE_STATIC   = 0
RGB_MODE_BREATH   = 1
RGB_MODE_NEON     = 2
RGB_MODE_WAVE     = 3
RGB_MODE_SHIFTING = 4
RGB_MODE_ZOOM     = 5

RGB_PAYLOAD_SIZE         = 16
RGB_STATIC_PAYLOAD_SIZE  = 4

PROFILE_DIR = str(pathlib.Path.home()) + "/.config/predator/saved profiles"

RGB_DEVICE        = "/dev/acer-gkbbl-0"
RGB_DEVICE_STATIC = "/dev/acer-gkbbl-static-0"

DYNAMIC_TAY_START = 5
ACTIVE_PROFILE    = "[ACTIVE]"
PROFILE_EXTENSION = ".json"
PREFERENCE_DIR    = str(pathlib.Path.home()) + "/.config/acer_rgb_config"
PREFERENCE_FILE   = "preferences.json"

####################
# class AcerRGBGUI_Tray
#-------------------
# Handles tray icon
class AcerRGBGUI_Tray(TaskBarIcon):
    def __init__(self, parent):
        TaskBarIcon.__init__(self)

        self.parent = parent

        self.SetIcon(wx.Icon('./icon.png', wx.BITMAP_TYPE_PNG), "RGB Config")

        self.Bind(wx.EVT_MENU, self.on_toggle_gui   , id=1)
        self.Bind(wx.EVT_MENU, self.on_close_gui    , id=2)

        self.Bind(wx.adv.EVT_TASKBAR_LEFT_DOWN, self.on_toggle_gui)

    def CreatePopupMenu(self):
        menu = wx.Menu()

        menuID = DYNAMIC_TAY_START

        # Add available profiles dynamically
        for profile in self.parent.profiles:
            menu.Append(menuID, profile)
            self.Bind(wx.EVT_MENU, self.on_quick_profile, id=menuID)

            menuID += 1

        menu.AppendSeparator()

        menu.Append(1, "RGB Config")
        menu.Append(2, "Close")

        return menu

    def on_toggle_gui(self, event):
        if self.parent.IsShown():
            self.parent.Hide()
        else:
            self.parent.Show()

    def on_close_gui(self, event):
        self.parent.Close()

    def on_quick_profile(self, event):
        self.parent.loadProfile(self.parent.profiles[event.Id-DYNAMIC_TAY_START])
        self.parent.apply()


####################
# class AcerRGBGUI_Frame
#-------------------
# Extend wx wxPython Frame
class AcerRGBGUI_Frame(acer_rgb_keyboard_config_wx.MainFrame):
    def __init__(self, parent, title):
        acer_rgb_keyboard_config_wx.MainFrame.__init__(self, parent)

        self.colorWidgets = (self.color_color0,
                             self.color_color1,
                             self.color_color2,
                             self.color_color3)

        self.colorLabels  = (self.label_color0,
                             self.label_color1,
                             self.label_color2,
                             self.label_color3)

        self.SetIcon(wx.Icon('./icon.png', wx.BITMAP_TYPE_PNG))

        self.preferences = {}

        # Search for profiles
        self.profiles = []

        if not os.path.exists(PROFILE_DIR):
            os.makedirs(PROFILE_DIR)

        if not os.path.exists(PREFERENCE_DIR):
            os.makedirs(PREFERENCE_DIR)

        self.listProfiles()

        # Load last applied settigs
        self.loadProfile(ACTIVE_PROFILE)

        # Load app preferences
        self.loadPreferences()

        # Create tray icon
        if self.preferences["tray"]:
            self.createTrayIcon()

        # Apply log preference
        if not self.preferences["log"]:
            self.panel_bottom.Hide()
            self.splitter_main_horizonzal.Unsplit()

        # Apply profiles preference
        if not self.preferences["profiles"]:
            self.panel_right.Hide()
            self.splitter_main_vertical.Unsplit()

        # Check RGB Devices available
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

    ####################
    # on_close
    #-------------------
    def on_close(self, event):
        self.trayIcon.Destroy()
        self.Destroy()

    ####################
    # on_rgb_mode_select
    #-------------------
    def on_rgb_mode_select(self, event):
        self.setWidgetState()

    ####################
    # on_direction_select
    #-------------------
    def on_direction_select(self, event):
        self.setWidgetState()

    ####################
    # on_apply_click
    #-------------------
    def on_apply_click(self, event):
        self.apply()

    ####################
    # on_refresh_click
    #-------------------
    def on_refresh_click(self, event):
        self.listProfiles()

    ####################
    # on_delete_click
    #-------------------
    def on_delete_click(self, event):
        profile = self.list_profiles.GetStringSelection()
        self.deleteProfile(os.path.join(PROFILE_DIR, profile))

    ####################
    # on_load_click
    #-------------------
    def on_load_click(self, event):
        profile = self.list_profiles.GetStringSelection()
        self.loadProfile(profile)

    ####################
    # on_save_click
    #-------------------
    def on_save_click(self, event):
        self.saveProfile()

    ####################
    # on_log_url_click
    #-------------------
    def on_log_url_click(self, event):
        webbrowser.open(self.rich_log.GetValue()[event.GetURLStart():event.GetURLEnd()+1], new=0, autoraise=True)

    ####################
    # on_menu_openProfileFolder
    #-------------------
    def on_menu_openProfileFolder(self, event):
        subprocess.Popen(["xdg-open", PROFILE_DIR])

    ####################
    # on_menu_tray
    #-------------------
    def on_menu_tray(self, event):
        if self.menuItem_tray.IsChecked():
            self.createTrayIcon()
        else:
            self.trayIcon.Destroy()

        self.preferences["tray"] = self.menuItem_tray.IsChecked()
        self.savePreferences()

    ####################
    # on_menu_log
    #-------------------
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
    # createTrayIcon
    #-------------------
    def createTrayIcon(self):
        self.trayIcon = AcerRGBGUI_Tray(self)
        self.Bind(wx.EVT_CLOSE, self.on_close)

    ####################
    # setWidgetState
    #-------------------
    def setWidgetState(self):
        selection = self.choise_mode.GetSelection()

        if selection == RGB_MODE_STATIC:
            self.enableSpeed(0)
            self.enableDirection(0)
            self.enableColors((1, 1, 1, 1))
            self.animation_preview.LoadFile("./preview_gif/preview_static.gif", wx.adv.ANIMATION_TYPE_GIF)
            self.animation_preview.Play()

        if selection == RGB_MODE_BREATH:
            self.enableSpeed(1)
            self.enableDirection(0)
            self.enableColors((1, 0, 0, 0))
            self.animation_preview.LoadFile("./preview_gif/preview_breath.gif", wx.adv.ANIMATION_TYPE_GIF)
            self.animation_preview.Play()

        if selection == RGB_MODE_NEON:
            self.enableSpeed(1)
            self.enableDirection(0)
            self.enableColors((0, 0, 0, 0))
            self.animation_preview.LoadFile("./preview_gif/preview_neon.gif", wx.adv.ANIMATION_TYPE_GIF)
            self.animation_preview.Play()

        if selection == RGB_MODE_WAVE:
            self.enableSpeed(1)
            self.enableDirection(1)
            self.enableColors((0, 0, 0, 0))
            if self.radio_left_right.GetValue():
                self.animation_preview.LoadFile("./preview_gif/preview_wave_left_right.gif", wx.adv.ANIMATION_TYPE_GIF)
            else:
                self.animation_preview.LoadFile("./preview_gif/preview_wave_right_left.gif", wx.adv.ANIMATION_TYPE_GIF)
            self.animation_preview.Play()

        if selection == RGB_MODE_SHIFTING:
            self.enableSpeed(1)
            self.enableDirection(1)
            self.enableColors((1, 0, 0, 0))
            if self.radio_left_right.GetValue():
                self.animation_preview.LoadFile("./preview_gif/preview_shifting_left_right.gif", wx.adv.ANIMATION_TYPE_GIF)
            else:
                self.animation_preview.LoadFile("./preview_gif/preview_shifting_right_left.gif", wx.adv.ANIMATION_TYPE_GIF)
            self.animation_preview.Play()

        if selection == RGB_MODE_ZOOM:
            self.enableSpeed(1)
            self.enableDirection(0)
            self.enableColors((1, 0, 0, 0))
            self.animation_preview.LoadFile("./preview_gif/preview_zoom.gif", wx.adv.ANIMATION_TYPE_GIF)
            self.animation_preview.Play()


    ####################
    # enableSpeed
    #-------------------
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
    def enableColors(self, enabled):
        for index in range(4):
            if enabled[index]:
                self.colorWidgets[index].Enable()
                self.colorLabels[index].Enable()
            else:
                self.colorWidgets[index].Disable()
                self.colorLabels[index].Disable()

    ####################
    # enableDirection
    #-------------------
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
    # setDefaultSettings
    #-------------------
    def setDefaultSettings(self):
        # Default settings
        self.settings = {"mode": RGB_MODE_WAVE,
                         "zone": 1,
                         "speed": 3,
                         "brightness": 100,
                         "direction": 1,
                         "red": 000,
                         "green": 000,
                         "blue": 000,
                         "colors": [
                            {"red": 000, "green": 000, "blue": 000},
                            {"red": 000, "green": 000, "blue": 000},
                            {"red": 000, "green": 000, "blue": 000},
                            {"red": 000, "green": 000, "blue": 000}
                         ]}

    ####################
    # getSettings
    #-------------------
    def getSettings(self):
        self.settings["mode"]       = self.choise_mode.GetSelection()
        self.settings["speed"]      = self.slider_speed.GetValue()
        self.settings["brightness"] = self.slider_brightness.GetValue()

        if self.radio_left_right.GetValue():
            self.settings["direction"] = 1
        else:
            self.settings["direction"] = 2

        for i, widget in enumerate(self.colorWidgets):
            self.settings["colors"][i] = self.getColor(widget)

        self.settings["red"]   = self.settings["colors"][0]["red"]
        self.settings["green"] = self.settings["colors"][0]["green"]
        self.settings["blue"]  = self.settings["colors"][0]["blue"]

    ####################
    # restoreSettings
    #-------------------
    def restoreSettings(self):
        self.choise_mode.SetSelection(self.settings["mode"])
        self.slider_speed.SetValue(self.settings["speed"])
        self.slider_brightness.SetValue(self.settings["brightness"])

        if self.settings["direction"] == 1:
            self.radio_left_right.SetValue(True)
        else:
            self.radio_right_left.SetValue(True)

        for i, widget in enumerate(self.colorWidgets):
            self.setColor(widget, self.settings["colors"][i])

        self.setWidgetState()

    ####################
    # loadPreferences
    #-------------------
    def loadPreferences(self):
        self.preferences = {"tray": False,
                            "log": True,
                            "profiles": True}

        pref_file = os.path.join(PREFERENCE_DIR, PREFERENCE_FILE)

        if os.path.isfile(pref_file):
            with open(f"{pref_file}", 'rt') as file:
                self.preferences = {**self.preferences, **json.load(file)}

            if self.preferences["tray"]:
                self.menuItem_tray.Check()
            if self.preferences["log"]:
                self.menuItem_log.Check()
            if self.preferences["profiles"]:
                self.menuItem_profiles.Check()

            self.appLog("Preferences loaded: " + pref_file, (0, 190, 0))

    ####################
    # savePreferences
    #-------------------
    def savePreferences(self):
        with open(os.path.join(PREFERENCE_DIR, PREFERENCE_FILE), "w") as file:
            json.dump(self.preferences, file, indent=4)

    ####################
    # listProfiles
    #-------------------
    def listProfiles(self):
        self.list_profiles.Clear()
        self.profiles = []

        for file in os.listdir(PROFILE_DIR):
            if os.path.isfile(os.path.join(PROFILE_DIR, file)):
                self.list_profiles.Append(pathlib.Path(file).stem)
                self.profiles.append(pathlib.Path(file).stem)

                self.profiles.sort(reverse=True)
            
        self.appLog("Profiles listed")

    ####################
    # loadProfile
    #-------------------
    def loadProfile(self, profile):
        if len(profile):
            self.setDefaultSettings()

            profile = os.path.join(PROFILE_DIR, profile) + PROFILE_EXTENSION

            if os.path.isfile(profile):
                with open(f"{profile}", 'rt') as file:
                    self.settings = {**self.settings, **json.load(file)}

                self.appLog("Profile loaded: " + profile, (0, 190, 0))

        self.restoreSettings()

    ####################
    # deleteProfile
    #-------------------
    def deleteProfile(self, profile):
        dlg = wx.MessageDialog(self, "Delete \"" + profile + "\"?", "Delete profile", wx.YES_NO)
        res = dlg.ShowModal()

        if res == wx.ID_YES:

            profile += PROFILE_EXTENSION

            if os.path.isfile(profile):
                os.remove(profile)

            self.appLog("Profile deleted: " + profile, (0, 190, 0))
            self.listProfiles()

    ####################
    # saveProfile
    #-------------------
    def saveProfile(self, profile=""):
        self.getSettings()

        res = 0

        if not len(profile):
            dlg = wx.TextEntryDialog(self, "Profile name", "Save profile")
            res = dlg.ShowModal()

        if res == wx.ID_OK or len(profile):
            if not len(profile):
                profile = str(dlg.GetValue())
            
            if len(profile):
                with open(os.path.join(PROFILE_DIR, profile) + PROFILE_EXTENSION, "w") as file:
                    json.dump(self.settings, file, indent=4)

            self.appLog("Profile saved: " + profile, (0, 190, 0))
            self.listProfiles()

    ####################
    # getColor
    #-------------------
    def getColor(self, widget):
        color = widget.GetColour()
        return {"red": color.Red(), "green": color.Green(), "blue": color.Blue()}

    ####################
    # setColor
    #-------------------
    def setColor(self, widget, color):
        widget.SetColour(wx.Colour(color["red"], color["green"], color["blue"]))

    ####################
    # apply
    #-------------------
    def apply(self):
        self.getSettings()

        self.saveProfile(ACTIVE_PROFILE)

        if self.settings["mode"] == RGB_MODE_STATIC:
            # Static RGB mode
            zone = 1

            for color in self.settings["colors"]:

                # Set zone coloring
                pload = [0] * RGB_STATIC_PAYLOAD_SIZE

                pload[0] = zone
                pload[1] = color["red"]
                pload[2] = color["green"]
                pload[3] = color["blue"]

                zone += 1

                # Write to Static device
                with open(RGB_DEVICE_STATIC, "wb") as device:
                    device.write(bytes(pload))

                self.appLog("Payload written to " + RGB_DEVICE_STATIC + ": " + str(pload))

            # Activate Static mode
            pload = [0] * RGB_PAYLOAD_SIZE
            pload[2] = self.settings["brightness"]

            # Write to RGB device
            with open(RGB_DEVICE, 'wb') as device:
                device.write(bytes(pload))

            self.appLog("Payload written to " + RGB_DEVICE + ": " + str(pload))
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
            with open(RGB_DEVICE, 'wb') as device:
                device.write(bytes(pload))

            self.appLog("Payload written to " + RGB_DEVICE + ": " + str(pload))

        self.appLog("Settings applied", (0, 190, 0))

    ####################
    # appLog
    #-------------------
    def appLog(self, message, color = False):
        print(message)

        self.rich_log.AppendText(message + "\n")

        if color:
            self.setLogTailStyle(len(message), {"color": color})

        self.rich_log.ShowPosition(len(self.rich_log.GetValue()))

    ####################
    # urlLog
    #-------------------
    def urlLog(self, url):
        self.appLog(url)
        self.setLogTailStyle(len(url), {"url": url})

    ####################
    # errLog
    #-------------------
    def errLog(self, message):
        self.appLog(message)
        self.setLogTailStyle(len(message), {"color": (255, 0, 0)})

    ####################
    # setLogTailStyle
    #-------------------
    def setLogTailStyle(self, tailLen, styles):
        logTextLen = len(self.rich_log.GetValue())

        tailLen += 1 # \n

        textAttr = wx.TextAttr()
        if "color" in styles:
            textAttr.SetTextColour(wx.Colour(styles["color"]))
        if "url" in styles and len(styles["url"]):
            textAttr.SetURL(styles["url"])

        self.rich_log.SetStyle(logTextLen - tailLen, logTextLen, textAttr)
        


####################
# class AcerRGBGUI
#-------------------
# Create wxpython app
class AcerRGBGUI(wx.App):
    def OnInit(self):
        self.mainFrame = AcerRGBGUI_Frame(None, "Acer RGB Settings")
        self.SetTopWindow(self.mainFrame)
        self.mainFrame.Show(True)

        return True


# Main entry point
if __name__ == "__main__":
    app = AcerRGBGUI(redirect=False)
    app.MainLoop()
