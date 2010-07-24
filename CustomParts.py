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
__date__ = "$Jul 23, 2010 11:43:27 AM$"
from OpenGL.raw.GL import glColor3f
from Theme import LEFT
from Theme import Theme
from Theme import _

class CustomParts:

    def __init__(self, theme):
        self.theme = theme
        self.partDiffControlAlign = LEFT
        self.partDiffControlFont = 'font'
        self.partDiffControlPos = (.25, .25)
        self.partDiffControlScale = .0015

        self.partDiffGameModeAlign = LEFT
        self.partDiffGameModeColor = Theme.hexToColor('#0066D6')
        self.partDiffGameModeFont = 'font'
        self.partDiffGameModePos = (-5, 0)
        self.partDiffGameModeScale = .00098
        self.partDiffHeaderColor = Theme.hexToColor('#fff')

        self.partDiffKeyboardImgPos = (0, 0)
        self.partDiffKeyboardImgScale = .1

        self.partDiffOptionAlign = LEFT
        self.partDiffOptionColor = Theme.hexToColor('#0066D6')
        self.partDiffOptionFont = 'font'
        self.partDiffOptionPos = (0, 1)
        self.partDiffOptionScale = .00098
        self.partDiffOptionSpace = 0

        self.partDiffPanelNameAlign = LEFT
        self.partDiffPanelNameFont = 'font'
        self.partDiffPanelNamePos = (0, 1)
        self.partDiffPanelNameScale = .001
        self.partDiffPanelPos = (.05, .05)
        self.partDiffPanelSize = (.05, .1)
        self.partDiffPanelSpacing = .24

        # PART ICON

        self.partDiffPartPos = (-0.352, 0)
        self.partDiffPartScale = .35

        self.partDiffSelectedColor = Theme.hexToColor('#1DCBEA')

        self.partDiffSubtitleText = _(' ')
        self.partDiffSubtitleTextAlign = LEFT
        self.partDiffSubtitleTextFont = 'font'
        self.partDiffSubtitleTextPos = (.5, .15)
        self.partDiffSubtitleTextScale = .0015

        self.partDiffTitleText = _('SELECT PART+DIFFICULTY')
        self.partDiffTitleTextAlign = LEFT
        self.partDiffTitleTextFont = 'font'
        self.partDiffTitleTextPos = (.5, .95)
        self.partDiffTitleTextScale = .002
    def run(self, ticks):
        pass
    def drawPartImage(self, dialog, part, scale, coord):
        if part in [0, 2, 4, 5]:
            if dialog.partImages[part]:
                dialog.drawImage(dialog.partImages[part], scale=scale, coord=coord)
        else:
            if dialog.partImages[part]:
                dialog.drawImage(dialog.partImages[part], scale=scale, coord=coord)
            else:
                if dialog.partImages[0]:
                    dialog.drawImage(dialog.partImages[0], scale=scale, coord=coord)
    def renderPanels(self, dialog):
        x = self.partDiffPanelPos[0]
        y = self.partDiffPanelPos[1]
        w, h = dialog.geometry
        font = dialog.fontDict['font']
        controlFont   = dialog.fontDict[self.partDiffControlFont]
        panelNameFont = dialog.fontDict[self.partDiffPanelNameFont]
        optionFont    = dialog.fontDict[self.partDiffOptionFont]
        wP = w * self.partDiffPanelSize[0]
        hP = h * self.partDiffPanelSize[1]
        glColor3f(*self.partDiffHeaderColor)
        if self.partDiffTitleText:
            dialog.fontDict[self.partDiffTitleTextFont].render(self.partDiffTitleText, self.partDiffTitleTextPos, scale=self.partDiffTitleTextScale, align=self.partDiffTitleTextAlign)
        if self.partDiffSubtitleText:
            dialog.fontDict[self.partDiffSubtitleTextFont].render(self.partDiffSubtitleText, self.partDiffSubtitleTextPos, scale=self.partDiffSubtitleTextScale, align=self.partDiffSubtitleTextAlign)
        for i in range(len(dialog.players)):
            glColor3f(*self.partDiffHeaderColor)
            dialog.fontDict[self.partDiffGameModeFont].render(dialog.gameModeText, self.partDiffGameModePos, scale=self.partDiffGameModeScale, align=self.partDiffGameModeAlign)
            if i == dialog.keyControl and dialog.img_keyboard_panel:
                dialog.drawImage(dialog.img_keyboard_panel, scale=(self.partDiffPanelSize[0], -self.partDiffPanelSize[1]), coord=(wP * .5 + w * x, hP * .5 + h * y), stretched=3)
            elif dialog.img_panel:
                dialog.drawImage(dialog.img_panel, scale=(self.partDiffPanelSize[0], -self.partDiffPanelSize[1]), coord=(wP * .5 + w * x, hP * .5 + h * y), stretched=3)
            if i == dialog.keyControl and dialog.img_keyboard:
                dialog.drawImage(dialog.img_keyboard, scale=(self.partDiffKeyboardImgScale, -self.partDiffKeyboardImgScale), coord=(wP * self.partDiffKeyboardImgPos[0] + w * x, hP * self.partDiffKeyboardImgPos[1] + h * y))
            #controlFont.render(dialog.players[i].name, (self.partDiffPanelSize[0] * self.partDiffControlPos[0] + x, self.partDiffPanelSize[1] * self.partDiffControlPos[1] + y), scale=self.partDiffControlScale, align=self.partDiffControlAlign, new=True)
            panelNameFont.render(dialog.players[i].name.lower(), (x + w * self.partDiffPanelNamePos[0], y + h * self.partDiffPanelNamePos[1]), scale=self.partDiffPanelNameScale, align=self.partDiffPanelNameAlign, new=True)
            if dialog.mode[i] == 0:
                self.drawPartImage(dialog, dialog.parts[i][dialog.selected[i]].id, scale=(self.partDiffPartScale, -self.partDiffPartScale), coord=(wP * self.partDiffPartPos[0] + w * x, hP * self.partDiffPartPos[1] + h * y))
                for p in range(len(dialog.parts[i])):
                    if dialog.selected[i] == p:
                        if dialog.img_selected:
                            dialog.drawImage(dialog.img_selected, scale=(.5, -.5), coord=(wP * .5 + w * x, hP * (.46 * .75) + h * y-(h * .04 * p) / .75))
                        glColor3f(*self.partDiffSelectedColor)
                    else:
                        glColor3f(*self.partDiffOptionColor)
                    font.render(str(dialog.parts[i][p]), (.09 * .5 * p + x, 1.295 * .46 + y + .07), scale=.001, align=0, new=True)
            elif dialog.mode[i] == 1:
                self.drawPartImage(dialog, dialog.players[i].part.id, scale=(self.partDiffPartScale, -self.partDiffPartScale), coord=(wP * self.partDiffPartPos[0] + w * x, hP * self.partDiffPartPos[1] + h * y))
                for d in range(len(dialog.info.partDifficulties[dialog.players[i].part.id])):
                    if dialog.selected[i] == d:
                        if dialog.img_selected:
                            dialog.drawImage(dialog.img_selected, scale=(.5, -.5), coord=(wP * .5 + w * x, hP * (.46 * .75) + h * y-(h * .04 * d) / .75))
                        glColor3f(*self.partDiffSelectedColor)
                    else:
                        glColor3f(*self.partDiffOptionColor)
                    font.render(str(dialog.info.partDifficulties[dialog.players[i].part.id][d]), (.09 * .65 * d + x, 1.295 * .46 + y + .07), scale=.001, align=0, new=True)
                if i in dialog.readyPlayers:
                    if dialog.img_ready:
                        dialog.drawImage(dialog.img_ready, scale=(.5, -.5), coord=(wP * .5 + w * x, hP * (.75 * .46) + h * y))
            x += .24