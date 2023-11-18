# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.0.0-0-g0efcecf-dirty)
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
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"RGB Config (acer-gkbbl-0)"), pos = wx.DefaultPosition, size = wx.Size( 900,550 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        horizontal_main = wx.BoxSizer( wx.HORIZONTAL )

        vertical_main = wx.BoxSizer( wx.VERTICAL )

        self.splitter_main_horizonzal = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D|wx.SP_LIVE_UPDATE|wx.SP_NOBORDER|wx.SP_THIN_SASH )
        self.splitter_main_horizonzal.SetSashGravity( 1 )
        self.splitter_main_horizonzal.Bind( wx.EVT_IDLE, self.splitter_main_horizonzalOnIdle )

        self.panel_top = wx.Panel( self.splitter_main_horizonzal, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        vertical_top = wx.BoxSizer( wx.VERTICAL )

        self.splitter_main_vertical = wx.SplitterWindow( self.panel_top, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_LIVE_UPDATE|wx.SP_NOBORDER|wx.SP_THIN_SASH )
        self.splitter_main_vertical.SetSashGravity( 1 )
        self.splitter_main_vertical.Bind( wx.EVT_IDLE, self.splitter_main_verticalOnIdle )

        self.panel_left = wx.Panel( self.splitter_main_vertical, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        vertical_settings = wx.BoxSizer( wx.VERTICAL )


        vertical_settings.Add( ( 0, 10), 0, wx.EXPAND, 5 )

        self.label_settings = wx.StaticText( self.panel_left, wx.ID_ANY, _(u"Settings"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.label_settings.Wrap( -1 )

        self.label_settings.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        vertical_settings.Add( self.label_settings, 0, wx.EXPAND|wx.LEFT|wx.TOP, 5 )

        self.m_staticline1 = wx.StaticLine( self.panel_left, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        vertical_settings.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

        horizontal_mode = wx.BoxSizer( wx.HORIZONTAL )

        horizontal_mode.SetMinSize( wx.Size( -1,50 ) )
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

        horizontal_brightness.SetMinSize( wx.Size( -1,50 ) )
        self.label_brightness = wx.StaticText( self.panel_left, wx.ID_ANY, _(u"Brightness"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.label_brightness.Wrap( -1 )

        horizontal_brightness.Add( self.label_brightness, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.slider_brightness = wx.Slider( self.panel_left, wx.ID_ANY, 100, 0, 100, wx.DefaultPosition, wx.Size( -1,-1 ), wx.SL_HORIZONTAL|wx.SL_VALUE_LABEL )
        horizontal_brightness.Add( self.slider_brightness, 2, wx.ALL|wx.EXPAND, 5 )


        vertical_settings.Add( horizontal_brightness, 0, wx.EXPAND, 5 )

        horizontal_speed = wx.BoxSizer( wx.HORIZONTAL )

        horizontal_speed.SetMinSize( wx.Size( -1,50 ) )
        self.label_speed = wx.StaticText( self.panel_left, wx.ID_ANY, _(u"Speed"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.label_speed.Wrap( -1 )

        horizontal_speed.Add( self.label_speed, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.slider_speed = wx.Slider( self.panel_left, wx.ID_ANY, 3, 0, 9, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL|wx.SL_VALUE_LABEL )
        horizontal_speed.Add( self.slider_speed, 2, wx.ALL|wx.EXPAND, 5 )


        vertical_settings.Add( horizontal_speed, 0, wx.EXPAND, 5 )

        horizontal_direction = wx.BoxSizer( wx.HORIZONTAL )

        horizontal_direction.SetMinSize( wx.Size( -1,50 ) )
        self.label_direction = wx.StaticText( self.panel_left, wx.ID_ANY, _(u"Direction"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.label_direction.Wrap( -1 )

        horizontal_direction.Add( self.label_direction, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.radio_left_right = wx.RadioButton( self.panel_left, wx.ID_ANY, _(u"Left to Right"), wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
        horizontal_direction.Add( self.radio_left_right, 1, wx.ALL|wx.EXPAND, 5 )

        self.radio_right_left = wx.RadioButton( self.panel_left, wx.ID_ANY, _(u"Right to Left"), wx.DefaultPosition, wx.DefaultSize, 0 )
        horizontal_direction.Add( self.radio_right_left, 1, wx.ALL|wx.EXPAND, 5 )


        vertical_settings.Add( horizontal_direction, 0, wx.EXPAND, 5 )

        horizontal_colors = wx.BoxSizer( wx.HORIZONTAL )

        horizontal_colors.SetMinSize( wx.Size( -1,50 ) )
        self.label_colors = wx.StaticText( self.panel_left, wx.ID_ANY, _(u"Colors"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.label_colors.Wrap( -1 )

        horizontal_colors.Add( self.label_colors, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        horizontal_color_sections = wx.BoxSizer( wx.HORIZONTAL )

        self.color_color0 = wx.ColourPickerCtrl( self.panel_left, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
        self.color_color0.SetMaxSize( wx.Size( 80,-1 ) )

        horizontal_color_sections.Add( self.color_color0, 2, wx.ALL|wx.EXPAND, 5 )

        self.color_color1 = wx.ColourPickerCtrl( self.panel_left, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
        self.color_color1.SetMaxSize( wx.Size( 80,-1 ) )

        horizontal_color_sections.Add( self.color_color1, 2, wx.ALL|wx.EXPAND, 5 )

        self.color_color2 = wx.ColourPickerCtrl( self.panel_left, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
        self.color_color2.SetMaxSize( wx.Size( 80,-1 ) )

        horizontal_color_sections.Add( self.color_color2, 2, wx.ALL|wx.EXPAND, 5 )

        self.color_color3 = wx.ColourPickerCtrl( self.panel_left, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
        self.color_color3.SetMaxSize( wx.Size( 80,-1 ) )

        horizontal_color_sections.Add( self.color_color3, 2, wx.ALL|wx.EXPAND, 5 )


        horizontal_colors.Add( horizontal_color_sections, 2, wx.EXPAND, 5 )


        vertical_settings.Add( horizontal_colors, 0, wx.EXPAND, 5 )

        horizontal_spacer = wx.BoxSizer( wx.VERTICAL )


        horizontal_spacer.Add( ( 0, 10), 1, wx.EXPAND, 5 )


        vertical_settings.Add( horizontal_spacer, 1, wx.EXPAND, 5 )

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

        self.label_profiles.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        vertical_profiles.Add( self.label_profiles, 0, wx.EXPAND|wx.LEFT|wx.TOP, 5 )

        self.m_staticline2 = wx.StaticLine( self.panel_right, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        vertical_profiles.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )

        list_profilesChoices = []
        self.list_profiles = wx.ListBox( self.panel_right, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, list_profilesChoices, wx.LB_SINGLE|wx.LB_SORT )
        vertical_profiles.Add( self.list_profiles, 1, wx.ALL|wx.EXPAND, 5 )


        vertical_profiles.Add( ( 0, 4), 0, wx.EXPAND, 5 )

        horizontal_profile_buttons = wx.BoxSizer( wx.HORIZONTAL )

        self.button_refresh = wx.Button( self.panel_right, wx.ID_ANY, _(u"Refresh"), wx.DefaultPosition, wx.DefaultSize, 0 )
        horizontal_profile_buttons.Add( self.button_refresh, 0, wx.ALL, 10 )

        self.button_delete = wx.Button( self.panel_right, wx.ID_ANY, _(u"Delete"), wx.DefaultPosition, wx.DefaultSize, 0 )
        horizontal_profile_buttons.Add( self.button_delete, 0, wx.ALL, 10 )


        horizontal_profile_buttons.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.button_load = wx.Button( self.panel_right, wx.ID_ANY, _(u"Load"), wx.DefaultPosition, wx.DefaultSize, 0 )
        horizontal_profile_buttons.Add( self.button_load, 1, wx.ALL, 10 )


        vertical_profiles.Add( horizontal_profile_buttons, 0, wx.EXPAND, 5 )


        self.panel_right.SetSizer( vertical_profiles )
        self.panel_right.Layout()
        vertical_profiles.Fit( self.panel_right )
        self.splitter_main_vertical.SplitVertically( self.panel_left, self.panel_right, 580 )
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
        self.splitter_main_horizonzal.SplitHorizontally( self.panel_top, self.panel_bottom, 400 )
        vertical_main.Add( self.splitter_main_horizonzal, 1, wx.EXPAND, 5 )


        horizontal_main.Add( vertical_main, 1, wx.EXPAND, 5 )


        self.SetSizer( horizontal_main )
        self.Layout()
        self.status_status = self.CreateStatusBar( 1, wx.STB_SIZEGRIP|wx.BORDER_THEME, wx.ID_ANY )
        self.menubar_main = wx.MenuBar( 0 )
        self.menu_file = wx.Menu()
        self.menuItem_openProfileFolder = wx.MenuItem( self.menu_file, wx.ID_ANY, _(u"Open profile folder"), wx.EmptyString, wx.ITEM_NORMAL )
        self.menu_file.Append( self.menuItem_openProfileFolder )

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
        self.Bind( wx.EVT_CLOSE, self.on_close )
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
    def on_close( self, event ):
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
        self.splitter_main_horizonzal.SetSashPosition( 400 )
        self.splitter_main_horizonzal.Unbind( wx.EVT_IDLE )

    def splitter_main_verticalOnIdle( self, event ):
        self.splitter_main_vertical.SetSashPosition( 580 )
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

        self.label_about_header.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

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


