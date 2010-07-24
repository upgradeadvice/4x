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
__date__ = "$Jul 23, 2010 11:42:36 AM$"
from OpenGL.raw.GL import glColor3f
from OpenGL.raw.GL import glColor4f
from Player import DRUMTYPES
from Player import GUITARTYPES
from Theme import CENTER
from Theme import LEFT
from Theme import RIGHT
from Theme import _
from Theme import Theme

class CustomLobby:

    def __init__(self, theme):
        self.theme = 2
        self.currentImage = -1
        self.nextImage = 0
        self.fadeTime = 2500
        lobby_avatar_scale               = 1.0
        lobby_avatar_x                   = 0.7
        lobby_avatar_y                   = 0.75
        lobby_mode                       = 0
        lobby_preview_spacing            = 0.04
        lobby_preview_x                  = 0.7
        lobby_preview_y                  = 0.0
        lobby_select_image_x             = 0.255
        lobby_select_image_y             = 0.335
        lobby_select_length              = 5
        lobby_select_scale               = 0.0018
        lobby_select_space               = 0.04
        lobby_select_x                   = 0.4
        lobby_select_y                   = 0.32
        lobby_title_character_x          = 0.26
        lobby_title_character_y          = 0.24
        lobby_title_scale                = 0.0024
        lobby_title_x                    = 0.5
        lobby_title_y                    = 0.07
        lobby_select_font                = "font"
        lobby_title_font                 = "loadingFont"
        lobby_disable_color              = "#666666"
        lobby_font_color                 = "#0066D6"
        lobby_info_color                 = "#0066D6"
        lobby_player_color               = "#0066D6"
        lobby_select_color               = "#1DCBEA"
        lobby_title_color                = "#0066D6"
        lobbyOptionColor                 = "#0066D6"
        lobbySaveCharColor               = "#0066D6"
        lobbyGameModeColor               = "#0066D6"
        lobbySelectedColor               = "#1DCBEA"
        lobbyDisabledColor               = "#222222"
        lobbyHeaderColor                 = "#0066D6"
        
        self.lobbyPanelAvatarDimension= (200.00, 110.00)
        self.lobbyTitleText           = _("Main Lobby")
        self.lobbyTitleTextPos        = (.5, .1)
        self.lobbyTitleTextAlign      = CENTER
        self.lobbyTitleTextScale      = .0025
        self.lobbyTitleTextFont       = "font"
        self.lobbySubtitleText        = _("Choose Your Character!")
        self.lobbySubtitleTextPos     = (.5, .15)
        self.lobbySubtitleTextAlign   = CENTER
        self.lobbySubtitleTextScale   = .0015
        self.lobbySubtitleTextFont    = "font"
        self.lobbyOptionScale         = .001
        self.lobbyOptionAlign         = CENTER
        self.lobbyOptionFont          = "font"
        self.lobbyOptionPos           = (.5, .46)
        self.lobbyOptionSpace         = .04
        self.lobbySaveCharScale       = .001
        self.lobbySaveCharAlign       = CENTER
        self.lobbySaveCharFont        = "font"
        self.lobbyGameModePos         = (.985, .03)
        self.lobbyGameModeScale       = .001
        self.lobbyGameModeAlign       = RIGHT
        self.lobbyGameModeFont        = "font"
        self.lobbyPanelNamePos        = (0, 0)
        self.lobbyPanelNameFont       = "font"
        self.lobbyPanelNameScale      = .001
        self.lobbyPanelNameAlign      = LEFT
        self.lobbyControlPos          = (.5,.375)
        self.lobbyControlFont         = "font"
        self.lobbyControlScale        = .0025
        self.lobbyControlAlign        = CENTER
        self.lobbySelectLength        = 4
        self.lobbyPartScale           = .25
        self.lobbyPartPos             = (.5,.52)
        self.lobbyControlImgScale     = .25
        self.lobbyControlImgPos       = (.5,.55)
        self.lobbyKeyboardImgScale    = .1
        self.lobbyKeyboardImgPos      = (.8, .95)
        self.lobbyPanelSize           = (.2, .8)
        self.lobbyPanelPos            = (.04, .1)
        self.lobbyPanelSpacing        = .24
        
        
        self.lobbyOptionColor             = Theme.hexToColor(lobbyOptionColor)
        self.lobbySaveCharColor           = Theme.hexToColor(lobbySaveCharColor)
        self.lobbyGameModeColor           = Theme.hexToColor(lobbyGameModeColor)
        self.lobbySelectedColor           = Theme.hexToColor(lobbySelectedColor)
        self.lobbyDisabledColor           = Theme.hexToColor(lobbyDisabledColor)
        self.lobbyHeaderColor             = Theme.hexToColor(lobbyHeaderColor)
        self.lobbyTitleColor              = Theme.hexToColor(lobby_title_color)
        self.lobbyInfoColor               = Theme.hexToColor(lobby_info_color)
        self.lobbyFontColor               = Theme.hexToColor(lobby_font_color)
        self.lobbyPlayerColor             = Theme.hexToColor(lobby_player_color)
        self.lobbySelectColor             = Theme.hexToColor(lobby_select_color)
        self.lobbyDisableColor            = Theme.hexToColor(lobby_disable_color)
        self.lobbyMode                    = lobby_mode
        self.lobbyPreviewX                = lobby_preview_x
        self.lobbyPreviewY                = lobby_preview_y
        self.lobbyPreviewSpacing          = lobby_preview_spacing
        self.lobbyTitleX                  = lobby_title_x
        self.lobbyTitleY                  = lobby_title_y
        self.lobbyTitleCharacterX         = lobby_title_character_x
        self.lobbyTitleCharacterY         = lobby_title_character_y
        self.lobbyTitleScale              = lobby_title_scale
        self.lobbyTitleFont               = lobby_title_font
        self.lobbyAvatarX                 = lobby_avatar_x
        self.lobbyAvatarY                 = lobby_avatar_y
        self.lobbyAvatarScale             = lobby_avatar_scale
        self.lobbySelectX                 = lobby_select_x
        self.lobbySelectY                 = lobby_select_y
        self.lobbySelectImageX            = lobby_select_image_x
        self.lobbySelectImageY            = lobby_select_image_y
        self.lobbySelectScale             = lobby_select_scale
        self.lobbySelectSpace             = lobby_select_space
        self.lobbySelectFont              = lobby_select_font
        self.lobbySelectLength            = lobby_select_length
  
    def run(self, ticks, lobby):
        self.fadeTime += ticks
        if self.fadeTime >= 2500:
            self.fadeTime -= 2500
            self.currentImage = (self.currentImage + 1) % 4
            i = self.currentImage
            while not lobby.partImages[self.currentImage]:
                self.currentImage = (self.currentImage + 1) % 4
                if i == self.currentImage:
                    break
            if lobby.partImages[self.currentImage]:
                self.nextImage = (self.currentImage + 1) % 4
                i = self.nextImage
                while not lobby.partImages[self.nextImage]:
                    self.nextImage = (self.nextImage + 1) % 4
                    if i == self.nextImage:
                        break
  
    def drawPartImage(self, lobby, type, scale, coord):
        if not lobby.partImages[self.currentImage]:
            return
        if type in GUITARTYPES:
            if self.fadeTime < 1000 or self.nextImage == self.currentImage:
                lobby.drawImage(lobby.partImages[self.currentImage], scale=scale, coord=coord)
            else:
                lobby.drawImage(lobby.partImages[self.currentImage], scale=scale, coord=coord, color=(1, 1, 1, ((2500.0-self.fadeTime) / 1500.0)))
                lobby.drawImage(lobby.partImages[self.nextImage], scale=scale, coord=coord, color=(1, 1, 1, ((self.fadeTime-1000.0) / 1500.0)))
                glColor4f(1, 1, 1, 1)
        elif type in DRUMTYPES:
            if lobby.partImages[4]:
                lobby.drawImage(lobby.partImages[4], scale=scale, coord=coord)
        else:
            if lobby.partImages[5]:
                lobby.drawImage(lobby.partImages[5], scale=scale, coord=coord)
  
    def renderPanels(self, lobby):
        x = self.lobbyPanelPos[0]
        y = self.lobbyPanelPos[1]
        w, h = lobby.geometry
        font = lobby.fontDict['font']
        controlFont   = lobby.fontDict[self.lobbyControlFont]
        panelNameFont = lobby.fontDict[self.lobbyPanelNameFont]
        optionFont    = lobby.fontDict[self.lobbyOptionFont]
        wP = w * self.lobbyPanelSize[0]
        hP = h * self.lobbyPanelSize[1]
        glColor3f(*self.lobbyHeaderColor)
        if self.lobbyTitleText:
            lobby.fontDict[self.lobbyTitleTextFont].render(self.lobbyTitleText, self.lobbyTitleTextPos, scale=self.lobbyTitleTextScale, align=self.lobbyTitleTextAlign)
        if self.lobbySubtitleText:
            lobby.fontDict[self.lobbySubtitleTextFont].render(self.lobbySubtitleText, self.lobbySubtitleTextPos, scale=self.lobbySubtitleTextScale, align=self.lobbySubtitleTextAlign)
        lobby.fontDict[self.lobbyGameModeFont].render(lobby.gameModeText, self.lobbyGameModePos, scale=self.lobbyGameModeScale, align=self.lobbyGameModeAlign)
        for i in range(4):
            j = lobby.panelOrder[i]
            if j in lobby.blockedPlayers or len(lobby.selectedPlayers) == lobby.maxPlayers:
                glColor3f(*self.lobbyDisabledColor)
            else:
                glColor3f(*self.lobbyHeaderColor)
            if i == lobby.keyControl and lobby.img_keyboard_panel:
                lobby.drawImage(lobby.img_keyboard_panel, scale=(self.lobbyPanelSize[0], -self.lobbyPanelSize[1]), coord=(wP * .5 + w * x, hP * .5 + h * y), stretched=3)
            elif lobby.img_panel:
                lobby.drawImage(lobby.img_panel, scale=(self.lobbyPanelSize[0], -self.lobbyPanelSize[1]), coord=(wP * .5 + w * x, hP * .5 + h * y), stretched=3)
            if i == lobby.keyControl and lobby.img_keyboard:
                lobby.drawImage(lobby.img_keyboard, scale=(self.lobbyKeyboardImgScale, -self.lobbyKeyboardImgScale), coord=(wP * self.lobbyKeyboardImgPos[0] + w * x, hP * self.lobbyKeyboardImgPos[1] + h * y))
            controlFont.render(lobby.controls[j], (self.lobbyPanelSize[0] * self.lobbyControlPos[0] + x, self.lobbyPanelSize[1] * self.lobbyControlPos[1] + y), scale=self.lobbyControlScale, align=self.lobbyControlAlign, new=True)
            self.drawPartImage(lobby, lobby.types[j], scale=(self.lobbyPartScale, -self.lobbyPartScale), coord=(wP * self.lobbyPartPos[0] + w * x, hP * self.lobbyPartPos[1] + h * y))
            #self.drawControlImage(lobby, lobby.types[j], scale = (self.lobbyControlImgScale, -self.lobbyControlImgScale), coord = (wP*self.lobbyControlImgPos[0]+w*x, hP*self.lobbyControlImgPos[1]+h*y))
            panelNameFont.render(lobby.options[lobby.selected[j]].lower(), (x + w * self.lobbyPanelNamePos[0], y + h * self.lobbyPanelNamePos[1]), scale=self.lobbyPanelNameScale, align=self.lobbyPanelNameAlign, new=True)
            for l, k in enumerate(range(lobby.pos[j][0], lobby.pos[j][1] + 1)):
                if k >= len(lobby.options):
                    break
                if lobby.selected[j] == k and (j not in lobby.blockedPlayers or j in lobby.selectedPlayers):
                    if lobby.img_selected:
                        lobby.drawImage(lobby.img_selected, scale=(.5, -.5), coord=(wP * .5 + w * x, hP * (.46 * .75) + h * y-(h * .04 * l) / .75))
                    if lobby.avatars[k]:
                        lobby.drawImage(lobby.avatars[k], scale=(lobby.avatarScale[k], -lobby.avatarScale[k]), coord=(wP * .5 + w * x, hP * .7 + h * y))
                    elif k == 0 and lobby.img_newchar_av:
                        lobby.drawImage(lobby.img_newchar_av, scale=(lobby.newCharAvScale, -lobby.newCharAvScale), coord=(wP * .5 + w * x, hP * .7 + h * y))
                    elif lobby.img_default_av:
                        lobby.drawImage(lobby.img_default_av, scale=(lobby.defaultAvScale, -lobby.defaultAvScale), coord=(wP * .5 + w * x, hP * .7 + h * y))
                    glColor3f(*self.lobbySelectedColor)
                elif k in lobby.blockedItems or j in lobby.blockedPlayers:
                    glColor3f(*self.lobbyDisabledColor)
                else:
                    glColor3f(*self.lobbyOptionColor)
                if k == 1:
                    if lobby.img_save_char:
                        lobby.drawImage(lobby.img_save_char, scale=(.5, -.5), coord=(wP * .5 + w * x, hP * (.46 * .75) + h * y-(h * .04 * l) / .75))
                    else:
                        glColor3f(*self.lobbySaveCharColor)
                        lobby.fontDict[self.lobbySaveCharFont].render(lobby.options[k], (self.lobbyPanelSize[0] * self.lobbyOptionPos[0] + x, self.lobbyPanelSize[1] * self.lobbyOptionPos[1] + y + self.lobbyOptionSpace * l), scale=self.lobbySaveCharScale, align=self.lobbySaveCharAlign, new=True)
                else:
                    optionFont.render(lobby.options[k], (self.lobbyPanelSize[0] * self.lobbyOptionPos[0] + x, self.lobbyPanelSize[1] * self.lobbyOptionPos[1] + y + self.lobbyOptionSpace * l), scale=self.lobbyOptionScale, align=self.lobbyOptionAlign, new=True)
            x += self.lobbyPanelSpacing