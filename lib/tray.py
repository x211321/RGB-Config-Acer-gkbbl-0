import wx
from wx.adv import TaskBarIcon

import gettext
_ = gettext.gettext

DYNAMIC_TRAY_START = 5

#######################
# class AcerRGBGUI_Tray
#----------------------
# Handles tray icon
class AcerRGBGUI_Tray(TaskBarIcon):
    def __init__(self, parent):
        TaskBarIcon.__init__(self)

        self.parent = parent

        # Set tray icon
        self.UpdateIcon()

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
        menu.Append(1, _("RGB Config"))
        menu.Append(2, _("Close"))

        return menu

    def UpdateIcon(self):
        self.SetIcon(wx.Icon('./assets/tray/%s.png' % self.parent.preferences["trayIconStyle"], wx.BITMAP_TYPE_PNG), _("RGB Config"))

    def on_toggle_gui(self, event):
        if self.parent.IsShown():
            self.parent.Hide()

            # Destroy about dialog if open
            if self.parent.aboutDlg:
                self.parent.aboutDlg.Destroy()
                self.parent.aboutDlg = None
        else:
            self.parent.Show()

    def on_quick_profile(self, event):
        self.parent.loadProfile(self.parent.profiles[event.Id-DYNAMIC_TRAY_START])
        self.parent.apply()
