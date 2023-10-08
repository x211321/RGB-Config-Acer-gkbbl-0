# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv
import wx.richtext

import gettext
_ = gettext.gettext

###########################################################################
## Class frame_main
###########################################################################

class frame_main ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"RGB Config (acer-gkbbl-0)"), pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        horizontal_main = wx.BoxSizer( wx.HORIZONTAL )

        vertical_main = wx.BoxSizer( wx.VERTICAL )

        self.splitter_main_horizonzal = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D|wx.SP_LIVE_UPDATE )
        self.splitter_main_horizonzal.Bind( wx.EVT_IDLE, self.splitter_main_horizonzalOnIdle )

        self.panel_top = wx.Panel( self.splitter_main_horizonzal, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        vertical_top = wx.BoxSizer( wx.VERTICAL )

        self.splitter_main_vertical = wx.SplitterWindow( self.panel_top, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_LIVE_UPDATE|wx.SP_NOBORDER|wx.SP_THIN_SASH )
        self.splitter_main_vertical.Bind( wx.EVT_IDLE, self.splitter_main_verticalOnIdle )

        self.panel_left = wx.Panel( self.splitter_main_vertical, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        vertical_settings = wx.BoxSizer( wx.VERTICAL )


        vertical_settings.Add( ( 0, 10), 0, wx.EXPAND, 5 )

        self.label_settings = wx.StaticText( self.panel_left, wx.ID_ANY, _(u"Settings"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.label_settings.Wrap( -1 )

        self.label_settings.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        vertical_settings.Add( self.label_settings, 0, wx.EXPAND|wx.LEFT|wx.TOP, 5 )

        self.m_staticline1 = wx.StaticLine( self.panel_left, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        vertical_settings.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

        horizontal_mode = wx.BoxSizer( wx.HORIZONTAL )

        self.label_mode = wx.StaticText( self.panel_left, wx.ID_ANY, _(u"RGB Mode"), wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_LEFT )
        self.label_mode.Wrap( -1 )

        horizontal_mode.Add( self.label_mode, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        bSizer16 = wx.BoxSizer( wx.HORIZONTAL )

        choise_modeChoices = [ _(u"Static"), _(u"Breath"), _(u"Neon"), _(u"Wave"), _(u"Shifting"), _(u"Zoom") ]
        self.choise_mode = wx.Choice( self.panel_left, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choise_modeChoices, 0 )
        self.choise_mode.SetSelection( 0 )
        bSizer16.Add( self.choise_mode, 3, wx.ALIGN_LEFT|wx.ALL, 5 )

        self.animation_preview = wx.adv.AnimationCtrl( self.panel_left, wx.ID_ANY, wx.adv.NullAnimation, wx.DefaultPosition, wx.Size( 60,40 ), wx.adv.AC_DEFAULT_STYLE|wx.adv.AC_NO_AUTORESIZE )
        bSizer16.Add( self.animation_preview, 0, wx.ALL|wx.EXPAND, 5 )


        horizontal_mode.Add( bSizer16, 2, wx.EXPAND, 5 )


        vertical_settings.Add( horizontal_mode, 0, wx.EXPAND, 5 )

        horizontal_brightness = wx.BoxSizer( wx.HORIZONTAL )

        self.label_brightness = wx.StaticText( self.panel_left, wx.ID_ANY, _(u"Brightness"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.label_brightness.Wrap( -1 )

        horizontal_brightness.Add( self.label_brightness, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.slider_brightness = wx.Slider( self.panel_left, wx.ID_ANY, 100, 0, 100, wx.DefaultPosition, wx.Size( -1,-1 ), wx.SL_HORIZONTAL|wx.SL_VALUE_LABEL )
        horizontal_brightness.Add( self.slider_brightness, 2, wx.ALL|wx.EXPAND, 5 )


        vertical_settings.Add( horizontal_brightness, 0, wx.EXPAND, 5 )

        horizontal_speed = wx.BoxSizer( wx.HORIZONTAL )

        self.label_speed = wx.StaticText( self.panel_left, wx.ID_ANY, _(u"Speed"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.label_speed.Wrap( -1 )

        horizontal_speed.Add( self.label_speed, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.slider_speed = wx.Slider( self.panel_left, wx.ID_ANY, 3, 0, 9, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL|wx.SL_VALUE_LABEL )
        horizontal_speed.Add( self.slider_speed, 2, wx.ALL|wx.EXPAND, 5 )


        vertical_settings.Add( horizontal_speed, 0, wx.EXPAND, 5 )

        horizontal_direction = wx.BoxSizer( wx.HORIZONTAL )

        self.label_direction = wx.StaticText( self.panel_left, wx.ID_ANY, _(u"Direction"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.label_direction.Wrap( -1 )

        horizontal_direction.Add( self.label_direction, 1, wx.ALL|wx.EXPAND, 5 )

        self.radio_left_right = wx.RadioButton( self.panel_left, wx.ID_ANY, _(u"Left to Right"), wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
        horizontal_direction.Add( self.radio_left_right, 1, wx.ALL|wx.EXPAND, 5 )

        self.radio_right_left = wx.RadioButton( self.panel_left, wx.ID_ANY, _(u"Right to Left"), wx.DefaultPosition, wx.DefaultSize, 0 )
        horizontal_direction.Add( self.radio_right_left, 1, wx.ALL|wx.EXPAND, 5 )


        vertical_settings.Add( horizontal_direction, 0, wx.EXPAND, 5 )

        horizontal_color1 = wx.BoxSizer( wx.HORIZONTAL )

        self.label_color0 = wx.StaticText( self.panel_left, wx.ID_ANY, _(u"Color section 1"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.label_color0.Wrap( -1 )

        horizontal_color1.Add( self.label_color0, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.color_color0 = wx.ColourPickerCtrl( self.panel_left, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
        horizontal_color1.Add( self.color_color0, 2, wx.ALL|wx.EXPAND, 5 )


        vertical_settings.Add( horizontal_color1, 0, wx.EXPAND, 5 )

        horizontal_color2 = wx.BoxSizer( wx.HORIZONTAL )

        self.label_color1 = wx.StaticText( self.panel_left, wx.ID_ANY, _(u"Color section 2"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.label_color1.Wrap( -1 )

        horizontal_color2.Add( self.label_color1, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.color_color1 = wx.ColourPickerCtrl( self.panel_left, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
        horizontal_color2.Add( self.color_color1, 2, wx.ALL|wx.EXPAND, 5 )


        vertical_settings.Add( horizontal_color2, 0, wx.EXPAND, 5 )

        horizontal_color3 = wx.BoxSizer( wx.HORIZONTAL )

        self.label_color2 = wx.StaticText( self.panel_left, wx.ID_ANY, _(u"Color section 3"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.label_color2.Wrap( -1 )

        horizontal_color3.Add( self.label_color2, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.color_color2 = wx.ColourPickerCtrl( self.panel_left, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
        horizontal_color3.Add( self.color_color2, 2, wx.ALL|wx.EXPAND, 5 )


        vertical_settings.Add( horizontal_color3, 0, wx.EXPAND, 5 )

        horizontal_color4 = wx.BoxSizer( wx.HORIZONTAL )

        self.label_color3 = wx.StaticText( self.panel_left, wx.ID_ANY, _(u"Color section 4"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.label_color3.Wrap( -1 )

        horizontal_color4.Add( self.label_color3, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.color_color3 = wx.ColourPickerCtrl( self.panel_left, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
        horizontal_color4.Add( self.color_color3, 2, wx.ALL|wx.EXPAND, 5 )


        vertical_settings.Add( horizontal_color4, 0, wx.EXPAND, 5 )


        vertical_settings.Add( ( 0, 10), 1, wx.EXPAND, 5 )

        grid_settings_buttons = wx.GridSizer( 0, 2, 0, 0 )

        self.button_save = wx.Button( self.panel_left, wx.ID_ANY, _(u"Save as profile"), wx.DefaultPosition, wx.DefaultSize, 0 )
        grid_settings_buttons.Add( self.button_save, 0, wx.ALIGN_LEFT|wx.ALL, 10 )

        self.button_apply = wx.Button( self.panel_left, wx.ID_ANY, _(u"Apply"), wx.DefaultPosition, wx.DefaultSize, 0 )
        grid_settings_buttons.Add( self.button_apply, 0, wx.ALIGN_RIGHT|wx.ALL, 10 )


        vertical_settings.Add( grid_settings_buttons, 0, wx.EXPAND, 5 )


        self.panel_left.SetSizer( vertical_settings )
        self.panel_left.Layout()
        vertical_settings.Fit( self.panel_left )
        self.panel_right = wx.Panel( self.splitter_main_vertical, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        vertical_profiles = wx.BoxSizer( wx.VERTICAL )


        vertical_profiles.Add( ( 0, 10), 0, wx.EXPAND, 5 )

        self.label_profiles = wx.StaticText( self.panel_right, wx.ID_ANY, _(u"Profiles"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.label_profiles.Wrap( -1 )

        self.label_profiles.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        vertical_profiles.Add( self.label_profiles, 0, wx.EXPAND|wx.LEFT|wx.TOP, 5 )

        self.m_staticline2 = wx.StaticLine( self.panel_right, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        vertical_profiles.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )

        list_profilesChoices = []
        self.list_profiles = wx.ListBox( self.panel_right, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, list_profilesChoices, wx.LB_SINGLE|wx.LB_SORT )
        vertical_profiles.Add( self.list_profiles, 1, wx.ALL|wx.EXPAND, 5 )


        vertical_profiles.Add( ( 0, 4), 0, wx.EXPAND, 5 )

        grid_profile_buttons = wx.GridSizer( 0, 3, 0, 0 )

        self.button_refresh = wx.Button( self.panel_right, wx.ID_ANY, _(u"Refresh"), wx.DefaultPosition, wx.DefaultSize, 0 )
        grid_profile_buttons.Add( self.button_refresh, 0, wx.ALIGN_LEFT|wx.ALL, 10 )

        self.button_delete = wx.Button( self.panel_right, wx.ID_ANY, _(u"Delete"), wx.DefaultPosition, wx.DefaultSize, 0 )
        grid_profile_buttons.Add( self.button_delete, 0, wx.ALIGN_CENTER|wx.ALL, 10 )

        self.button_load = wx.Button( self.panel_right, wx.ID_ANY, _(u"Load"), wx.DefaultPosition, wx.DefaultSize, 0 )
        grid_profile_buttons.Add( self.button_load, 0, wx.ALIGN_RIGHT|wx.ALL, 10 )


        vertical_profiles.Add( grid_profile_buttons, 0, wx.EXPAND, 5 )


        self.panel_right.SetSizer( vertical_profiles )
        self.panel_right.Layout()
        vertical_profiles.Fit( self.panel_right )
        self.splitter_main_vertical.SplitVertically( self.panel_left, self.panel_right, 470 )
        vertical_top.Add( self.splitter_main_vertical, 1, wx.EXPAND, 5 )


        self.panel_top.SetSizer( vertical_top )
        self.panel_top.Layout()
        vertical_top.Fit( self.panel_top )
        self.panel_bottom = wx.Panel( self.splitter_main_horizonzal, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        vertical_bottom = wx.BoxSizer( wx.VERTICAL )

        self.rich_log = wx.richtext.RichTextCtrl( self.panel_bottom, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.BORDER_SIMPLE|wx.VSCROLL|wx.WANTS_CHARS )
        vertical_bottom.Add( self.rich_log, 1, wx.EXPAND |wx.ALL, 5 )


        self.panel_bottom.SetSizer( vertical_bottom )
        self.panel_bottom.Layout()
        vertical_bottom.Fit( self.panel_bottom )
        self.splitter_main_horizonzal.SplitHorizontally( self.panel_top, self.panel_bottom, 470 )
        vertical_main.Add( self.splitter_main_horizonzal, 1, wx.EXPAND, 5 )


        horizontal_main.Add( vertical_main, 1, wx.EXPAND, 5 )


        self.SetSizer( horizontal_main )
        self.Layout()
        self.menubar_main = wx.MenuBar( 0 )
        self.menu_file = wx.Menu()
        self.menuItem_openProfileFolder = wx.MenuItem( self.menu_file, wx.ID_ANY, _(u"Open profile folder"), wx.EmptyString, wx.ITEM_NORMAL )
        self.menu_file.Append( self.menuItem_openProfileFolder )

        self.menuItem_installKernelModule = wx.MenuItem( self.menu_file, wx.ID_ANY, _(u"Install kernel module"), wx.EmptyString, wx.ITEM_NORMAL )
        self.menu_file.Append( self.menuItem_installKernelModule )

        self.menuItem_quit = wx.MenuItem( self.menu_file, wx.ID_ANY, _(u"Quit"), wx.EmptyString, wx.ITEM_NORMAL )
        self.menu_file.Append( self.menuItem_quit )

        self.menubar_main.Append( self.menu_file, _(u"File") )

        self.menu_options = wx.Menu()
        self.menuItem_tray = wx.MenuItem( self.menu_options, wx.ID_ANY, _(u"Show tray icon"), wx.EmptyString, wx.ITEM_CHECK )
        self.menu_options.Append( self.menuItem_tray )

        self.menuItem_startMinimized = wx.MenuItem( self.menu_options, wx.ID_ANY, _(u"Start minimized"), wx.EmptyString, wx.ITEM_CHECK )
        self.menu_options.Append( self.menuItem_startMinimized )

        self.menuItem_closeToTray = wx.MenuItem( self.menu_options, wx.ID_ANY, _(u"Close to tray"), wx.EmptyString, wx.ITEM_CHECK )
        self.menu_options.Append( self.menuItem_closeToTray )

        self.subMenu_trayIconStyle = wx.Menu()
        self.menu_options.AppendSubMenu( self.subMenu_trayIconStyle, _(u"Tray icon style") )

        self.menu_options.AppendSeparator()

        self.menuItem_applyStart = wx.MenuItem( self.menu_options, wx.ID_ANY, _(u"Apply [ACTIVE] on startup"), wx.EmptyString, wx.ITEM_CHECK )
        self.menu_options.Append( self.menuItem_applyStart )

        self.menuItem_extendSpeed = wx.MenuItem( self.menu_options, wx.ID_ANY, _(u"Extend max speed"), wx.EmptyString, wx.ITEM_CHECK )
        self.menu_options.Append( self.menuItem_extendSpeed )

        self.subMenu_language = wx.Menu()
        self.menu_options.AppendSubMenu( self.subMenu_language, _(u"Language") )

        self.menubar_main.Append( self.menu_options, _(u"Options") )

        self.menu_view = wx.Menu()
        self.menuItem_log = wx.MenuItem( self.menu_view, wx.ID_ANY, _(u"Show log"), wx.EmptyString, wx.ITEM_CHECK )
        self.menu_view.Append( self.menuItem_log )

        self.menuItem_profiles = wx.MenuItem( self.menu_view, wx.ID_ANY, _(u"Show profiles"), wx.EmptyString, wx.ITEM_CHECK )
        self.menu_view.Append( self.menuItem_profiles )

        self.menuItem_preview = wx.MenuItem( self.menu_view, wx.ID_ANY, _(u"Show preview"), wx.EmptyString, wx.ITEM_CHECK )
        self.menu_view.Append( self.menuItem_preview )

        self.menubar_main.Append( self.menu_view, _(u"View") )

        self.menu_about = wx.Menu()
        self.menuItem_about = wx.MenuItem( self.menu_about, wx.ID_ANY, _(u"About RGB Config (acer-gkbbl-0)"), wx.EmptyString, wx.ITEM_NORMAL )
        self.menu_about.Append( self.menuItem_about )

        self.menubar_main.Append( self.menu_about, _(u"About") )

        self.SetMenuBar( self.menubar_main )


        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_SHOW, self.on_show )
        self.choise_mode.Bind( wx.EVT_CHOICE, self.on_rgb_mode_select )
        self.radio_left_right.Bind( wx.EVT_RADIOBUTTON, self.on_direction_select )
        self.radio_right_left.Bind( wx.EVT_RADIOBUTTON, self.on_direction_select )
        self.button_save.Bind( wx.EVT_BUTTON, self.on_save_click )
        self.button_apply.Bind( wx.EVT_BUTTON, self.on_apply_click )
        self.button_refresh.Bind( wx.EVT_BUTTON, self.on_refresh_click )
        self.button_delete.Bind( wx.EVT_BUTTON, self.on_delete_click )
        self.button_load.Bind( wx.EVT_BUTTON, self.on_load_click )
        self.rich_log.Bind( wx.EVT_TEXT_URL, self.on_log_url_click )
        self.Bind( wx.EVT_MENU, self.on_menu_openProfileFolder, id = self.menuItem_openProfileFolder.GetId() )
        self.Bind( wx.EVT_MENU, self.on_menu_installKernelModule, id = self.menuItem_installKernelModule.GetId() )
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

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def on_show( self, event ):
        event.Skip()

    def on_rgb_mode_select( self, event ):
        event.Skip()

    def on_direction_select( self, event ):
        event.Skip()


    def on_save_click( self, event ):
        event.Skip()

    def on_apply_click( self, event ):
        event.Skip()

    def on_refresh_click( self, event ):
        event.Skip()

    def on_delete_click( self, event ):
        event.Skip()

    def on_load_click( self, event ):
        event.Skip()

    def on_log_url_click( self, event ):
        event.Skip()

    def on_menu_openProfileFolder( self, event ):
        event.Skip()

    def on_menu_installKernelModule( self, event ):
        event.Skip()

    def on_force_close( self, event ):
        event.Skip()

    def on_menu_tray( self, event ):
        event.Skip()

    def on_menu_startMinimized( self, event ):
        event.Skip()

    def on_menu_closeToTray( self, event ):
        event.Skip()

    def on_menu_applyStart( self, event ):
        event.Skip()

    def on_menu_extendSpeed( self, event ):
        event.Skip()

    def on_menu_log( self, event ):
        event.Skip()

    def on_menu_profiles( self, event ):
        event.Skip()

    def on_menu_preview( self, event ):
        event.Skip()

    def on_menu_about( self, event ):
        event.Skip()

    def splitter_main_horizonzalOnIdle( self, event ):
        self.splitter_main_horizonzal.SetSashPosition( 470 )
        self.splitter_main_horizonzal.Unbind( wx.EVT_IDLE )

    def splitter_main_verticalOnIdle( self, event ):
        self.splitter_main_vertical.SetSashPosition( 470 )
        self.splitter_main_vertical.Unbind( wx.EVT_IDLE )


###########################################################################
## Class dialog_about
###########################################################################

class dialog_about ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"About RGB Config (acer-gkbbl-0)"), pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        vertical_about = wx.BoxSizer( wx.VERTICAL )

        self.label_about_header = wx.StaticText( self, wx.ID_ANY, _(u"RGB Config (acer-gkbbl-0)"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.label_about_header.Wrap( -1 )

        self.label_about_header.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        vertical_about.Add( self.label_about_header, 0, wx.ALL|wx.EXPAND, 5 )

        self.label_about_license = wx.StaticText( self, wx.ID_ANY, _(u"MIT License\n\nCopyright 2022 x211321\n\nPermission is hereby granted, free of charge, to any person obtaining \na copy of this software and associated documentation files (the \"Software\"), \nto deal in the Software without restriction, including without limitation\nthe rights to use, copy, modify, merge, publish, distribute, sublicense,\n and/or sell copies of the Software, and to permit persons to whom the\nSoftware is furnished to do , subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included\n in all copies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND,\nEXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES \nOF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND \nNONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT\nHOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, \nWHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING\nFROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR \nOTHER DEALINGS IN THE SOFTWARE."), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.label_about_license.Wrap( -1 )

        vertical_about.Add( self.label_about_license, 0, wx.ALL|wx.EXPAND, 5 )

        self.hyperlink_about = wx.adv.HyperlinkCtrl( self, wx.ID_ANY, _(u"RGB Config (acer-gkbbl-0) on GitHub"), u"https://github.com/x211321/RGB-Config-Acer-gkbbl-0", wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE )
        vertical_about.Add( self.hyperlink_about, 0, wx.ALL|wx.EXPAND, 5 )

        self.button_about_close = wx.Button( self, wx.ID_ANY, _(u"Close"), wx.DefaultPosition, wx.DefaultSize, 0 )
        vertical_about.Add( self.button_about_close, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 15 )


        self.SetSizer( vertical_about )
        self.Layout()
        vertical_about.Fit( self )

        self.Centre( wx.BOTH )

        # Connect Events
        self.button_about_close.Bind( wx.EVT_BUTTON, self.on_button_about_close_click )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def on_button_about_close_click( self, event ):
        event.Skip()


###########################################################################
## Class dialog_install_module
###########################################################################

class dialog_install_module ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        flex_install_module = wx.FlexGridSizer( 2, 1, 0, 0 )
        flex_install_module.SetFlexibleDirection( wx.BOTH )
        flex_install_module.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.panel_install_module = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        vertical_install_module = wx.BoxSizer( wx.VERTICAL )

        horizontal_install_module_explanation = wx.BoxSizer( wx.HORIZONTAL )

        self.label_install_module_explanation = wx.StaticText( self.panel_install_module, wx.ID_ANY, _(u"RGB Config (acer-gkbbl-0) will perform the steps listed below."), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.label_install_module_explanation.Wrap( -1 )

        self.label_install_module_explanation.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        horizontal_install_module_explanation.Add( self.label_install_module_explanation, 0, wx.ALL|wx.EXPAND, 5 )


        vertical_install_module.Add( horizontal_install_module_explanation, 1, wx.EXPAND, 5 )

        self.line_install_module_step1_system_requirements = wx.StaticLine( self.panel_install_module, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        vertical_install_module.Add( self.line_install_module_step1_system_requirements, 0, wx.EXPAND |wx.ALL, 5 )

        horizontal_install_module_step1_system_requirements = wx.BoxSizer( wx.HORIZONTAL )

        self.label_install_module_step1_system_requirements = wx.StaticText( self.panel_install_module, wx.ID_ANY, _(u"Step 1 - Check system requirements"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.label_install_module_step1_system_requirements.Wrap( -1 )

        self.label_install_module_step1_system_requirements.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        horizontal_install_module_step1_system_requirements.Add( self.label_install_module_step1_system_requirements, 0, wx.ALL, 5 )


        horizontal_install_module_step1_system_requirements.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.label_install_module_step1_system_requirements_result = wx.StaticText( self.panel_install_module, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.label_install_module_step1_system_requirements_result.Wrap( -1 )

        self.label_install_module_step1_system_requirements_result.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        horizontal_install_module_step1_system_requirements.Add( self.label_install_module_step1_system_requirements_result, 0, wx.ALL|wx.EXPAND, 5 )


        vertical_install_module.Add( horizontal_install_module_step1_system_requirements, 1, wx.EXPAND, 5 )

        horizontal_install_module_step1_system_requirements_manufacturer = wx.BoxSizer( wx.HORIZONTAL )

        self.label_install_module_step1_system_requirements_manufacturer = wx.StaticText( self.panel_install_module, wx.ID_ANY, _(u"Manufacturer"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.label_install_module_step1_system_requirements_manufacturer.Wrap( -1 )

        self.label_install_module_step1_system_requirements_manufacturer.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        horizontal_install_module_step1_system_requirements_manufacturer.Add( self.label_install_module_step1_system_requirements_manufacturer, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 20 )


        horizontal_install_module_step1_system_requirements_manufacturer.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.label_install_module_step1_system_requirements_manufacturer_result = wx.StaticText( self.panel_install_module, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.label_install_module_step1_system_requirements_manufacturer_result.Wrap( -1 )

        self.label_install_module_step1_system_requirements_manufacturer_result.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        horizontal_install_module_step1_system_requirements_manufacturer.Add( self.label_install_module_step1_system_requirements_manufacturer_result, 0, wx.ALL|wx.EXPAND, 5 )


        vertical_install_module.Add( horizontal_install_module_step1_system_requirements_manufacturer, 1, wx.EXPAND, 5 )

        horizontal_install_module_step1_system_requirements_model = wx.BoxSizer( wx.HORIZONTAL )

        self.label_install_module_step1_system_requirements_model = wx.StaticText( self.panel_install_module, wx.ID_ANY, _(u"Device"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.label_install_module_step1_system_requirements_model.Wrap( -1 )

        self.label_install_module_step1_system_requirements_model.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        horizontal_install_module_step1_system_requirements_model.Add( self.label_install_module_step1_system_requirements_model, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 20 )


        horizontal_install_module_step1_system_requirements_model.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.label_install_module_step1_system_requirements_model_result = wx.StaticText( self.panel_install_module, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.label_install_module_step1_system_requirements_model_result.Wrap( -1 )

        self.label_install_module_step1_system_requirements_model_result.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        horizontal_install_module_step1_system_requirements_model.Add( self.label_install_module_step1_system_requirements_model_result, 0, wx.ALL|wx.EXPAND, 5 )


        vertical_install_module.Add( horizontal_install_module_step1_system_requirements_model, 1, wx.EXPAND, 5 )

        horizontal_install_module_step1_system_requirements_secureboot = wx.BoxSizer( wx.HORIZONTAL )

        self.label_install_module_step1_system_requirements_secureboot = wx.StaticText( self.panel_install_module, wx.ID_ANY, _(u"Secure boot"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.label_install_module_step1_system_requirements_secureboot.Wrap( -1 )

        self.label_install_module_step1_system_requirements_secureboot.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        horizontal_install_module_step1_system_requirements_secureboot.Add( self.label_install_module_step1_system_requirements_secureboot, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 20 )


        horizontal_install_module_step1_system_requirements_secureboot.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.label_install_module_step1_system_requirements_secureboot_result = wx.StaticText( self.panel_install_module, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.label_install_module_step1_system_requirements_secureboot_result.Wrap( -1 )

        self.label_install_module_step1_system_requirements_secureboot_result.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        horizontal_install_module_step1_system_requirements_secureboot.Add( self.label_install_module_step1_system_requirements_secureboot_result, 0, wx.ALL|wx.EXPAND, 5 )


        vertical_install_module.Add( horizontal_install_module_step1_system_requirements_secureboot, 1, wx.EXPAND, 5 )

        horizontal_install_module_step1_system_requirements_initsystem = wx.BoxSizer( wx.HORIZONTAL )

        self.label_install_module_step1_system_requirements_initsystem = wx.StaticText( self.panel_install_module, wx.ID_ANY, _(u"Init system"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.label_install_module_step1_system_requirements_initsystem.Wrap( -1 )

        self.label_install_module_step1_system_requirements_initsystem.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        horizontal_install_module_step1_system_requirements_initsystem.Add( self.label_install_module_step1_system_requirements_initsystem, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 20 )


        horizontal_install_module_step1_system_requirements_initsystem.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.label_install_module_step1_system_requirements_initsystem_result = wx.StaticText( self.panel_install_module, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.label_install_module_step1_system_requirements_initsystem_result.Wrap( -1 )

        self.label_install_module_step1_system_requirements_initsystem_result.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        horizontal_install_module_step1_system_requirements_initsystem.Add( self.label_install_module_step1_system_requirements_initsystem_result, 0, wx.ALL|wx.EXPAND, 5 )


        vertical_install_module.Add( horizontal_install_module_step1_system_requirements_initsystem, 1, wx.EXPAND, 5 )

        self.line_install_module_step2_download = wx.StaticLine( self.panel_install_module, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        vertical_install_module.Add( self.line_install_module_step2_download, 0, wx.EXPAND |wx.ALL, 5 )

        horizontal_install_module_step2_download = wx.BoxSizer( wx.HORIZONTAL )

        self.label_install_module_step2_download = wx.StaticText( self.panel_install_module, wx.ID_ANY, _(u"Step 2 - Download installation files"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.label_install_module_step2_download.Wrap( -1 )

        self.label_install_module_step2_download.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        horizontal_install_module_step2_download.Add( self.label_install_module_step2_download, 0, wx.ALL, 5 )


        horizontal_install_module_step2_download.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.label_install_module_step2_download_result = wx.StaticText( self.panel_install_module, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.label_install_module_step2_download_result.Wrap( -1 )

        self.label_install_module_step2_download_result.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        horizontal_install_module_step2_download.Add( self.label_install_module_step2_download_result, 0, wx.ALL|wx.EXPAND, 5 )


        vertical_install_module.Add( horizontal_install_module_step2_download, 1, wx.EXPAND, 5 )

        horizontal_install_module_step2_download_progress = wx.BoxSizer( wx.HORIZONTAL )

        self.hyperlink_install_module_step2_download_website = wx.adv.HyperlinkCtrl( self.panel_install_module, wx.ID_ANY, _(u"Kernel module Github"), wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE )
        horizontal_install_module_step2_download_progress.Add( self.hyperlink_install_module_step2_download_website, 0, wx.EXPAND|wx.LEFT, 20 )

        self.hyperlink_install_module_step2_download_url = wx.adv.HyperlinkCtrl( self.panel_install_module, wx.ID_ANY, _(u"[source]"), wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE )
        horizontal_install_module_step2_download_progress.Add( self.hyperlink_install_module_step2_download_url, 0, wx.ALL, 5 )


        horizontal_install_module_step2_download_progress.Add( ( 5, 0), 1, wx.EXPAND, 5 )

        self.label_install_module_step2_download_state = wx.StaticText( self.panel_install_module, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.label_install_module_step2_download_state.Wrap( -1 )

        self.label_install_module_step2_download_state.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        horizontal_install_module_step2_download_progress.Add( self.label_install_module_step2_download_state, 0, wx.ALL|wx.EXPAND, 5 )


        vertical_install_module.Add( horizontal_install_module_step2_download_progress, 1, wx.EXPAND, 5 )

        self.line_install_module_step3_extract = wx.StaticLine( self.panel_install_module, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        vertical_install_module.Add( self.line_install_module_step3_extract, 0, wx.EXPAND |wx.ALL, 5 )

        horizontal_install_module_step3_extract = wx.BoxSizer( wx.HORIZONTAL )

        self.label_install_module_step3_extract = wx.StaticText( self.panel_install_module, wx.ID_ANY, _(u"Step 3 - Extract installation files"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.label_install_module_step3_extract.Wrap( -1 )

        self.label_install_module_step3_extract.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        horizontal_install_module_step3_extract.Add( self.label_install_module_step3_extract, 0, wx.ALL, 5 )


        horizontal_install_module_step3_extract.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.label_install_module_step3_extract_result = wx.StaticText( self.panel_install_module, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.label_install_module_step3_extract_result.Wrap( -1 )

        self.label_install_module_step3_extract_result.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        horizontal_install_module_step3_extract.Add( self.label_install_module_step3_extract_result, 0, wx.ALL|wx.EXPAND, 5 )


        vertical_install_module.Add( horizontal_install_module_step3_extract, 1, wx.EXPAND, 5 )

        self.line_install_module_step4_install = wx.StaticLine( self.panel_install_module, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        vertical_install_module.Add( self.line_install_module_step4_install, 0, wx.EXPAND |wx.ALL, 5 )

        horizontal_install_module_step4_install = wx.BoxSizer( wx.HORIZONTAL )

        self.label_install_module_step4_install = wx.StaticText( self.panel_install_module, wx.ID_ANY, _(u"Step 4 - Run install script"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.label_install_module_step4_install.Wrap( -1 )

        self.label_install_module_step4_install.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        horizontal_install_module_step4_install.Add( self.label_install_module_step4_install, 0, wx.ALL, 5 )


        horizontal_install_module_step4_install.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.label_install_module_step4_install_result = wx.StaticText( self.panel_install_module, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.label_install_module_step4_install_result.Wrap( -1 )

        self.label_install_module_step4_install_result.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        horizontal_install_module_step4_install.Add( self.label_install_module_step4_install_result, 0, wx.ALL|wx.EXPAND, 5 )


        vertical_install_module.Add( horizontal_install_module_step4_install, 1, wx.EXPAND, 5 )

        self.line_install_module_step5_verify = wx.StaticLine( self.panel_install_module, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        vertical_install_module.Add( self.line_install_module_step5_verify, 0, wx.EXPAND |wx.ALL, 5 )

        horizontal_install_module_step5_verify = wx.BoxSizer( wx.HORIZONTAL )

        self.label_install_module_step5_verify = wx.StaticText( self.panel_install_module, wx.ID_ANY, _(u"Step 5 - Verify installation"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.label_install_module_step5_verify.Wrap( -1 )

        self.label_install_module_step5_verify.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        horizontal_install_module_step5_verify.Add( self.label_install_module_step5_verify, 0, wx.ALL, 5 )


        horizontal_install_module_step5_verify.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.label_install_module_step5_verify_result = wx.StaticText( self.panel_install_module, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.label_install_module_step5_verify_result.Wrap( -1 )

        self.label_install_module_step5_verify_result.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        horizontal_install_module_step5_verify.Add( self.label_install_module_step5_verify_result, 0, wx.ALL|wx.EXPAND, 5 )


        vertical_install_module.Add( horizontal_install_module_step5_verify, 1, wx.EXPAND, 5 )

        horizontal_install_module_step5_verify_rgb = wx.BoxSizer( wx.HORIZONTAL )

        self.label_install_module_step5_verify_rgb = wx.StaticText( self.panel_install_module, wx.ID_ANY, _(u"RGB device"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.label_install_module_step5_verify_rgb.Wrap( -1 )

        self.label_install_module_step5_verify_rgb.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        horizontal_install_module_step5_verify_rgb.Add( self.label_install_module_step5_verify_rgb, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 20 )


        horizontal_install_module_step5_verify_rgb.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.label_install_module_step5_verify_rgb_result = wx.StaticText( self.panel_install_module, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.label_install_module_step5_verify_rgb_result.Wrap( -1 )

        self.label_install_module_step5_verify_rgb_result.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        horizontal_install_module_step5_verify_rgb.Add( self.label_install_module_step5_verify_rgb_result, 0, wx.ALL|wx.EXPAND, 5 )


        vertical_install_module.Add( horizontal_install_module_step5_verify_rgb, 1, wx.EXPAND, 5 )

        horizontal_install_module_step5_verify_rgbstatic = wx.BoxSizer( wx.HORIZONTAL )

        self.label_install_module_step5_verify_rgbstatic = wx.StaticText( self.panel_install_module, wx.ID_ANY, _(u"Static RGB device"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.label_install_module_step5_verify_rgbstatic.Wrap( -1 )

        self.label_install_module_step5_verify_rgbstatic.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        horizontal_install_module_step5_verify_rgbstatic.Add( self.label_install_module_step5_verify_rgbstatic, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 20 )


        horizontal_install_module_step5_verify_rgbstatic.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.label_install_module_step5_verify_rgbstatic_result = wx.StaticText( self.panel_install_module, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.label_install_module_step5_verify_rgbstatic_result.Wrap( -1 )

        self.label_install_module_step5_verify_rgbstatic_result.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        horizontal_install_module_step5_verify_rgbstatic.Add( self.label_install_module_step5_verify_rgbstatic_result, 0, wx.ALL|wx.EXPAND, 5 )


        vertical_install_module.Add( horizontal_install_module_step5_verify_rgbstatic, 1, wx.EXPAND, 5 )


        self.panel_install_module.SetSizer( vertical_install_module )
        self.panel_install_module.Layout()
        vertical_install_module.Fit( self.panel_install_module )
        flex_install_module.Add( self.panel_install_module, 1, wx.EXPAND |wx.ALL, 10 )

        self.panel_install_module_buttons = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        horizontal_install_module_buttons = wx.BoxSizer( wx.HORIZONTAL )

        self.button_install_module_exit = wx.Button( self.panel_install_module_buttons, wx.ID_ANY, _(u"Exit"), wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
        horizontal_install_module_buttons.Add( self.button_install_module_exit, 0, wx.ALL, 15 )


        horizontal_install_module_buttons.Add( ( 100, 0), 1, wx.EXPAND, 5 )

        self.button_install_module_start = wx.Button( self.panel_install_module_buttons, wx.ID_ANY, _(u"Begin installation"), wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
        horizontal_install_module_buttons.Add( self.button_install_module_start, 0, wx.ALL, 15 )


        self.panel_install_module_buttons.SetSizer( horizontal_install_module_buttons )
        self.panel_install_module_buttons.Layout()
        horizontal_install_module_buttons.Fit( self.panel_install_module_buttons )
        flex_install_module.Add( self.panel_install_module_buttons, 1, wx.EXPAND |wx.ALL, 5 )


        self.SetSizer( flex_install_module )
        self.Layout()
        flex_install_module.Fit( self )

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.on_close )
        self.Bind( wx.EVT_SHOW, self.on_show )
        self.button_install_module_exit.Bind( wx.EVT_BUTTON, self.on_exit )
        self.button_install_module_start.Bind( wx.EVT_BUTTON, self.on_install )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def on_close( self, event ):
        event.Skip()

    def on_show( self, event ):
        event.Skip()

    def on_exit( self, event ):
        event.Skip()

    def on_install( self, event ):
        event.Skip()


