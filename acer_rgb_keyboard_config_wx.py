# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv
import wx.richtext

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"RGB Config (acer-gkbbl-0)", pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

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

        self.label_settings = wx.StaticText( self.panel_left, wx.ID_ANY, u"Settings", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.label_settings.Wrap( -1 )

        self.label_settings.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        vertical_settings.Add( self.label_settings, 0, wx.EXPAND|wx.LEFT|wx.TOP, 5 )

        self.m_staticline1 = wx.StaticLine( self.panel_left, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        vertical_settings.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

        horizontal_mode = wx.BoxSizer( wx.HORIZONTAL )

        self.label_mode = wx.StaticText( self.panel_left, wx.ID_ANY, u"RGB Mode", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_LEFT )
        self.label_mode.Wrap( -1 )

        horizontal_mode.Add( self.label_mode, 2, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        choise_modeChoices = [ u"Static", u"Breath", u"Neon", u"Wave", u"Shifting", u"Zoom" ]
        self.choise_mode = wx.Choice( self.panel_left, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choise_modeChoices, 0 )
        self.choise_mode.SetSelection( 0 )
        horizontal_mode.Add( self.choise_mode, 3, wx.ALL|wx.EXPAND, 5 )

        self.animation_preview = wx.adv.AnimationCtrl( self.panel_left, wx.ID_ANY, wx.adv.NullAnimation, wx.DefaultPosition, wx.Size( 60,40 ), wx.adv.AC_DEFAULT_STYLE|wx.adv.AC_NO_AUTORESIZE )
        horizontal_mode.Add( self.animation_preview, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )


        vertical_settings.Add( horizontal_mode, 0, wx.EXPAND, 5 )

        horizontal_brightness = wx.BoxSizer( wx.HORIZONTAL )

        self.label_brightness = wx.StaticText( self.panel_left, wx.ID_ANY, u"Brightness", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.label_brightness.Wrap( -1 )

        horizontal_brightness.Add( self.label_brightness, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.slider_brightness = wx.Slider( self.panel_left, wx.ID_ANY, 100, 0, 100, wx.DefaultPosition, wx.Size( -1,-1 ), wx.SL_HORIZONTAL|wx.SL_VALUE_LABEL )
        horizontal_brightness.Add( self.slider_brightness, 2, wx.ALL|wx.EXPAND, 5 )


        vertical_settings.Add( horizontal_brightness, 0, wx.EXPAND, 5 )

        horizontal_speed = wx.BoxSizer( wx.HORIZONTAL )

        self.label_speed = wx.StaticText( self.panel_left, wx.ID_ANY, u"Speed", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.label_speed.Wrap( -1 )

        horizontal_speed.Add( self.label_speed, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.slider_speed = wx.Slider( self.panel_left, wx.ID_ANY, 3, 0, 9, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL|wx.SL_VALUE_LABEL )
        horizontal_speed.Add( self.slider_speed, 2, wx.ALL|wx.EXPAND, 5 )


        vertical_settings.Add( horizontal_speed, 0, wx.EXPAND, 5 )

        horizontal_direction = wx.BoxSizer( wx.HORIZONTAL )

        self.label_direction = wx.StaticText( self.panel_left, wx.ID_ANY, u"Direction", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.label_direction.Wrap( -1 )

        horizontal_direction.Add( self.label_direction, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )

        self.radio_left_right = wx.RadioButton( self.panel_left, wx.ID_ANY, u"Left to Right", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
        horizontal_direction.Add( self.radio_left_right, 1, wx.ALL|wx.EXPAND, 5 )

        self.radio_right_left = wx.RadioButton( self.panel_left, wx.ID_ANY, u"Right to Left", wx.DefaultPosition, wx.DefaultSize, 0 )
        horizontal_direction.Add( self.radio_right_left, 1, wx.ALL|wx.EXPAND, 5 )


        vertical_settings.Add( horizontal_direction, 0, wx.EXPAND, 5 )

        horizontal_color1 = wx.BoxSizer( wx.HORIZONTAL )

        self.label_color0 = wx.StaticText( self.panel_left, wx.ID_ANY, u"Color section 1", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.label_color0.Wrap( -1 )

        horizontal_color1.Add( self.label_color0, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.color_color0 = wx.ColourPickerCtrl( self.panel_left, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
        horizontal_color1.Add( self.color_color0, 2, wx.ALL|wx.EXPAND, 5 )


        vertical_settings.Add( horizontal_color1, 0, wx.EXPAND, 5 )

        horizontal_color2 = wx.BoxSizer( wx.HORIZONTAL )

        self.label_color1 = wx.StaticText( self.panel_left, wx.ID_ANY, u"Color section 2", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.label_color1.Wrap( -1 )

        horizontal_color2.Add( self.label_color1, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.color_color1 = wx.ColourPickerCtrl( self.panel_left, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
        horizontal_color2.Add( self.color_color1, 2, wx.ALL|wx.EXPAND, 5 )


        vertical_settings.Add( horizontal_color2, 0, wx.EXPAND, 5 )

        horizontal_color3 = wx.BoxSizer( wx.HORIZONTAL )

        self.label_color2 = wx.StaticText( self.panel_left, wx.ID_ANY, u"Color section 3", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.label_color2.Wrap( -1 )

        horizontal_color3.Add( self.label_color2, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.color_color2 = wx.ColourPickerCtrl( self.panel_left, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
        horizontal_color3.Add( self.color_color2, 2, wx.ALL|wx.EXPAND, 5 )


        vertical_settings.Add( horizontal_color3, 0, wx.EXPAND, 5 )

        horizontal_color4 = wx.BoxSizer( wx.HORIZONTAL )

        self.label_color3 = wx.StaticText( self.panel_left, wx.ID_ANY, u"Color section 4", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.label_color3.Wrap( -1 )

        horizontal_color4.Add( self.label_color3, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.color_color3 = wx.ColourPickerCtrl( self.panel_left, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
        horizontal_color4.Add( self.color_color3, 2, wx.ALL|wx.EXPAND, 5 )


        vertical_settings.Add( horizontal_color4, 0, wx.EXPAND, 5 )


        vertical_settings.Add( ( 0, 10), 1, wx.EXPAND, 5 )

        grid_settings_buttons = wx.GridSizer( 0, 2, 0, 0 )

        self.button_save = wx.Button( self.panel_left, wx.ID_ANY, u"Save as profile", wx.DefaultPosition, wx.DefaultSize, 0 )
        grid_settings_buttons.Add( self.button_save, 0, wx.ALIGN_LEFT|wx.ALL, 10 )

        self.button_apply = wx.Button( self.panel_left, wx.ID_ANY, u"Apply", wx.DefaultPosition, wx.DefaultSize, 0 )
        grid_settings_buttons.Add( self.button_apply, 0, wx.ALIGN_RIGHT|wx.ALL, 10 )


        vertical_settings.Add( grid_settings_buttons, 0, wx.EXPAND, 5 )


        self.panel_left.SetSizer( vertical_settings )
        self.panel_left.Layout()
        vertical_settings.Fit( self.panel_left )
        self.pane_right = wx.Panel( self.splitter_main_vertical, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        vertical_profiles = wx.BoxSizer( wx.VERTICAL )


        vertical_profiles.Add( ( 0, 10), 0, wx.EXPAND, 5 )

        self.label_profiles = wx.StaticText( self.pane_right, wx.ID_ANY, u"Profiles", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.label_profiles.Wrap( -1 )

        self.label_profiles.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        vertical_profiles.Add( self.label_profiles, 0, wx.EXPAND|wx.LEFT|wx.TOP, 5 )

        self.m_staticline2 = wx.StaticLine( self.pane_right, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        vertical_profiles.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )

        list_profilesChoices = []
        self.list_profiles = wx.ListBox( self.pane_right, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, list_profilesChoices, wx.LB_SINGLE|wx.LB_SORT )
        vertical_profiles.Add( self.list_profiles, 1, wx.ALL|wx.EXPAND, 5 )


        vertical_profiles.Add( ( 0, 4), 0, wx.EXPAND, 5 )

        grid_profile_buttons = wx.GridSizer( 0, 3, 0, 0 )

        self.button_refresh = wx.Button( self.pane_right, wx.ID_ANY, u"Refresh", wx.DefaultPosition, wx.DefaultSize, 0 )
        grid_profile_buttons.Add( self.button_refresh, 0, wx.ALIGN_LEFT|wx.ALL, 10 )

        self.button_delete = wx.Button( self.pane_right, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
        grid_profile_buttons.Add( self.button_delete, 0, wx.ALIGN_CENTER|wx.ALL, 10 )

        self.button_load = wx.Button( self.pane_right, wx.ID_ANY, u"Load", wx.DefaultPosition, wx.DefaultSize, 0 )
        grid_profile_buttons.Add( self.button_load, 0, wx.ALIGN_RIGHT|wx.ALL, 10 )


        vertical_profiles.Add( grid_profile_buttons, 0, wx.EXPAND, 5 )


        self.pane_right.SetSizer( vertical_profiles )
        self.pane_right.Layout()
        vertical_profiles.Fit( self.pane_right )
        self.splitter_main_vertical.SplitVertically( self.panel_left, self.pane_right, 500 )
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
        self.splitter_main_horizonzal.SplitHorizontally( self.panel_top, self.panel_bottom, 460 )
        vertical_main.Add( self.splitter_main_horizonzal, 1, wx.EXPAND, 5 )


        horizontal_main.Add( vertical_main, 1, wx.EXPAND, 5 )


        self.SetSizer( horizontal_main )
        self.Layout()
        self.status_status = self.CreateStatusBar( 1, wx.STB_SIZEGRIP|wx.BORDER_THEME, wx.ID_ANY )

        self.Centre( wx.BOTH )

        # Connect Events
        self.choise_mode.Bind( wx.EVT_CHOICE, self.on_rgb_mode_select )
        self.radio_left_right.Bind( wx.EVT_RADIOBUTTON, self.on_direction_select )
        self.radio_right_left.Bind( wx.EVT_RADIOBUTTON, self.on_direction_select )
        self.button_save.Bind( wx.EVT_BUTTON, self.on_save_click )
        self.button_apply.Bind( wx.EVT_BUTTON, self.on_apply_click )
        self.button_refresh.Bind( wx.EVT_BUTTON, self.on_refresh_click )
        self.button_delete.Bind( wx.EVT_BUTTON, self.on_delete_click )
        self.button_load.Bind( wx.EVT_BUTTON, self.on_load_click )
        self.rich_log.Bind( wx.EVT_TEXT_URL, self.on_log_url_click )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
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

    def splitter_main_horizonzalOnIdle( self, event ):
        self.splitter_main_horizonzal.SetSashPosition( 460 )
        self.splitter_main_horizonzal.Unbind( wx.EVT_IDLE )

    def splitter_main_verticalOnIdle( self, event ):
        self.splitter_main_vertical.SetSashPosition( 500 )
        self.splitter_main_vertical.Unbind( wx.EVT_IDLE )


