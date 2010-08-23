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

from OpenGL.raw.GL import glColor3f
from OpenGL.raw.GL import glColor4f
from Player import DRUMTYPES
from Player import GUITARTYPES
from Theme import CENTER
from Theme import LEFT
from Theme import Theme
from Theme import _


class CustomLobby:

    def __init__(self, theme):
        self.theme = 2
        self.currentImage = -1
        self.nextImage = 0
        self.fadeTime = 2900
        self.lobbyControlAlign = CENTER
        self.lobbyControlFont = 'font'
        self.lobbyControlImgPos = (.5, .55)
        self.lobbyControlImgScale = .15
        self.lobbyControlPos = (.5, .15)
        self.lobbyControlScale = .0015
        self.lobbyDisabledColor = (.6, .6, .6)
        self.lobbyGameModeAlign = CENTER
        self.lobbyGameModeColor = Theme.hexToColor('#2891a6')
        self.lobbyGameModeFont = 'font'
        self.lobbyGameModePos = (.115, .715)
        self.lobbyGameModeScale = .0015
        self.lobbyHeaderColor = Theme.hexToColor('#2891a6')
        self.lobbyKeyboardImgPos = (.8, .95)
        self.lobbyKeyboardImgScale = .1
        self.lobbyOptionAlign = CENTER
        self.lobbyOptionColor = Theme.hexToColor('#2891a6')
        self.lobbyOptionFont = 'font'
        self.lobbyOptionPos = (.5, .26)
        self.lobbyOptionScale = .0015
        self.lobbyOptionSpace = .035
        self.lobbyPanelAvatarDimension = (0, 0)
        self.lobbyPanelNameAlign = LEFT
        self.lobbyPanelNameFont = 'font'
        self.lobbyPanelNamePos = (0, 0)
        self.lobbyPanelNameScale = .1
        self.lobbyPanelPos = (.1, .24)
        self.lobbyPanelSize = (.15, .53)
        self.lobbyPanelSpacing = .215
        self.lobbyPartPos = (.5, .84)
        self.lobbyPartScale = .094
        self.lobbySaveCharAlign = CENTER
        self.lobbySaveCharColor = Theme.hexToColor('#2891a6')
        self.lobbySaveCharFont = 'font'
        self.lobbySaveCharScale = .0015
        self.lobbySelectedColor = Theme.hexToColor('#ffffff')
        self.lobbySelectLength = 4
        self.lobbySubtitleText = _('CHOOSE YOUR CHARACTER')
        self.lobbySubtitleTextAlign = CENTER
        self.lobbySubtitleTextFont = 'font'
        self.lobbySubtitleTextPos = (.5, .715)
        self.lobbySubtitleTextScale = .00098
        self.lobbyTitleText = _('LOBBY -')
        self.lobbyTitleTextAlign = CENTER
        self.lobbyTitleTextFont = 'font'
        self.lobbyTitleTextPos = (.05, .715)
        self.lobbyTitleTextScale = .0015

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

    def drawPartImage(
        self,
        lobby,
        parttype,
        scale,
        coord,
        ):
        if not lobby.partImages[self.currentImage]:
            return
        if parttype in GUITARTYPES:
            if self.fadeTime < 1000 or self.nextImage \
                == self.currentImage:
                lobby.drawImage(lobby.partImages[self.currentImage],
                                scale=scale, coord=coord, stretched = 11)
            else:
                lobby.drawImage(lobby.partImages[self.currentImage],
                                scale=scale, coord=coord, color=(1, 1,
                                1, (2500.0 - self.fadeTime) / 1500.0), stretched = 11)
                lobby.drawImage(lobby.partImages[self.nextImage],
                                scale=scale, coord=coord, color=(1, 1,
                                1, (self.fadeTime - 1000.0) / 1500.0), stretched = 11)
                glColor4f(1, 1, 1, 1)
        elif parttype in DRUMTYPES:
            if lobby.partImages[4]:
                lobby.drawImage(lobby.partImages[4], scale=scale,
                                coord=coord, stretched = 11)
        else:
            if lobby.partImages[5]:
                lobby.drawImage(lobby.partImages[5], scale=scale,
                                coord=coord, stretched = 11)

    def renderPanels(self, lobby):
        x = self.lobbyPanelPos[0]
        y = self.lobbyPanelPos[1]
        (w, h) = lobby.geometry

        controlFont = lobby.fontDict[self.lobbyControlFont]
        optionFont = lobby.fontDict[self.lobbyOptionFont]
        wP = w * self.lobbyPanelSize[0]
        hP = h * self.lobbyPanelSize[1]
        glColor3f(*self.lobbyHeaderColor)
        for i in range(4):
            j = lobby.panelOrder[i]
            if j in lobby.blockedPlayers or len(lobby.selectedPlayers) \
                == lobby.maxPlayers:
                glColor3f(*self.lobbyDisabledColor)
            else:
                glColor3f(*self.lobbyHeaderColor)
            if i == lobby.keyControl and lobby.img_keyboard_panel:
                lobby.drawImage(lobby.img_keyboard_panel,
                                scale=(self.lobbyPanelSize[0],
                                -self.lobbyPanelSize[1]), coord=(wP
                                * .5 + w * x, hP * .5 + h * y),
                                stretched=3)
            elif lobby.img_panel:
                lobby.drawImage(lobby.img_panel,
                                scale=(self.lobbyPanelSize[0],
                                -self.lobbyPanelSize[1]), coord=(wP
                                * .5 + w * x, hP * .5 + h * y),
                                stretched=3)
            if i == lobby.keyControl and lobby.img_keyboard:
                lobby.drawImage(lobby.img_keyboard,
                                scale=(self.lobbyKeyboardImgScale,
                                -self.lobbyKeyboardImgScale), coord=(wP
                                * self.lobbyKeyboardImgPos[0] + w * x,
                                hP * self.lobbyKeyboardImgPos[1] + h
                                * y))
            controlFont.render(lobby.controls[j],
                               (self.lobbyPanelSize[0]
                               * self.lobbyControlPos[0] + x,
                               self.lobbyPanelSize[1]
                               * self.lobbyControlPos[1] + y),
                               scale=self.lobbyControlScale,
                               align=self.lobbyControlAlign, new=True)
            self.drawPartImage(lobby, lobby.types[j],
                               scale=(self.lobbyPartScale,
                               -self.lobbyPartScale), coord=(wP
                               * self.lobbyPartPos[0] + w * x, hP
                               * self.lobbyPartPos[1] + h * y))

            for (l, k) in enumerate(range(lobby.pos[j][0],
                                    lobby.pos[j][1] + 1)):
                if k >= len(lobby.options):
                    break
                if lobby.selected[j] == k and (j
                        not in lobby.blockedPlayers or j
                        in lobby.selectedPlayers):
                    if lobby.img_selected:
                        lobby.drawImage(lobby.img_selected, scale=(.5,
                                -.5), coord=(wP * .5 + w * x, hP * (.46
                                * .75) + h * y - h * .04 * l / .75))
                    if lobby.avatars[k]:
                        pass
                    elif k == 0 and lobby.img_newchar_av:
                        pass
                    elif lobby.img_default_av:
                        pass
                    glColor3f(*self.lobbySelectedColor)
                elif k in lobby.blockedItems or j \
                    in lobby.blockedPlayers:
                    glColor3f(*self.lobbyDisabledColor)
                else:
                    glColor3f(*self.lobbyOptionColor)
                if k == 1:
                    if lobby.img_save_char:
                        lobby.drawImage(lobby.img_save_char, scale=(.5,
                                -.5), coord=(wP * .5 + w * x, hP * (.46
                                * .75) + h * y - h * .04 * l / .75))
                    else:
                        glColor3f(*self.lobbySaveCharColor)
                        lobby.fontDict[self.lobbySaveCharFont].render(lobby.options[k],
                                (self.lobbyPanelSize[0]
                                * self.lobbyOptionPos[0] + x,
                                self.lobbyPanelSize[1]
                                * self.lobbyOptionPos[1] + y
                                + self.lobbyOptionSpace * l),
                                scale=self.lobbySaveCharScale,
                                align=self.lobbySaveCharAlign, new=True)
                else:
                    optionFont.render(lobby.options[k],
                            (self.lobbyPanelSize[0]
                            * self.lobbyOptionPos[0] + x,
                            self.lobbyPanelSize[1]
                            * self.lobbyOptionPos[1] + y
                            + self.lobbyOptionSpace * l),
                            scale=self.lobbyOptionScale,
                            align=self.lobbyOptionAlign, new=True)
            x += self.lobbyPanelSpacing


