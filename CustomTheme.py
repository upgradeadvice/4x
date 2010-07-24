#####################################################################
# -*- coding: utf-8 -*-                                             #
#                                                                   #
# Frets on Fire X (FoFiX)                                           #
# Copyright (C) 2006 Sami Kyöstilä                                  #
#               2008 myfingershurt                                  #
#               2008 Blazingamer                                    #
#               2008 evilynux <evilynux@gmail.com>                  #
#                                                                   #
# This program is free software; you can redistribute it and/or     #
# modify it under the terms of the GNU General Public License       #
# as published by the Free Software Foundation; either version 2    #
# of the License, or (at your option) any later version.            #
#                                                                   #
# This program is distributed in the hope that it will be useful,   #
# but WITHOUT ANY WARRANTY; without even the implied warranty of    #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the     #
# GNU General Public License for more details.                      #
#                                                                   #
# You should have received a copy of the GNU General Public License #
# along with this program; if not, write to the Free Software       #
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,        #
# MA  02110-1301, USA.                                              #
#####################################################################

__author__ = "fuzion"
__date__ = "$Jul 23, 2010 11:41:05 AM$"

from Theme import Theme

class CustomTheme(Theme):
  
    def __init__(self, path, name):
        self.name = name
        self.path = path
        Theme.__init__(self, path, name)
        artist_selected_color            = "#4080FF"
        artist_text_color                = "#4080FF"
        background_color                 = "#000000"
        bars_color                       = "#FFFF80"
        base_color                       = "#0066D6"
        career_title_color               = "#000000"
        character_create_font_color      = "#0066D6"
        character_create_help_color      = "#0066D6"
        character_create_select_color    = "#1DCBEA"
        fail_completed_color             = "#0066D6"
        fail_selected_color              = "#1DCBEA"
        fail_text_color                  = "#0066D6"
        fretK_color                      = "#000000"
        fretS_color                      = "#4CB2E5"
        hopo_color                       = "#00AAAA"
        hopo_indicator_active_color      = "#0066D6"
        hopo_indicator_inactive_color    = "#666666"
        ingame_stats_color               = "#0066D6"
        key2_color                       = "#000000"
        key_color                        = "#333333"
        library_selected_color           = "#1DCBEA"
        library_text_color               = "#0066D6"
        loading_text_color               = "#0066D6"
        mesh_color                       = "#000000"
        opt_selected_color               = "#1DCBEA"
        opt_text_color                   = "#0066D6"
        pause_selected_color             = "#1DCBEA"
        pause_text_color                 = "#0066D6"
        result_cheats_color              = "#0066D6"
        rockmeter_score_color            = "#0066D6"
        selected_color                   = "#1DCBEA"
        songlistcd_score_color           = "#0066D6"
        songlist_score_color             = "#93C351"
        song_name_selected_color         = "#1DCBEA"
        song_name_text_color             = "#0066D6"
        song_rb2_diff_color              = "#1DCBEA"
        spot_color                       = "#0066D6"
        star_fillup_color                = "#0066D6"
        tracks_color                     = "#FFFF80"
        vocal_fillup_color               = "#DFDFDE"
        vocal_glow_color                 = "#33FF00"
        vocal_glow_color_star            = "#FFFF00"
        vocal_lane_color                 = "#99FF80"
        vocal_lane_color_star            = "#FFFF80"
        vocal_shadow_color               = "#CCFFBF"
        vocal_shadow_color_star          = "#FFFFBF"

        avatar_select_font               = "font"
        character_create_help_font       = "loadingFont"
        character_create_option_font     = "font"
        control_activate_font            = "font"
        control_check_font               = "font"
        control_description_font         = "font"
        loading_font_scale               = 0.0015
        menu_tip_text_font               = "font"
        result_cheats_font               = "font"
        result_high_score_font           = "font"
        lobby_select_font                = "font"
        lobby_title_font                 = "loadingFont"

        avatar_select_avatar_x           = .667
        avatar_select_avatar_y           = .5
        avatar_select_text_scale         = .0027
        avatar_select_text_x             = .44
        avatar_select_text_y             = .16
        avatar_select_wheel_y            = 0.0
        character_create_help_scale      = 0.0018
        character_create_help_x          = 0.5
        character_create_help_y          = 0.73
        character_create_option_x        = 0.75
        character_create_scale           = .0018
        character_create_space           = .045
        character_create_x               = 0.25
        character_create_y               = 0.15
        control_activate_part_size       = 22.000
        control_activate_part_x          = 0.41
        control_activate_scale           = 0.0018
        control_activate_select_x        = 0.5
        control_activate_space           = 0.045
        control_activate_x               = 0.645
        control_activate_y               = 0.18
        control_check_part_mult          = 2.8
        control_check_scale              = 0.0018
        control_check_space              = 0.23
        control_check_text_y             = 0.61
        control_check_x                  = 0.16
        control_check_y                  = 0.26
        control_description_scale        = 0.002
        control_description_x            = 0.5
        control_description_y            = 0.13
        crowd_loop_delay                 = None
        display_all_grey_stars           = True
        fail_bkg                         = [0.5,0.5,1.0,1.0]
        fail_songname_x                  = 0.5
        fail_songname_y                  = 0.35
        fail_text_x                      = None
        fail_text_y                      = None
        fret_press                       = True
        glow_color                       = "fret"
        hopo_indicator_x                 = None
        hopo_indicator_y                 = None
        jurgen_text_pos                  = [1,1,.00035]
        loading_line_spacing             = 1.0
        loading_right_margin             = 1.0
        loading_x                        = 0.5
        loading_y                        = 0.6
        main_menu_scale                  = None
        main_menu_vspacing               = 0.05
        mark_solo_sections               = 2
        menu_neck_choose_x               = 0.1
        menu_neck_choose_y               = 0.05
        menu_tip_text_color              = None
        menu_tip_text_display            = False
        menu_tip_text_scale              = .002
        menu_tip_text_scroll_mode        = 0
        menu_tip_text_scroll_space       = .25
        menu_tip_text_y                  = .7
        menu_x                           = .5
        menu_y                           = .5
        neck_length                      = 9.0
        neck_width                       = 3.0
        obar_3dfill                      = False
        obar_hscale                      = 0.7
        opt_bkg                          = [0.5,0.5,1.0,1.0]
        opt_text_x                       = None
        opt_text_y                       = None
        pause_bkg                        = [0.5,0.5,1.0,1.0]
        pause_text_x                     = None
        pause_text_y                     = None
        pov_origin_x                     = None
        pov_origin_y                     = None
        pov_origin_z                     = None
        pov_target_x                     = None
        pov_target_y                     = None
        pov_target_z                     = None
        power_up_name                    = None
        rbmenu                           = True
        result_cheats_info               = [.5,.3,.002]
        result_cheats_numbers            = [.5,.35,.0015]
        result_cheats_percent            = [.45,.4,.0015]
        result_cheats_score              = [.75,.4,.0015]
        result_menu_x                    = .5
        result_menu_y                    = .2
        result_score                     = [.5,.11,0.0025,None,None]
        result_song                      = [.05,.045,.002,None,None]
        result_song_form                 = 0
        result_song_text                 = "%s Finished!"
        result_star                      = [.5,.4,0.15,1.1]
        result_star_type                 = 0
        result_stats_accuracy            = [.5,.61,0.002,None,None]
        result_stats_accuracy_text       = "Accuracy: %.1f%%"
        result_stats_diff                = [.5,.55,0.002,None,None]
        result_stats_diff_text           = "Difficulty: %s"
        result_stats_name                = [.5,.73,0.002,None,None]
        result_stats_notes               = [.5,.52,0.002,None,None]
        result_stats_notes_text          = "%s Notes Hit"
        result_stats_part                = [.5,.64,0.002,None,None]
        result_stats_part_text           = "Part: %s"
        result_stats_streak              = [.5,.58,0.002,None,None]
        result_stats_streak_text         = "Long Streak: %s"
        setlistguidebuttonsposX          = 0.408
        setlistguidebuttonsposY          = 0.0322
        setlistguidebuttonsscaleX        = 0.29
        setlistguidebuttonsscaleY        = 0.308
        setlistpreviewbuttonposX         = 0.5
        setlistpreviewbuttonposY         = 0.5
        setlistpreviewbuttonscaleX       = 0.5
        setlistpreviewbuttonscaleY       = 0.5
        shadowoffsetx                    = 0.0
        shadowoffsety                    = 0.0
        small_1x_mult                    = True
        song_cdscore_x                   = 0.6
        song_cd_x                        = 0.0
        song_info_display_scale          = 0.0020
        song_info_display_X              = 0.05
        song_info_display_Y              = 0.05
        song_listcd_cd_x                 = .75
        song_listcd_cd_y                 = .6
        song_listcd_list_x               = .1
        song_listcd_score_x              = .6
        song_listcd_score_y              = .5
        song_listscore_x                 = 0.8
        song_list_display                = None
        song_list_x                      = 0.15
        song_select_submenu_offset_lines = 2
        song_select_submenu_offset_spaces= 2
        song_select_submenu_x            = 0.100
        song_select_submenu_y            = 0.075
        star_fillup_center_x             = None
        star_fillup_center_y             = None
        star_fillup_in_radius            = None
        star_fillup_out_radius           = None
        threeDspin                       = True
        twoDkeys                         = False
        twoDnote                         = False
        use_fret_colors                  = False
        use_solo_submenu                 = None
        versiontag                       = False
        versiontagposX                   = 0.5
        versiontagposY                   = 0.5
        vocal_circular_fillup            = True
        vocal_fillup_center_x            = 139
        vocal_fillup_center_y            = 151
        vocal_fillup_factor              = 300.000
        vocal_fillup_in_radius           = 25
        vocal_fillup_out_radius          = 139
        vocal_glow_fade                  = .6
        vocal_glow_size                  = .012
        vocal_lane_size                  = .002
        vocal_meter_size                 = 45.000
        vocal_meter_x                    = .25
        vocal_meter_y                    = .8
        vocal_mult_x                     = .28
        vocal_mult_y                     = .8
        vocal_power_x                    = .5
        vocal_power_y                    = .8
        #Colors
        self.backgroundColor              = self.hexToColor(background_color)  
        self.baseColor                    = self.hexToColor(base_color)
        self.selectedColor                = self.hexToColor(selected_color)
        self.meshColor                    = self.hexToColor(mesh_color)
        self.hopoColor                    = self.hexToColor(hopo_color)
        self.spotColor                    = self.hexToColor(spot_color)
        self.keyColor                     = self.hexToColor(key_color)
        self.key2Color                    = self.hexToColor(key2_color)
        self.tracksColor                  = self.hexToColor(tracks_color)
        self.barsColor                    = self.hexToColor(bars_color)
        self.glowColor                    = self.hexToColor(glow_color)
        self.spNoteColor                  = self.hexToColor(fretS_color)
        self.killNoteColor                = self.hexToColor(fretK_color)
        self.songlist_score_colorVar      = self.hexToColor(songlist_score_color)
        self.songlistcd_score_colorVar    = self.hexToColor(songlistcd_score_color)
        self.career_title_colorVar        = self.hexToColor(career_title_color)
        self.opt_text_colorVar            = self.hexToColor(opt_text_color)
        self.opt_selected_colorVar        = self.hexToColor(opt_selected_color)
        self.song_name_text_colorVar      = self.hexToColor(song_name_text_color)
        self.song_name_selected_colorVar  = self.hexToColor(song_name_selected_color)
        self.artist_text_colorVar         = self.hexToColor(artist_text_color)
        self.artist_selected_colorVar     = self.hexToColor(artist_selected_color)
        self.library_text_colorVar        = self.hexToColor(library_text_color)
        self.library_selected_colorVar    = self.hexToColor(library_selected_color)
        self.pause_text_colorVar          = self.hexToColor(pause_text_color)
        self.pause_selected_colorVar      = self.hexToColor(pause_selected_color)
        self.fail_completed_colorVar      = self.hexToColor(fail_completed_color)
        self.fail_text_colorVar           = self.hexToColor(fail_text_color)
        self.fail_selected_colorVar       = self.hexToColor(fail_selected_color)
        self.song_rb2_diff_colorVar       = self.hexToColor(song_rb2_diff_color)
        self.loadingColor                 = self.hexToColor(loading_text_color)
        self.menuTipTextColor             = self.hexToColorResults(menu_tip_text_color)
        self.characterCreateFontColor     = self.hexToColor(character_create_font_color)
        self.characterCreateSelectColor   = self.hexToColor(character_create_select_color)
        self.characterCreateHelpColor     = self.hexToColor(character_create_help_color)
        self.vocalLaneColor               = self.hexToColorResults(vocal_lane_color)
        self.vocalShadowColor             = self.hexToColorResults(vocal_shadow_color)
        self.vocalGlowColor               = self.hexToColorResults(vocal_glow_color)
        self.vocalLaneColorStar           = self.hexToColorResults(vocal_lane_color_star)
        self.vocalShadowColorStar         = self.hexToColorResults(vocal_shadow_color_star)
        self.vocalGlowColorStar           = self.hexToColorResults(vocal_glow_color_star)
        self.rockmeter_score_colorVar     = self.hexToColorResults(rockmeter_score_color)
        self.ingame_stats_colorVar        = self.hexToColorResults(ingame_stats_color)
        self.hopoIndicatorActiveColor     = self.hexToColor(hopo_indicator_active_color)
        self.hopoIndicatorInactiveColor   = self.hexToColor(hopo_indicator_inactive_color)
		
        #Note Colors (this applies to frets and notes)
        self.use_fret_colors              = use_fret_colors

        #Point of View
        self.povTargetX                   = pov_target_x  
        self.povTargetY                   = pov_target_y
        self.povTargetZ                   = pov_target_z
        self.povOriginX                   = pov_origin_x
        self.povOriginY                   = pov_origin_y
        self.povOriginZ                   = pov_origin_z

        #Loading phrases
        self.loadingPhrase = [
            'Loading...',
            "Computing...",
            ]
        self.resultsPhrase = [
            'Great...',
            "Awesome!",
            ]

        #Miscellany (aka Garbage no one cares about)
        self.crowdLoopDelay               = crowd_loop_delay
        self.songInfoDisplayScale         = song_info_display_scale
        self.songInfoDisplayX             = song_info_display_X
        self.songInfoDisplayY             = song_info_display_Y
        self.displayAllGreyStars          = display_all_grey_stars
        self.smallMult                    = small_1x_mult
        self.jurgTextPos                  = jurgen_text_pos
        self.oBarHScale                   = obar_hscale
        self.oBar3dFill                   = obar_3dfill
        self.power_up_name                = power_up_name

        #Continuous star fillup!
        self.starFillupCenterX            = star_fillup_center_x
        self.starFillupCenterY            = star_fillup_center_y
        self.starFillupInRadius           = star_fillup_in_radius
        self.starFillupOutRadius          = star_fillup_out_radius
        self.starFillupColor              = star_fillup_color

        #Neck size, neck choose (yeah? you got a problem with that goruping?)
        self.neckWidth                    = neck_width
        self.neckLength                   = neck_length
        self.neck_prompt_x                = menu_neck_choose_x
        self.neck_prompt_y                = menu_neck_choose_y

        #Setlist
        self.songListDisplay              = song_list_display
        self.setlistguidebuttonsposX      = setlistguidebuttonsposX
        self.setlistguidebuttonsposY      = setlistguidebuttonsposY
        self.setlistguidebuttonsscaleX    = setlistguidebuttonsscaleX
        self.setlistguidebuttonsscaleY    = setlistguidebuttonsscaleY
        self.setlistpreviewbuttonposX     = setlistpreviewbuttonposX
        self.setlistpreviewbuttonposY     = setlistpreviewbuttonposY
        self.setlistpreviewbuttonscaleX   = setlistpreviewbuttonscaleX
        self.setlistpreviewbuttonscaleY   = setlistpreviewbuttonscaleY
        self.versiontagposX               = versiontagposX
        self.versiontagposY               = versiontagposY
        self.songSelectSubmenuOffsetLines = song_select_submenu_offset_lines
        self.songSelectSubmenuOffsetSpaces= song_select_submenu_offset_spaces
        self.songSelectSubmenuX           = song_select_submenu_x
        self.songSelectSubmenuY           = song_select_submenu_y
        self.song_cd_Xpos                 = song_cd_x
        self.song_listcd_cd_Xpos          = song_listcd_cd_x
        self.song_listcd_cd_Ypos          = song_listcd_cd_y
        self.song_listcd_score_Xpos       = song_listcd_score_x
        self.song_listcd_score_Ypos       = song_listcd_score_y
        self.song_listcd_list_Xpos        = song_listcd_list_x
        self.song_cdscore_Xpos            = song_cdscore_x
        self.song_list_Xpos               = song_list_x
        self.song_listscore_Xpos          = song_listscore_x

        #pause menu and fail menu
        self.pause_bkg_pos                = pause_bkg
        self.pause_text_xPos              = pause_text_x
        self.pause_text_yPos              = pause_text_y
        self.opt_bkg_size                 = opt_bkg
        self.opt_text_xPos                = opt_text_x
        self.opt_text_yPos                = opt_text_y
        self.fail_bkg_pos                 = fail_bkg
        self.fail_text_xPos               = fail_text_x
        self.fail_text_yPos               = fail_text_y
        self.fail_songname_xPos           = fail_songname_x 
        self.fail_songname_yPos           = fail_songname_y 

        #main menu system
        self.menuX                        = menu_x
        self.menuY                        = menu_y
        self.menuRB                       = rbmenu
        self.loadingX                     = loading_x
        self.loadingY                     = loading_y
        self.loadingFScale                = loading_font_scale
        self.loadingRMargin               = loading_right_margin
        self.loadingLSpacing              = loading_line_spacing
        self.main_menu_scaleVar           = main_menu_scale
        self.main_menu_vspacingVar        = main_menu_vspacing
        self.use_solo_submenu             = use_solo_submenu
        #self.songback                     = songback
        self.versiontag                   = versiontag
        self.shadowoffsetx                = shadowoffsetx
        self.shadowoffsety                = shadowoffsety
        self.menuTipTextY                 = menu_tip_text_y
        self.menuTipTextFont              = menu_tip_text_font
        self.menuTipTextScale             = menu_tip_text_scale
        self.menuTipTextScrollSpace       = menu_tip_text_scroll_space
        self.menuTipTextScrollMode        = menu_tip_text_scroll_mode
        self.menuTipTextDisplay           = menu_tip_text_display
        

        #Lobby
        self.lobbyTitleFont               = lobby_title_font
        self.lobbySelectFont              = lobby_select_font
        self.controlActivateX             = control_activate_x
        self.controlActivateSelectX       = control_activate_select_x
        self.controlActivatePartX         = control_activate_part_x
        self.controlActivateY             = control_activate_y
        self.controlActivateScale         = control_activate_scale
        self.controlActivateSpace         = control_activate_space
        self.controlActivatePartSize      = control_activate_part_size
        self.controlActivateFont          = control_activate_font
        self.controlDescriptionX          = control_description_x
        self.controlDescriptionY          = control_description_y
        self.controlDescriptionScale      = control_description_scale
        self.controlDescriptionFont       = control_description_font
        self.controlCheckX                = control_check_x
        self.controlCheckY                = control_check_y
        self.controlCheckTextY            = control_check_text_y
        self.controlCheckPartMult         = control_check_part_mult
        self.controlCheckScale            = control_check_scale
        self.controlCheckSpace            = control_check_space
        self.controlCheckFont             = control_check_font
        self.characterCreateX             = character_create_x
        self.characterCreateY             = character_create_y
        self.characterCreateOptionX       = character_create_option_x
        self.characterCreateHelpX         = character_create_help_x
        self.characterCreateHelpY         = character_create_help_y
        self.characterCreateHelpScale     = character_create_help_scale
        self.characterCreateOptionFont    = character_create_option_font
        self.characterCreateHelpFont      = character_create_help_font
        self.characterCreateScale         = character_create_scale
        self.characterCreateSpace         = character_create_space
        self.avatarSelectTextX            = avatar_select_text_x
        self.avatarSelectTextY            = avatar_select_text_y
        self.avatarSelectTextScale        = avatar_select_text_scale
        self.avatarSelectFont             = avatar_select_font
        self.avatarSelectAvX              = avatar_select_avatar_x
        self.avatarSelectAvY              = avatar_select_avatar_y
        self.avatarSelectWheelY           = avatar_select_wheel_y

        #Vocal mode
        self.vocalMeterSize               = vocal_meter_size
        self.vocalMeterX                  = vocal_meter_x
        self.vocalMeterY                  = vocal_meter_y
        self.vocalMultX                   = vocal_mult_x
        self.vocalMultY                   = vocal_mult_y
        self.vocalPowerX                  = vocal_power_x
        self.vocalPowerY                  = vocal_power_y
        self.vocalFillupCenterX           = vocal_fillup_center_x
        self.vocalFillupCenterY           = vocal_fillup_center_y
        self.vocalFillupInRadius          = vocal_fillup_in_radius
        self.vocalFillupOutRadius         = vocal_fillup_out_radius
        self.vocalFillupFactor            = vocal_fillup_factor
        self.vocalFillupColor             = vocal_fillup_color
        self.vocalCircularFillup          = vocal_circular_fillup
        self.vocalLaneSize                = vocal_lane_size
        self.vocalGlowSize                = vocal_glow_size
        self.vocalGlowFade                = vocal_glow_fade

        #3D Note/Fret rendering system
        self.twoDnote                     = twoDnote
        self.twoDkeys                     = twoDkeys
        self.threeDspin                   = threeDspin
        self.fret_press                   = fret_press
        # self.noterot                      = [self.config.get("theme", "noterot" + str(i + 1)) for i in range(5)]
        # self.keyrot                       = [self.config.get("theme", "keyrot" + str(i + 1)) for i in range(5)]
        # self.drumnoterot                  = [self.config.get("theme", "drumnoterot" + str(i + 1)) for i in range(5)]
        # self.drumkeyrot                   = [self.config.get("theme", "drumkeyrot" + str(i + 1)) for i in range(5)]
        # self.notepos                      = [self.config.get("theme", "notepos" + str(i + 1)) for i in range(5)]
        # self.keypos                       = [self.config.get("theme", "keypos" + str(i + 1)) for i in range(5)]
        # self.drumnotepos                  = [self.config.get("theme", "drumnotepos" + str(i + 1)) for i in range(5)]
        # self.drumkeypos                   = [self.config.get("theme", "drumkeypos" + str(i + 1)) for i in range(5)]

        #In-game rendering
        self.hopoIndicatorX               = hopo_indicator_x
        self.hopoIndicatorY               = hopo_indicator_y  
        self.markSolos                    = mark_solo_sections

        #Game results scene
        self.result_score                 = result_score
        self.result_star                  = result_star
        self.result_song                  = result_song
        self.result_song_form             = result_song_form
        self.result_song_text             = result_song_text
        self.result_stats_part            = result_stats_part
        self.result_stats_part_text       = result_stats_part_text
        self.result_stats_name            = result_stats_name
        self.result_stats_diff            = result_stats_diff
        self.result_stats_diff_text       = result_stats_diff_text
        self.result_stats_accuracy        = result_stats_accuracy
        self.result_stats_accuracy_text   = result_stats_accuracy_text
        self.result_stats_streak          = result_stats_streak
        self.result_stats_streak_text     = result_stats_streak_text
        self.result_stats_notes           = result_stats_notes
        self.result_stats_notes_text      = result_stats_notes_text
        self.result_cheats_info           = result_cheats_info
        self.result_cheats_numbers        = result_cheats_numbers
        self.result_cheats_percent        = result_cheats_percent
        self.result_cheats_score          = result_cheats_score
        self.result_cheats_color          = result_cheats_color
        self.result_cheats_font           = result_cheats_font
        self.result_high_score_font       = result_high_score_font
        self.result_menu_x                = result_menu_x
        self.result_menu_y                = result_menu_y
        self.result_star_type             = result_star_type

        #Submenus
        self.submenuScale['advsettingstext10'] = .8
        self.submenuScale['careerfailtext4']   = .8
        self.submenuScale['careerpausetext5']  = .8
        self.submenuScale['careerpausetext6']  = .8
        self.submenuScale['failtext3']         = .8
        self.submenuScale['gameresulttext3']   = .8
        self.submenuScale['multiplayertext3']  = .8
        self.submenuScale['multiplayertext4']  = .8
        self.submenuScale['multiplayertext6']  = .8
        self.submenuScale['pausetext5']        = .8
        self.submenuScale['pausetext6']        = .8
        self.submenuScale['setlisttext8']      = .8
        self.submenuScale['settingstext9']     = .8
        self.submenuScale['solotext2']         = .8
        self.submenuScale['trainingtext2']     = .8
        self.submenuVSpace['advsettingstext10']= 0.0008
        self.submenuVSpace['careerfailtext4']  = 0.0
        self.submenuVSpace['careerpausetext5'] = .0008
        self.submenuVSpace['careerpausetext6'] = -0.005
        self.submenuVSpace['failtext3']        = -0.005
        self.submenuVSpace['gameresulttext3']  = -0.004
        self.submenuVSpace['multiplayertext3'] = -0.005
        self.submenuVSpace['multiplayertext4'] = -0.005
        self.submenuVSpace['multiplayertext6'] = .0008
        self.submenuVSpace['pausetext5']       = 0.00081
        self.submenuVSpace['pausetext6']       = -0.00091
        self.submenuVSpace['setlisttext8']     = -0.005
        self.submenuVSpace['settingstext9']    = -0.0011
        self.submenuVSpace['solotext2']        = 0.004
        self.submenuVSpace['trainingtext2']    = 0.0038
        self.submenuX['advsettingstext10']     = .46
        self.submenuX['careerfailtext4']       = 0.29
        self.submenuX['careerpausetext5']      = 0.29
        self.submenuX['careerpausetext6']      = 0.29
        self.submenuX['failtext3']             = 0.29
        self.submenuX['gameresulttext3']       = 0.29
        self.submenuX['multiplayertext3']      = 0.29
        self.submenuX['multiplayertext4']      = 0.40
        self.submenuX['multiplayertext6']      = 0.40
        self.submenuX['pausetext5']            = 0.29
        self.submenuX['pausetext6']            = 0.29
        self.submenuX['setlisttext8']          = .455
        self.submenuX['settingstext9']         = .455
        self.submenuX['solotext2']             = .192
        self.submenuX['trainingtext2']         = .190
        self.submenuY['advsettingstext10']     = 0.07
        self.submenuY['careerfailtext4']       = 0.07
        self.submenuY['careerpausetext5']      = 0.07
        self.submenuY['careerpausetext6']      = 0.07
        self.submenuY['failtext3']             = 0.07
        self.submenuY['gameresulttext3']       = 0.07
        self.submenuY['multiplayertext3']      = 0.07
        self.submenuY['multiplayertext4']      = 0.07
        self.submenuY['multiplayertext6']      = 0.07
        self.submenuY['pausetext5']            = 0.07
        self.submenuY['pausetext6']            = 0.07
        self.submenuY['setlisttext8']          = 0.07
        self.submenuY['settingstext9']         = 0.07
        self.submenuY['solotext2']             = 0.07
        self.submenuY['trainingtext2']         = 0.07
        self.sub_menu_xVar                     = 0.45
        self.sub_menu_yVar                     = 0.5

        self.themeLobby = self.loadThemeModule('CustomLobby')
        self.setlist = self.loadThemeModule('CustomSetlist')
        self.partDiff = self.loadThemeModule('CustomParts')