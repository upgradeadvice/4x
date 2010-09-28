# -*- coding: utf-8 -*-
#####################################################################
#                                                                   #
# Frets on Fire X (FoFiX)                                           #
# Copyright (C) 2006 Sami Kyöstilä                                  #
#               2008 myfingershurt                                  #
#               2008 Blazingamer                                    #
#               2008 evilynux <evilynux@gmail.com>                  #
#               2010 FoFiX Team                                     #
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
__date__   = "$Aug 23, 2010 03:30:05 AM$"

from Theme import Theme


class CustomTheme(Theme):

    def __init__(
        self,
        path,
        name,
        iniFile=False,
        ):

        Theme.__init__(self, path, name)
        
        #new
        self.menuPos = [0.5,0.070000000000000007]
        self.povTarget  = (0.0, 1.0, 3.0)
        self.povOrigin  = (0.0, 2.0, -3.5)
        self.countdownPosX = 0.5
        self.countdownPosY = 0.30

        artist_selected_color = '#ffffff'
        artist_text_color = '#497A5D'
        background_color = '#000000'
        bars_color = '#497A5D'
        base_color = '#497A5D'
        career_title_color = '#497A5D'
        character_create_font_color = '#497A5D'
        character_create_help_color = '#497A5D'
        character_create_select_color = '#ffffff'
        fail_completed_color = '#497A5D'
        fail_selected_color = '#ffffff'
        fail_text_color = '#497A5D'
        fret0_color = '#497A5D'
        fret1_color = '#497A5D'
        fret2_color = '#497A5D'
        fret3_color = '#497A5D'
        fret4_color = '#497A5D'
        fret5_color = '#497A5D'
        fretK_color = '#497A5D'
        fretS_color = '#497A5D'
        glow_color = '#497A5D'
        hopo_color = '#497A5D'
        hopo_indicator_active_color = '#497A5D'
        hopo_indicator_inactive_color = '#497A5D'
        ingame_stats_color = '#497A5D'
        key2_color = '#497A5D'
        key_color = '#497A5D'
        library_selected_color = '#ffffff'
        library_text_color = '#497A5D'
        loading_text_color = '#497A5D'
        menu_tip_text_color = '#497A5D'
        mesh_color = '#497A5D'
        opt_selected_color = '#ffffff'
        opt_text_color = '#497A5D'
        pause_selected_color = '#ffffff'
        pause_text_color = '#497A5D'
        rockmeter_score_color = '#497A5D'
        selected_color = '#ffffff'
        songlistcd_score_color = '#497A5D'
        songlist_score_color = '#497A5D'
        song_name_selected_color = '#ffffff'
        song_name_text_color = '#497A5D'
        song_rb2_diff_color = '#497A5D'
        spot_color = '#497A5D'
        star_fillup_color = '#497A5D'
        tracks_color = '#497A5D'
        vocal_glow_color = '#497A5D'
        vocal_glow_color_star = '#497A5D'
        vocal_lane_color = '#497A5D'
        vocal_lane_color_star = '#497A5D'
        vocal_shadow_color = '#497A5D'
        vocal_shadow_color_star = '#497A5D'

        self.shaderSolocolor = (1,0.90588235294118,0.53333333333333,0.6)
        self.fail_bkg_pos       = [1, 1, .00035]
        self.fail_text_xPos     = .5
        self.fail_text_yPos     = .5
        self.fail_songname_xPos = .5
        self.fail_songname_yPos = .6
		
        self.result_score = [1, 1, .00035]
        self.result_star = [1, 1, .00035]
        self.result_song = [1, 1, .00035]
        self.result_song_form = .5
        self.result_song_text = "result_song_text"
        self.result_stats_part = [1, 1, .00035]
        self.result_stats_part_text = "result_stats_part_text"
        self.result_stats_name = [1, 1, .00035]
        self.result_stats_diff = [1, 1, .00035]
        self.result_stats_diff_text = "result_stats_diff_text"
        self.result_stats_accuracy = [1, 1, .00035]
        self.result_stats_accuracy_text = "result_stats_accuracy_text"
        self.result_stats_streak = [1, 1, .00035]
        self.result_stats_streak_text = "result_stats_streak_text"
        self.result_stats_notes = [1, 1, .00035]
        self.result_stats_notes_text = "result_stats_notes_text"
        self.result_cheats_info = [1, 1, .00035]
        self.result_cheats_numbers = [1, 1, .00035]
        self.result_cheats_percent = [1, 1, .00035]
        self.result_cheats_score   = [1, 1, .00035]
        self.result_cheats_color   = (1, 1, 1)
        self.result_cheats_font    = 'font'
        self.result_high_score_font = 'font'
        self.result_menu_x         = 'font'
        self.result_menu_y         = 'font'
        self.result_star_type      = 1

        self.artist_selected_colorVar = \
            self.hexToColor(artist_selected_color)
        self.artist_text_colorVar = self.hexToColor(artist_text_color)
        self.avatarSelectAvX = .75
        self.avatarSelectAvY = .35
        self.avatarSelectWheelY = 0.0
        self.backgroundColor = self.hexToColor(background_color)
        self.barsColor = self.hexToColor(bars_color)
        self.baseColor = self.hexToColor(base_color)
        self.career_title_colorVar = self.hexToColor(career_title_color)
        self.characterCreateFontColor = \
            self.hexToColor(character_create_font_color)
        self.characterCreateHelpColor = \
            self.hexToColor(character_create_help_color)
        self.characterCreateHelpScale = 0.0009
        self.characterCreateHelpX = 0.5
        self.characterCreateHelpY = 0.72
        self.characterCreateOptionX = .75
        self.characterCreateScale = .0018
        self.characterCreateSelectColor = \
            self.hexToColor(character_create_select_color)
        self.characterCreateSpace = .045
        self.characterCreateX = .25
        self.characterCreateY = 0.15
        self.controlActivateFont = 'loadingFont'
        self.controlActivatePartSize = 22.000
        self.controlActivatePartX = .41
        self.controlActivateScale = .0018
        self.controlActivateSelectX = 0.5
        self.controlActivateSpace = .045
        self.controlActivateX = .645
        self.controlActivateY = .18
        self.controlCheckFont = 'loadingFont'
        self.controlCheckPartMult = 2.8
        self.controlCheckSpace = .23
        self.controlCheckTextY = .61
        self.controlCheckX = .16
        self.controlCheckY = .26
        self.controlDescriptionFont = 'font'
        self.controlDescriptionScale = .002
        self.controlDescriptionX = 0.5
        self.controlDescriptionY = .617
        self.displayAllGreyStars = False
        self.fail_bkg_pos = [0.5, 0.5, 1.000, 1.000]
        self.fail_completed_colorVar = \
            self.hexToColor(fail_completed_color)
        self.fail_selected_colorVar = \
            self.hexToColor(fail_selected_color)
        self.fail_songname_xPos = 0.5
        self.fail_songname_yPos = .35
        self.fail_text_colorVar = self.hexToColor(fail_text_color)
        self.fail_text_xPos = None
        self.fail_text_yPos = 0.40000000000000002
        self.fret_press = True
        self.glowColor = self.hexToColor(glow_color)
        self.hopoColor = self.hexToColor(hopo_color)
        self.hopoIndicatorActiveColor = \
            self.hexToColor(hopo_indicator_active_color)
        self.hopoIndicatorInactiveColor = \
            self.hexToColor(hopo_indicator_inactive_color)
        self.hopoIndicatorX = None
        self.hopoIndicatorY = None
        self.ingame_stats_colorVar = \
            self.hexToColorResults(ingame_stats_color)
        self.jurgTextPos = [1, 1, .00035]
        self.key2Color = self.hexToColor(key2_color)
        self.keyColor = self.hexToColor(key_color)
        self.keypos = [-0.09, -0.09, -0.09, -0.09, -0.09]
        self.killNoteColor = self.hexToColor(fretK_color)
        self.library_selected_colorVar = \
            self.hexToColor(library_selected_color)
        self.library_text_colorVar = self.hexToColor(library_text_color)
        self.loadingColor = self.hexToColor(loading_text_color)
        self.loadingFScale = 0.0015
        self.loadingLSpacing = 1
        self.loadingRMargin = 1.000
        self.loadingX = .5
        self.loadingY = .070000000000000007
        self.lobbyPanelAvatarDimension = (100.00, 55.00)
        self.lobbyPreviewX = 0.69999999999999996
        self.lobbySelectFont = 'loadingFont'
        self.lobbySelectImageX = 0.255
        self.lobbySelectImageY = 0.335
        self.lobbySelectLength = 4
        self.lobbySelectScale = .0018
        self.lobbySelectSpace = 0.040000000000000001
        self.lobbySelectX = 0.40000000000000002
        self.lobbySelectY = 0.32
        self.lobbyTitleCharacterX = .26
        self.lobbyTitleCharacterY = 0.24
        self.lobbyTitleFont = 'font'
        self.lobbyTitleScale = 0.0024
        self.lobbyTitleX = 0.40000000000000002
        self.lobbyTitleY = 0.59999999999999998
        self.main_menu_scaleVar = 1
        self.main_menu_vspacingVar = 0.000000
        self.menuRB = True
        self.menuTipTextColor = \
            self.hexToColorResults(menu_tip_text_color)
        self.menuTipTextDisplay = True
        self.menuTipTextFont = 'font'
        self.menuTipTextScale = 0.001
        self.menuTipTextScrollMode = 0
        self.menuTipTextScrollSpace = .25
        self.menuTipTextY = .715
        self.menuX = 0.5
        self.menuY = 0.070000000000000007
        self.meshColor = self.hexToColor(mesh_color)
        self.oBarHScale = 0.69999999999999996
        self.opt_bkg_size = [0.5, 0.5, 1.000, 1.000]
        self.opt_selected_colorVar = self.hexToColor(opt_selected_color)
        self.opt_text_colorVar = self.hexToColor(opt_text_color)
        self.opt_text_xPos = None
        self.opt_text_yPos = None
        self.pause_bkg_pos = [0.5, 0.5, 1.000, 1.000]
        self.pause_selected_colorVar = \
            self.hexToColor(pause_selected_color)
        self.pause_text_colorVar = self.hexToColor(pause_text_color)
        self.pause_text_xPos = None
        self.pause_text_yPos = None
        self.povOriginX = 0
        self.povOriginY = 2
        self.povOriginZ = -3.5
        self.povTargetX = 0
        self.povTargetY = 1
        self.povTargetZ = 3
        self.power_up_name = None
        self.rbmenu = True

        self.result_menu_x = 0.40000000000000002
        self.result_menu_y = .2

        self.result_cheats_color = (1, 1, 1)
        self.result_cheats_font = 'font'
        self.result_high_score_font = 'font'
        self.result_song_text = '- %s -'
        self.result_stats_accuracy_text = '%.1f%%'
        self.result_stats_diff_text = '  %s'
        self.result_stats_notes_text = '%s Hit'
        self.result_stats_part_text = '%s'
        self.result_stats_streak_text = '%d Streak'

        self.result_song = (.35, .2, .0008, None)

        self.result_score = (.35, .26, 0.0004)
        self.result_stats_diff = (0.5, .26, 0.0016, None)
        self.result_stats_part = (.65, .26, 0.0016, None)
        self.result_stats_notes = (.35, .34, .0018, None)
        self.result_stats_accuracy = (0.5, .34, .0018, None)
        self.result_stats_streak = (.65, .34, .0018, None)
        self.result_stats_name = (0.5, .42, 0.0025, None, None)
        self.result_star = (0.5, .30, 0.070000000000000007, 1.000)

        self.result_cheats_info = (.64, .26, .0013)
        self.result_cheats_numbers = (.64, .28, .0013)
        self.result_cheats_percent = (.64, 0.29999999999999999, .0013)

        self.result_song_form = 3
        self.rockmeter_score_colorVar = \
            self.hexToColorResults(rockmeter_score_color)
        self.selectedColor = self.hexToColor(selected_color)
        self.shadowoffsetx = 0.0
        self.shadowoffsety = 0.0
        self.songInfoDisplayScale = .0008
        self.songInfoDisplayX = .05
        self.songInfoDisplayY = .05
        self.songlistcd_score_colorVar = \
            self.hexToColor(songlistcd_score_color)
        self.songListDisplay = 3
        self.songlist_score_colorVar = \
            self.hexToColor(songlist_score_color)
        self.songSelectSubmenuOffsetLines = 4
        self.songSelectSubmenuOffsetSpaces = 3
        self.songSelectSubmenuX = 0.10000000000000001
        self.songSelectSubmenuY = 0.075
        self.song_cdscore_Xpos = 0.59999999999999998
        self.song_cd_Xpos = 0.0
        self.song_listcd_cd_Xpos = .25
        self.song_listcd_cd_Ypos = 0.59999999999999998
        self.song_listcd_list_Xpos = 0.5
        self.song_listcd_score_xpos = 0.10000000000000001
        self.song_listcd_score_ypos = 0.59999999999999998
        self.song_listscore_Xpos = 0.69999999999999996
        self.song_list_Xpos = 0.29999999999999999
        self.song_name_selected_colorVar = \
            self.hexToColor(song_name_selected_color)
        self.song_name_text_colorVar = \
            self.hexToColor(song_name_text_color)
        self.song_rb2_diff_colorVar = \
            self.hexToColor(song_rb2_diff_color)
        self.noteColors = [self.hexToColor(fret0_color),self.hexToColor(fret1_color),self.hexToColor(fret2_color),self.hexToColor(fret3_color),self.hexToColor(fret4_color),self.hexToColor(fret5_color)]
        self.spNoteColor = self.hexToColor(fretS_color)
        self.spotColor = self.hexToColor(spot_color)
        self.starFillupCenterX = 139
        self.starFillupCenterY = 151
        self.starFillupColor = self.hexToColor(star_fillup_color)
        self.starFillupInRadius = 121
        self.starFillupOutRadius = 138
        self.submenuScale['advsettingstext10'] = 1
        self.submenuScale['careerfailtext4'] = 1
        self.submenuScale['careerpausetext5'] = 1
        self.submenuScale['careerpausetext6'] = 1
        self.submenuScale['failtext3'] = 1
        self.submenuScale['gameresulttext3'] = 1
        self.submenuScale['multiplayertext3'] = 1
        self.submenuScale['multiplayertext4'] = 1
        self.submenuScale['multiplayertext7'] = 1
        self.submenuScale['pausetext5'] = 1
        self.submenuScale['pausetext6'] = 1
        self.submenuScale['setlisttext8'] = 1
        self.submenuScale['settingstext9'] = 1
        self.submenuScale['solotext2'] = 1
        self.submenuScale['trainingtext2'] = 1
        self.submenuVSpace['advsettingstext10'] = 0.0000000000000000000000000000000000000
        self.submenuVSpace['careerfailtext4'] = 0.00000000000000000000000000000000000000
        self.submenuVSpace['careerpausetext5'] = 0.0000000000000000000000000000000000000
        self.submenuVSpace['careerpausetext6'] = 0.0000000000000000000000000000000000000
        self.submenuVSpace['failtext3'] =0.0000000000000000000000000000000000000
        self.submenuVSpace['gameresulttext3'] = 0.0000000000000000000000000000000000000
        self.submenuVSpace['multiplayertext3'] = 0.0000000000000000000000000000000000000
        self.submenuVSpace['multiplayertext4'] = 0.0000000000000000000000000000000000000
        self.submenuVSpace['multiplayertext7'] = 0.0000000000000000000000000000000000000
        self.submenuVSpace['pausetext5'] = 0.0000000000000000000000000000000000000
        self.submenuVSpace['pausetext6'] = 0.0000000000000000000000000000000000000
        self.submenuVSpace['setlisttext8'] = 0.0000000000000000000000000000000000000
        self.submenuVSpace['settingstext9'] = 0.0000000000000000000000000000000000000
        self.submenuVSpace['solotext2'] = 0.0000000000000000000000000000000000000
        self.submenuVSpace['trainingtext2'] = 0.0000000000000000000000000000000000000
        self.submenuX['advsettingstext10'] = 0.5
        self.submenuX['careerfailtext4'] = 0.5
        self.submenuX['careerpausetext5'] = 0.5
        self.submenuX['careerpausetext6'] = 0.5
        self.submenuX['failtext3'] = 0.5
        self.submenuX['gameresulttext3'] = 0.5
        self.submenuX['multiplayertext3'] = 0.5
        self.submenuX['multiplayertext4'] = 0.5
        self.submenuX['multiplayertext7'] = 0.5
        self.submenuX['pausetext5'] = 0.5
        self.submenuX['pausetext6'] = 0.5
        self.submenuX['setlisttext8'] = 0.5
        self.submenuX['settingstext9'] = 0.5
        self.submenuX['solotext2'] = 0.5
        self.submenuX['trainingtext2'] = 0.5
        self.submenuY['advsettingstext10'] = 0.070000000000000007
        self.submenuY['careerfailtext4'] = 0.070000000000000007
        self.submenuY['careerpausetext5'] = 0.070000000000000007
        self.submenuY['careerpausetext6'] = 0.070000000000000007
        self.submenuY['failtext3'] = 0.070000000000000007
        self.submenuY['gameresulttext3'] = 0.070000000000000007
        self.submenuY['multiplayertext3'] = 0.070000000000000007
        self.submenuY['multiplayertext4'] = 0.070000000000000007
        self.submenuY['multiplayertext7'] = 0.070000000000000007
        self.submenuY['pausetext5'] = 0.070000000000000007
        self.submenuY['pausetext6'] = 0.070000000000000007
        self.submenuY['setlisttext8'] = 0.070000000000000007
        self.submenuY['settingstext9'] = 0.070000000000000007
        self.submenuY['solotext2'] = 0.070000000000000007
        self.submenuY['trainingtext2'] = 0.070000000000000007
        self.sub_menu_xVar = 0.5
        self.sub_menu_yVar = 0.070000000000000007
        self.threeDspin = True
        self.tracksColor = self.hexToColor(tracks_color)
        self.twoDkeys = False
        self.twoDnote = False
        self.use_fret_colors = False
        self.use_solo_submenu = True
        self.versiontag = False
        self.versiontagposX = 0.9422
        self.versiontagposY = 0.06
        self.vocalCircularFillup = True
        self.vocalFillupCenterX = 139
        self.vocalFillupCenterY = 151
        self.vocalFillupColor = self.hexToColorResults('#497A5D')
        self.vocalFillupFactor = 300.000
        self.vocalFillupInRadius = 25
        self.vocalFillupOutRadius = 139
        self.vocalGlowColor = self.hexToColorResults(vocal_glow_color)
        self.vocalGlowColorStar = \
            self.hexToColorResults(vocal_glow_color_star)
        self.vocalGlowFade = 0.59999999999999998
        self.vocalGlowSize = .008
        self.vocalLaneColor = self.hexToColorResults(vocal_lane_color)
        self.vocalLaneColorStar = \
            self.hexToColorResults(vocal_lane_color_star)
        self.vocalLaneSize = .0008
        self.vocalMeterSize = 45.000
        self.vocalMeterX = 0.5
        self.vocalMeterY = .75
        self.vocalMultX = 0.5
        self.vocalMultY = .8
        self.vocalPowerX = 0.5
        self.vocalPowerY = .8
        self.vocalShadowColor = \
            self.hexToColorResults(vocal_shadow_color)
        self.vocalShadowColorStar = \
            self.hexToColorResults(vocal_shadow_color_star)

        self.loadingPhrase = [
            '',
            "I'm an instant star. Just add water and stir. - David Bowie"
                ,
            '',
            'Forget all that macho shit, and learn how to play guitar. - John Mellencamp'
                ,
            'Time you enjoy wasting, was not wasted. - John Lennon',
            'Turn off your cheats already!',
            "I don't know anything about music, In my line you don't have to. - Elvis Presley"
                ,
            '',
            'Onstage, I make love to 25,000 people, then I go home alone. - Janis Joplin'
                ,
            "I've been imitated so well I've heard people copy my mistakes. - Jimi Hendrix"
                ,
            "I'm just a musical prostitute, my dear. - Freddie Mercury"
                ,
            '',
            'The worst crime is faking it. - Kurt Cobain',
            '',
            ]

        self.themeLobby = self.loadThemeModule('CustomLobby')
        self.setlist = self.loadThemeModule('CustomSetlist')
        self.partDiff = self.loadThemeModule('CustomParts')


