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
__date__ = "$Jul 23, 2010 11:42:59 AM$"

import math
import string
from OpenGL.GL import glRotate
from OpenGL.raw.GL import glBlendFunc
from OpenGL.raw.GL import glColor3f
from OpenGL.raw.GL import glColor4f
from OpenGL.raw.GL import glDepthMask
from OpenGL.raw.GL import glDisable
from OpenGL.raw.GL import glEnable
from OpenGL.raw.GL import glGetIntegerv
from OpenGL.raw.GL import glLoadIdentity
from OpenGL.raw.GL import glMatrixMode
from OpenGL.raw.GL import glOrtho
from OpenGL.raw.GL import glPopMatrix
from OpenGL.raw.GL import glPushMatrix
from OpenGL.raw.GL import glScalef
from OpenGL.raw.GL import glTranslatef
from OpenGL.raw.GL.constants import GL_BLEND
from OpenGL.raw.GL.constants import GL_COLOR_MATERIAL
from OpenGL.raw.GL.constants import GL_CULL_FACE
from OpenGL.raw.GL.constants import GL_DEPTH_TEST
from OpenGL.raw.GL.constants import GL_MODELVIEW
from OpenGL.raw.GL.constants import GL_NORMALIZE
from OpenGL.raw.GL.constants import GL_ONE_MINUS_SRC_ALPHA
from OpenGL.raw.GL.constants import GL_PROJECTION
from OpenGL.raw.GL.constants import GL_SRC_ALPHA
from OpenGL.raw.GL.constants import GL_TEXTURE
from OpenGL.raw.GL.constants import GL_TEXTURE_2D
from OpenGL.raw.GL.constants import GL_VIEWPORT
from OpenGL.raw.GLU import gluPerspective

import Song as Song
from Shader import shaders
from Theme import _


class CustomSetlist:
    def __init__(self, theme):
        self.theme = theme
        self.setlist_type = theme.songListDisplay
        if self.setlist_type is None:
            self.setlist_type = 3
        if self.setlist_type == 0: #CD mode
            self.setlistStyle = 0
            self.headerSkip = 0
            self.footerSkip = 0
            self.labelType = 1
            self.labelDistance = 2
            self.showMoreLabels = True
            self.texturedLabels = True
            self.itemsPerPage = 1
            self.showLockedSongs = False
            self.showSortTiers = True
            self.selectTiers = False
            self.itemSize = (0, .125)
        elif self.setlist_type == 1: #List mode
            self.setlistStyle = 1
            self.headerSkip = 2
            self.footerSkip = 1
            self.labelType = 0
            self.labelDistance = 0
            self.showMoreLabels = False
            self.texturedLabels = False
            self.itemsPerPage = 7
            self.showLockedSongs = False
            self.showSortTiers = True
            self.selectTiers = False
            self.itemSize = (0, .126)
        elif self.setlist_type == 2: #List/CD mode
            self.setlistStyle = 1
            self.headerSkip = 0
            self.footerSkip = 1
            self.labelType = 1
            self.labelDistance = 1
            self.showMoreLabels = False
            self.texturedLabels = True
            self.itemsPerPage = 8
            self.showLockedSongs = False
            self.showSortTiers = True
            self.selectTiers = False
            self.itemSize = (0, .125)
        else: #RB2 mode
            self.setlistStyle = 0
            self.headerSkip = 0
            self.footerSkip = 0
            self.labelType = 0
            self.labelDistance = 1
            self.showMoreLabels = False
            self.texturedLabels = False
            self.itemsPerPage = 12
            self.showLockedSongs = True
            self.showSortTiers = True
            self.selectTiers = False
            self.itemSize = (0, .07)

        self.career_title_color = self.theme.career_title_colorVar
        self.song_name_text_color = self.theme.song_name_text_colorVar
        self.song_name_selected_color = self.theme.song_name_selected_colorVar
        self.song_rb2_diff_color = self.theme.song_rb2_diff_colorVar
        self.artist_text_color = self.theme.artist_text_colorVar
        self.artist_selected_color = self.theme.artist_selected_colorVar
        self.library_text_color = self.theme.library_text_colorVar
        self.library_selected_color = self.theme.library_selected_colorVar
        self.songlist_score_color = self.theme.songlist_score_colorVar
        self.songlistcd_score_color = self.theme.songlistcd_score_colorVar

        self.song_cd_xpos = theme.song_cd_Xpos
        self.song_cdscore_xpos = theme.song_cdscore_Xpos
        self.song_list_xpos = theme.song_list_Xpos
        self.song_listscore_xpos = theme.song_listscore_Xpos
        self.song_listcd_list_xpos = theme.song_listcd_list_Xpos
        self.song_listcd_cd_xpos = theme.song_listcd_cd_Xpos
        self.song_listcd_cd_ypos = theme.song_listcd_cd_Ypos
        self.song_listcd_score_xpos = theme.song_listcd_score_Xpos
        self.song_listcd_score_ypos = theme.song_listcd_score_Ypos

    def run(self, ticks):
        pass

    def renderHeader(self, scene):
        pass

    def renderUnselectedItem(self, scene, i, n):
        w, h = scene.geometry
        font = scene.fontDict['songListFont']
        lfont = scene.fontDict['songListFont']
        #sfont = scene.fontDict['shadowfont']
        if self.setlist_type == 0:
            return
        elif self.setlist_type == 1:
            if not scene.items:
                return
            item = scene.items[i]

            glColor4f(0, 0, 0, 1)
            if isinstance(item, Song.SongInfo) or isinstance(item, Song.RandomSongInfo):
                c1, c2, c3 = self.song_name_text_color
                glColor3f(c1, c2, c3)
            elif isinstance(item, Song.LibraryInfo):
                c1, c2, c3 = self.library_text_color
                glColor3f(c1, c2, c3)
            elif isinstance(item, Song.TitleInfo) or isinstance(item, Song.SortTitleInfo):
                c1, c2, c3 = self.career_title_color
                glColor3f(c1, c2, c3)

            text = item.name

            if isinstance(item, Song.SongInfo) and item.getLocked(): #TODO: SongDB
                text = _("-- Locked --")

            if isinstance(item, Song.SongInfo): #MFH - add indentation when tier sorting
                if scene.tiersPresent:
                    text = "    " + text

            if isinstance(item, Song.TitleInfo) or isinstance(item, Song.SortTitleInfo):
                text = string.upper(text)

            scale = lfont.scaleText(text, maxwidth=0.440)

            lfont.render(text, (self.song_list_xpos, .0925 * (n + 1)-.0375), scale=scale)


            #MFH - Song list score / info display:
            if isinstance(item, Song.SongInfo) and not item.getLocked():
                scale = 0.0009
                text = scene.scoreDifficulty.text
                c1, c2, c3 = self.songlist_score_color
                glColor3f(c1, c2, c3)
                lfont.render(text, (self.song_listscore_xpos, .0925 * (n + 1)-.034), scale=scale, align=2)
                if not item.frets == "":
                    suffix = ", (" + item.frets + ")"
                else:
                    suffix = ""

                if not item.year == "":
                    yeartag = ", " + item.year
                else:
                    yeartag = ""


                scale = .0014
                c1, c2, c3 = self.artist_text_color
                glColor3f(c1, c2, c3)

                # evilynux - Force uppercase display for artist name
                text = string.upper(item.artist) + suffix + yeartag

                # evilynux - automatically scale artist name and year
                scale = lfont.scaleText(text, maxwidth=0.440, scale=scale)
                if scale > .0014:
                    scale = .0014

                lfont.render(text, (self.song_list_xpos + .05, .0925 * (n + 1) + .0125), scale=scale)

                score = _("Nil")
                stars = 0
                name = ""

                try:
                    difficulties = item.partDifficulties[scene.scorePart.id]
                except KeyError:
                    difficulties = []
                for d in difficulties:
                    if d.id == scene.scoreDifficulty.id:
                        scores = item.getHighscores(d, part=scene.scorePart)
                        if scores:
                            score, stars, name, scoreExt = scores[0]
                            try:
                                notesHit, notesTotal, noteStreak, modVersion, handicap, handicapLong, originalScore = scoreExt
                            except ValueError:
                                notesHit, notesTotal, noteStreak, modVersion, oldScores1, oldScores2 = scoreExt
                                handicap = 0
                                handicapLong = "None"
                                originalScore = score
                        else:
                            score, stars, name = 0, 0, "---"

                if score == _("Nil") and scene.nilShowNextScore:   #MFH
                    for d in difficulties:   #MFH - just take the first valid difficulty you can find and display it.
                        scores = item.getHighscores(d, part=scene.scorePart)
                        if scores:
                            score, stars, name, scoreExt = scores[0]
                            try:
                                notesHit, notesTotal, noteStreak, modVersion, handicap, handicapLong, originalScore = scoreExt
                            except ValueError:
                                notesHit, notesTotal, noteStreak, modVersion, oldScores1, oldScores2 = scoreExt
                                handicap = 0
                                handicapLong = "None"
                                originalScore = score
                            break
                        else:
                            score, stars, name = 0, 0, "---"
                    else:
                        score, stars, name = _("Nil"), 0, "---"





                starx = self.song_listscore_xpos + .01
                stary = .0925 * (n + 1)-0.039
                starscale = 0.03
                stary = 1.0 - (stary / scene.fontScreenBottom)
                scene.drawStarScore(w, h, starx, stary - h / 2, stars, starscale, horiz_spacing=1.0, hqStar=True) #MFH

                scale = 0.0014
                # evilynux - score color
                c1, c2, c3 = self.songlist_score_color
                glColor3f(c1, c2, c3)
                # evilynux - hit% and note streak only if enabled
                if score is not _("Nil") and score > 0 and notesTotal != 0:
                    text = "%.1f%% (%d)" % ((float(notesHit) / notesTotal) * 100.0, noteStreak)
                    lfont.render(text, (self.song_listscore_xpos + .1, .0925 * (n + 1)-.015), scale=scale, align=2)

                text = str(score)
                lfont.render(text, (self.song_listscore_xpos + .1, .0925 * (n + 1) + .0125), scale=scale * 1.28, align=2)

        elif self.setlist_type == 2: #old list/cd
            y = h * (.87-(.1 * n))
            if not scene.items:
                return
            item = scene.items[i]
            if isinstance(item, Song.SongInfo) or isinstance(item, Song.RandomSongInfo):
                c1, c2, c3 = self.song_name_text_color
                glColor4f(c1, c2, c3, 1)
            if isinstance(item, Song.LibraryInfo):
                c1, c2, c3 = self.library_text_color
                glColor4f(c1, c2, c3, 1)
            if isinstance(item, Song.TitleInfo) or isinstance(item, Song.SortTitleInfo):
                c1, c2, c3 = self.career_title_color
                glColor4f(c1, c2, c3, 1)
            text = item.name
            if isinstance(item, Song.SongInfo) and item.getLocked():
                text = _("-- Locked --")
            if isinstance(item, Song.SongInfo): #MFH - add indentation when tier sorting
                if scene.tiersPresent:
                    text = "    " + text
            if isinstance(item, Song.TitleInfo) or isinstance(item, Song.SortTitleInfo):
                text = string.upper(text)
            scale = font.scaleText(text, maxwidth=0.45)
            font.render(text, (self.song_listcd_list_xpos, .09 * (n + 1)), scale=scale)
            if isinstance(item, Song.SongInfo) and not item.getLocked():
                if not item.frets == "":
                    suffix = ", (" + item.frets + ")"
                else:
                    suffix = ""

                if not item.year == "":
                    yeartag = ", " + item.year
                else:
                    yeartag = ""

                scale = .0014
                c1, c2, c3 = self.artist_text_color
                glColor4f(c1, c2, c3, 1)

                text = string.upper(item.artist) + suffix + yeartag

                scale = font.scaleText(text, maxwidth=0.4, scale=scale)
                font.render(text, (self.song_listcd_list_xpos + .05, .09 * (n + 1) + .05), scale=scale)
        elif self.setlist_type == 3: #old rb2
            font = scene.fontDict['songListFont']
            if not scene.items or scene.itemIcons is None:
                return
            item = scene.items[i]
            y = h * (.7825-(.0459 * (n + 1)))

            if scene.img_tier:
                imgwidth = scene.img_tier.width1()
                imgheight = scene.img_tier.height1()
                wfactor = 381.1 / imgwidth
                hfactor = 24.000 / imgheight
                if isinstance(item, Song.TitleInfo) or isinstance(item, Song.SortTitleInfo) and scene.img_tier:
                    scene.drawImage(scene.img_tier, scale=(wfactor, -hfactor), coord=(w / 1.587, h-((0.055 * h) * (n + 1))-(0.219 * h)))

            icon = None
            if isinstance(item, Song.SongInfo):
                if item.icon != "":
                    try:
                        icon = scene.itemIcons[item.icon]
                        imgwidth = icon.width1()
                        wfactor = 23.000 / imgwidth
                        scene.drawImage(icon, scale=(wfactor, -wfactor), coord=(w / 2.86, h-((0.055 * h) * (n + 1))-(0.219 * h)))
                    except KeyError:
                        pass
            elif isinstance(item, Song.LibraryInfo):
                try:
                    icon = scene.itemIcons["Library"]
                    imgwidth = icon.width1()
                    wfactor = 23.000 / imgwidth
                    scene.drawImage(icon, scale=(wfactor, -wfactor), coord=(w / 2.86, h-((0.055 * h) * (n + 1))-(0.219 * h)))
                except KeyError:
                    pass
            elif isinstance(item, Song.RandomSongInfo):
                try:
                    icon = scene.itemIcons["Random"]
                    imgwidth = icon.width1()
                    wfactor = 23.000 / imgwidth
                    scene.drawImage(icon, scale=(wfactor, -wfactor), coord=(w / 2.86, h-((0.055 * h) * (n + 1))-(0.219 * h)))
                except KeyError:
                    pass

            if isinstance(item, Song.SongInfo) or isinstance(item, Song.LibraryInfo):
                c1, c2, c3 = self.song_name_text_color
                glColor4f(c1, c2, c3, 1)
            elif isinstance(item, Song.TitleInfo) or isinstance(item, Song.SortTitleInfo):
                c1, c2, c3 = self.career_title_color
                glColor4f(c1, c2, c3, 1)
            elif isinstance(item, Song.RandomSongInfo):
                c1, c2, c3 = self.song_name_text_color
                glColor4f(c1, c2, c3, 1)

            text = item.name


            if isinstance(item, Song.SongInfo) and item.getLocked():
                text = _("-- Locked --")

            if isinstance(item, Song.SongInfo): #MFH - add indentation when tier sorting
                if scene.tiersPresent or icon:
                    text = "    " + text


            # evilynux - Force uppercase display for Career titles
            maxwidth = .55

            if isinstance(item, Song.TitleInfo) or isinstance(item, Song.SortTitleInfo):
                text = string.upper(text)

            scale = .0015
            wt, ht = font.getStringSize(text, scale=scale)

            while wt > maxwidth:
                tlength = len(text) - 4
                text = text[:tlength] + "..."
                wt, ht = font.getStringSize(text, scale=scale)
                if wt < .45:
                    break


            font.render(text, (.35, .0413 * (n + 1) + .15), scale=scale)

            if isinstance(item, Song.SongInfo):
                if not item.getLocked():
                    try:
                        difficulties = item.partDifficulties[scene.scorePart.id]
                    except KeyError:
                        difficulties = []
                    for d in difficulties:
                        if d.id == scene.scoreDifficulty.id:
                            scores = item.getHighscores(d, part=scene.scorePart)
                            if scores:
                                score, stars, name, scoreExt = scores[0]
                                try:
                                    notesHit, notesTotal, noteStreak, modVersion, handicap, handicapLong, originalScore = scoreExt
                                except ValueError:
                                    notesHit, notesTotal, noteStreak, modVersion, oldScores1, oldScores2 = scoreExt
                                    handicap = 0
                                    handicapLong = "None"
                                    originalScore = score
                                break
                            else:
                                score, stars, name = 0, 0, "---"
                    else:
                        score, stars, name = _("Nil"), 0, "---"

                    if score == _("Nil") and scene.nilShowNextScore:   #MFH
                        for d in difficulties:   #MFH - just take the first valid difficulty you can find and display it.
                            scores = item.getHighscores(d, part=scene.scorePart)
                            if scores:
                                score, stars, name, scoreExt = scores[0]
                                try:
                                    notesHit, notesTotal, noteStreak, modVersion, handicap, handicapLong, originalScore = scoreExt
                                except ValueError:
                                    notesHit, notesTotal, noteStreak, modVersion, oldScores1, oldScores2 = scoreExt
                                    handicap = 0
                                    handicapLong = "None"
                                    originalScore = score
                                break
                            else:
                                score, stars, name = 0, 0, "---"
                        else:
                            score, stars, name = _("Nil"), 0, "---"

                    #evilynux - hit% and note streak if enabled
                    scale = 0.0009
                    if score is not _("Nil") and score > 0 and notesTotal != 0:
                        text = "%.1f%% (%d)" % ((float(notesHit) / notesTotal) * 100.0, noteStreak)
                        font.render(text, (.92, .0413 * (n + 1) + .163), scale=scale, align=2)

                    text = str(score)

                    font.render(text, (.92, .0413 * (n + 1) + .15), scale=scale, align=2)

    def renderSelectedItem(self, scene, n):
        w, h = scene.geometry
        font = scene.fontDict['songListFont']
        lfont = scene.fontDict['songListFont']
        sfont = scene.fontDict['shadowfont']
        item = scene.selectedItem
        if not item:
            return
        if isinstance(item, Song.BlankSpaceInfo):
            return
        if self.setlist_type == 0:
            return
        elif self.setlist_type == 1:
            y = h * (.88-(.125 * n))
            if scene.img_item_select:
                wfactor = scene.img_item_select.widthf(pixelw=635.000)
                scene.drawImage(scene.img_item_select, scale=(wfactor, -wfactor), coord=(w / 2.1, y))
            glColor4f(0, 0, 0, 1)
            if isinstance(item, Song.SongInfo) or isinstance(item, Song.RandomSongInfo):
                c1, c2, c3 = self.song_name_selected_color
                glColor3f(c1, c2, c3)
            elif isinstance(item, Song.LibraryInfo):
                c1, c2, c3 = self.library_selected_color
                glColor3f(c1, c2, c3)
            elif isinstance(item, Song.TitleInfo) or isinstance(item, Song.SortTitleInfo):
                c1, c2, c3 = self.career_title_color
                glColor3f(c1, c2, c3)

            text = item.name

            if isinstance(item, Song.SongInfo) and item.getLocked(): #TODO: SongDB
                text = _("-- Locked --")

            if isinstance(item, Song.SongInfo): #MFH - add indentation when tier sorting
                if scene.tiersPresent:
                    text = "    " + text

            if isinstance(item, Song.TitleInfo) or isinstance(item, Song.SortTitleInfo):
                text = string.upper(text)

            scale = sfont.scaleText(text, maxwidth=0.440)

            sfont.render(text, (self.song_list_xpos, .0925 * (n + 1)-.0375), scale=scale)


            #MFH - Song list score / info display:
            if isinstance(item, Song.SongInfo) and not item.getLocked():
                scale = 0.0009
                text = scene.scoreDifficulty.text
                c1, c2, c3 = self.songlist_score_color
                glColor3f(c1, c2, c3)
                lfont.render(text, (self.song_listscore_xpos, .0925 * (n + 1)-.034), scale=scale, align=2)
                if not item.frets == "":
                    suffix = ", (" + item.frets + ")"
                else:
                    suffix = ""

                if not item.year == "":
                    yeartag = ", " + item.year
                else:
                    yeartag = ""


                scale = .0014
                c1, c2, c3 = self.artist_selected_color
                glColor3f(c1, c2, c3)

                # evilynux - Force uppercase display for artist name
                text = string.upper(item.artist) + suffix + yeartag

                # evilynux - automatically scale artist name and year
                scale = lfont.scaleText(text, maxwidth=0.440, scale=scale)
                if scale > .0014:
                    scale = .0014

                lfont.render(text, (self.song_list_xpos + .05, .0925 * (n + 1) + .0125), scale=scale)

                score = _("Nil")
                stars = 0
                name = ""

                try:
                    difficulties = item.partDifficulties[scene.scorePart.id]
                except KeyError:
                    difficulties = []
                for d in difficulties:
                    if d.id == scene.scoreDifficulty.id:
                        scores = item.getHighscores(d, part=scene.scorePart)
                        if scores:
                            score, stars, name, scoreExt = scores[0]
                            try:
                                notesHit, notesTotal, noteStreak, modVersion, handicap, handicapLong, originalScore = scoreExt
                            except ValueError:
                                notesHit, notesTotal, noteStreak, modVersion, oldScores1, oldScores2 = scoreExt
                                handicap = 0
                                handicapLong = "None"
                                originalScore = score
                        else:
                            score, stars, name = 0, 0, "---"

                if score == _("Nil") and scene.nilShowNextScore:   #MFH
                    for d in difficulties:   #MFH - just take the first valid difficulty you can find and display it.
                        scores = item.getHighscores(d, part=scene.scorePart)
                        if scores:
                            score, stars, name, scoreExt = scores[0]
                            try:
                                notesHit, notesTotal, noteStreak, modVersion, handicap, handicapLong, originalScore = scoreExt
                            except ValueError:
                                notesHit, notesTotal, noteStreak, modVersion, oldScores1, oldScores2 = scoreExt
                                handicap = 0
                                handicapLong = "None"
                                originalScore = score
                            break
                        else:
                            score, stars, name = 0, 0, "---"
                    else:
                        score, stars, name = _("Nil"), 0, "---"

                starx = self.song_listscore_xpos + .01
                stary = .0925 * (n + 1)-0.039
                starscale = 0.03
                stary = 1.0 - (stary / scene.fontScreenBottom)
                scene.drawStarScore(w, h, starx, stary - h / 2, stars, starscale, horiz_spacing=1.0, hqStar=True) #MFH

                scale = 0.0014
                # evilynux - score color
                c1, c2, c3 = self.songlist_score_color
                glColor3f(c1, c2, c3)
                # evilynux - hit% and note streak only if enabled
                if score is not _("Nil") and score > 0 and notesTotal != 0:
                    text = "%.1f%% (%d)" % ((float(notesHit) / notesTotal) * 100.0, noteStreak)
                    lfont.render(text, (self.song_listscore_xpos + .1, .0925 * (n + 1)-.015), scale=scale, align=2)

                text = str(score)
                lfont.render(text, (self.song_listscore_xpos + .1, .0925 * (n + 1) + .0125), scale=scale * 1.28, align=2)
        elif self.setlist_type == 2:
            y = h * (.87-(.1 * n))
            glColor4f(1, 1, 1, 1)
            if scene.img_selected:
                imgwidth = scene.img_selected.width1()
                scene.drawImage(scene.img_selected, scale=(1, -1), coord=(self.song_listcd_list_xpos * w + (imgwidth * .64 / 2), y * 1.2-h * .215))
            text = scene.library
            font.render(text, (.05, .01))
            if scene.songLoader:
                font.render(_("Loading Preview..."), (.05, .7), scale=0.001)

            if isinstance(item, Song.SongInfo):
                c1, c2, c3 = self.song_name_selected_color
                glColor4f(c1, c2, c3, 1)
                if item.getLocked():
                    text = item.getUnlockText()
                elif scene.careerMode and not item.completed:
                    text = _("Play To Advance")
                elif scene.practiceMode:
                    text = _("Practice")
                elif item.count:
                    count = int(item.count)
                    if count == 1: 
                        text = _("Played Once")
                    else:
                        text = _("Played %d times.") % count
                else:
                    text = _("Quickplay")
            elif isinstance(item, Song.LibraryInfo):
                c1, c2, c3 = self.library_selected_color
                glColor4f(c1, c2, c3, 1)
                if item.songCount == 1:
                    text = _("There Is 1 Song In This Setlist.")
                elif item.songCount > 1:
                    text = _("There Are %d Songs In This Setlist.") % (item.songCount)
                else:
                    text = ""
            elif isinstance(item, Song.TitleInfo) or isinstance(item, Song.SortTitleInfo):
                text = _("Tier")
                c1, c2, c3 = self.career_title_color
                glColor4f(c1, c2, c3, 1)
            elif isinstance(item, Song.RandomSongInfo):
                text = _("Random Song")
                c1, c2, c3 = self.song_name_selected_color
                glColor4f(c1, c2, c3, 1)

            font.render(text, (self.song_listcd_score_xpos, .085), scale=0.0012)

            if isinstance(item, Song.SongInfo) or isinstance(item, Song.RandomSongInfo):
                c1, c2, c3 = self.song_name_selected_color
                glColor4f(c1, c2, c3, 1)
            elif isinstance(item, Song.LibraryInfo):
                c1, c2, c3 = self.library_selected_color
                glColor4f(c1, c2, c3, 1)
            elif isinstance(item, Song.TitleInfo) or isinstance(item, Song.SortTitleInfo):
                c1, c2, c3 = self.career_title_color
                glColor4f(c1, c2, c3, 1)
            text = item.name
            if isinstance(item, Song.SongInfo) and item.getLocked():
                text = _("-- Locked --")

            if isinstance(item, Song.SongInfo): #MFH - add indentation when tier sorting
                if scene.tiersPresent:
                    text = "    " + text

            elif isinstance(item, Song.TitleInfo) or isinstance(item, Song.SortTitleInfo):
                text = string.upper(text)

            scale = font.scaleText(text, maxwidth=0.45)
            font.render(text, (self.song_listcd_list_xpos, .09 * (n + 1)), scale=scale)

            if isinstance(item, Song.SongInfo) and not item.getLocked():
                if not item.frets == "":
                    suffix = ", (" + item.frets + ")"
                else:
                    suffix = ""

                if not item.year == "":
                    yeartag = ", " + item.year
                else:
                    yeartag = ""

                scale = .0014
                c1, c2, c3 = self.artist_selected_color
                glColor4f(c1, c2, c3, 1)
                text = string.upper(item.artist) + suffix + yeartag

                scale = font.scaleText(text, maxwidth=0.4, scale=scale)
                font.render(text, (self.song_listcd_list_xpos + .05, .09 * (n + 1) + .05), scale=scale)

        elif self.setlist_type == 3:
            y = h * (.7825-(.0459 * (n)))

            if scene.img_tier:
                imgwidth = scene.img_tier.width1()
                imgheight = scene.img_tier.height1()
                wfactor = 381.1 / imgwidth
                hfactor = 24.000 / imgheight
                if isinstance(item, Song.TitleInfo) or isinstance(item, Song.SortTitleInfo):
                    scene.drawImage(scene.img_tier, scale=(wfactor, -hfactor), coord=(w / 1.587, h-((0.055 * h) * (n + 1))-(0.219 * h)))

            if scene.img_selected:
                imgwidth = scene.img_selected.width1()
                imgheight = scene.img_selected.height1()
                wfactor = 381.5 / imgwidth
                hfactor = 36.000 / imgheight

                scene.drawImage(scene.img_selected, scale=(wfactor, -hfactor), coord=(w / 1.587, y * 1.2-h * .213))


            icon = None
            if isinstance(item, Song.SongInfo):
                if item.icon != "":
                    try:
                        icon = scene.itemIcons[item.icon]
                        imgwidth = icon.width1()
                        wfactor = 23.000 / imgwidth
                        scene.drawImage(icon, scale=(wfactor, -wfactor), coord=(w / 2.86, h-((0.055 * h) * (n + 1))-(0.219 * h)))
                    except KeyError:
                        pass

                c1, c2, c3 = self.song_name_selected_color
                glColor3f(c1, c2, c3)
                if item.getLocked():
                    text = item.getUnlockText()
                elif scene.careerMode and not item.completed:
                    text = _("Play To Advance")
                elif scene.practiceMode:
                    text = _("Practice")
                elif item.count:
                    count = int(item.count)
                    if count == 1: 
                        text = _("Played Once")
                    else:
                        text = _("Played %d times.") % count
                else:
                    text = _("Quickplay")
            elif isinstance(item, Song.LibraryInfo):
                try:
                    icon = scene.itemIcons["Library"]
                    imgwidth = icon.width1()
                    wfactor = 23.000 / imgwidth
                    scene.drawImage(icon, scale=(wfactor, -wfactor), coord=(w / 2.86, h-((0.055 * h) * (n + 1))-(0.219 * h)))
                except KeyError:
                    pass
                c1, c2, c3 = self.library_selected_color
                glColor3f(c1, c2, c3)
                if item.songCount == 1:
                    text = _("There Is 1 Song In This Setlist.")
                elif item.songCount > 1:
                    text = _("There Are %d Songs In This Setlist.") % (item.songCount)
                else:
                    text = ""
            elif isinstance(item, Song.TitleInfo) or isinstance(item, Song.SortTitleInfo):
                text = _("Tier")
                c1, c2, c3 = self.career_title_color
                glColor3f(c1, c2, c3)
            elif isinstance(item, Song.RandomSongInfo):
                try:
                    icon = scene.itemIcons["Random"]
                    imgwidth = icon.width1()
                    wfactor = 23.000 / imgwidth
                    scene.drawImage(icon, scale=(wfactor, -wfactor), coord=(w / 2.86, h-((0.055 * h) * (n + 1))-(0.219 * h)))
                except KeyError:
                    pass
                text = _("Random Song")
                c1, c2, c3 = self.career_title_color
                glColor3f(c1, c2, c3)

            font.render(text, (0.92, .13), scale=0.0012, align=2)

            maxwidth = .45
            if isinstance(item, Song.SongInfo) or isinstance(item, Song.LibraryInfo) or isinstance(item, Song.RandomSongInfo):
                c1, c2, c3 = self.song_name_selected_color
                glColor4f(c1, c2, c3, 1)
            if isinstance(item, Song.TitleInfo) or isinstance(item, Song.SortTitleInfo):
                c1, c2, c3 = self.career_title_color
                glColor4f(c1, c2, c3, 1)

            text = item.name

            if isinstance(item, Song.SongInfo) and item.getLocked():
                text = _("-- Locked --")

            if isinstance(item, Song.SongInfo): #MFH - add indentation when tier sorting
                if scene.tiersPresent or icon:
                    text = "    " + text


            # evilynux - Force uppercase display for Career titles
            if isinstance(item, Song.TitleInfo) or isinstance(item, Song.SortTitleInfo):
                maxwidth = .55
                text = string.upper(text)

            scale = .0015
            wt, ht = font.getStringSize(text, scale=scale)

            while wt > maxwidth:
                tlength = len(text) - 4
                text = text[:tlength] + "..."
                wt, ht = font.getStringSize(text, scale=scale)
                if wt < .45:
                    break


            font.render(text, (.35, .0413 * (n + 1) + .15), scale=scale) #add theme option for song_listCD_xpos

            if isinstance(item, Song.SongInfo):
                if not item.getLocked():
                    try:
                        difficulties = item.partDifficulties[scene.scorePart.id]
                    except KeyError:
                        difficulties = []
                    for d in difficulties:
                        if d.id == scene.scoreDifficulty.id:
                            scores = item.getHighscores(d, part=scene.scorePart)
                            if scores:
                                score, stars, name, scoreExt = scores[0]
                                try:
                                    notesHit, notesTotal, noteStreak, modVersion, handicap, handicapLong, originalScore = scoreExt
                                except ValueError:
                                    notesHit, notesTotal, noteStreak, modVersion, oldScores1, oldScores2 = scoreExt
                                    handicap = 0
                                    handicapLong = "None"
                                    originalScore = score
                                break
                            else:
                                score, stars, name = 0, 0, "---"
                    else:
                        score, stars, name = _("Nil"), 0, "---"
                    if score == _("Nil") and scene.nilShowNextScore:   #MFH
                        for d in difficulties:   #MFH - just take the first valid difficulty you can find and display it.
                            scores = item.getHighscores(d, part=scene.scorePart)
                            if scores:
                                score, stars, name, scoreExt = scores[0]
                                try:
                                    notesHit, notesTotal, noteStreak, modVersion, handicap, handicapLong, originalScore = scoreExt
                                except ValueError:
                                    notesHit, notesTotal, noteStreak, modVersion, oldScores1, oldScores2 = scoreExt
                                    handicap = 0
                                    handicapLong = "None"
                                    originalScore = score
                                break
                            else:
                                score, stars, name = 0, 0, "---"
                        else:
                            score, stars, name = _("Nil"), 0, "---"

                    scale = 0.0009
                    if score is not _("Nil") and score > 0 and notesTotal != 0:
                        text = "%.1f%% (%d)" % ((float(notesHit) / notesTotal) * 100.0, noteStreak)
                        w, h = font.getStringSize(text, scale=scale)
                        font.render(text, (.92, .0413 * (n + 1) + .163), scale=scale, align=2)

                    text = str(score)

                    font.render(text, (.92, .0413 * (n + 1) + .15), scale=scale, align=2)

    def renderItem(self, scene, color, label):
        if not scene.itemMesh:
            return
        if color:
            glColor3f(*color)
        glEnable(GL_COLOR_MATERIAL)
        if self.setlist_type == 2:
            glRotate(90, 0, 0, 1)
            glRotate(((scene.time - scene.lastTime) * 2 % 360) - 90, 1, 0, 0)
        scene.itemMesh.render("Mesh_001")
        glColor3f(.1, .1, .1)
        scene.itemMesh.render("Mesh")
        if label and scene.label:
            glEnable(GL_TEXTURE_2D)
            label.bind()
            glColor3f(1, 1, 1)
            glMatrixMode(GL_TEXTURE)
            glScalef(1, -1, 1)
            glMatrixMode(GL_MODELVIEW)
            scene.label.render("Mesh_001")
            glMatrixMode(GL_TEXTURE)
            glLoadIdentity()
            glMatrixMode(GL_MODELVIEW)
            glDisable(GL_TEXTURE_2D)
            if shaders.enable("cd"):
                scene.itemMesh.render("Mesh_001")
                shaders.disable()

    def renderLibrary(self, scene, color, label):
        if not scene.libraryMesh:
            return
        if color:
            glColor3f(*color)

        glEnable(GL_NORMALIZE)
        glEnable(GL_COLOR_MATERIAL)
        if self.setlist_type == 2:
            glRotate(-180, 0, 1, 0)
            glRotate(-90, 0, 0, 1)
            glRotate(((scene.time - scene.lastTime) * 4 % 360) - 90, 1, 0, 0)
        scene.libraryMesh.render("Mesh_001")
        glColor3f(.1, .1, .1)
        scene.libraryMesh.render("Mesh")

        # Draw the label if there is one
        if label and scene.libraryLabel:
            glEnable(GL_TEXTURE_2D)
            label.bind()
            glColor3f(1, 1, 1)
            glMatrixMode(GL_TEXTURE)
            glScalef(1, -1, 1)
            glMatrixMode(GL_MODELVIEW)
            scene.libraryLabel.render()
            glMatrixMode(GL_TEXTURE)
            glLoadIdentity()
            glMatrixMode(GL_MODELVIEW)
            glDisable(GL_TEXTURE_2D)
        glDisable(GL_NORMALIZE)

    def renderTitle(self, scene, color, label):
        if not scene.tierMesh:
            return

        if color:
            glColor3f(*color)

        glEnable(GL_NORMALIZE)
        glEnable(GL_COLOR_MATERIAL)
        scene.tierMesh.render("Mesh_001")
        glColor3f(.1, .1, .1)
        scene.tierMesh.render("Mesh")

        # Draw the label if there is one
        if label:
            glEnable(GL_TEXTURE_2D)
            label.bind()
            glColor3f(1, 1, 1)
            glMatrixMode(GL_TEXTURE)
            glScalef(1, -1, 1)
            glMatrixMode(GL_MODELVIEW)
            scene.libraryLabel.render()
            glMatrixMode(GL_TEXTURE)
            glLoadIdentity()
            glMatrixMode(GL_MODELVIEW)
            glDisable(GL_TEXTURE_2D)
        glDisable(GL_NORMALIZE)

    def renderRandom(self, scene, color, label):
        if not scene.itemMesh:
            return

        if color:
            glColor3f(*color)

        glEnable(GL_NORMALIZE)
        glEnable(GL_COLOR_MATERIAL)
        scene.itemMesh.render("Mesh_001")
        glColor3f(.1, .1, .1)
        scene.itemMesh.render("Mesh")

        # Draw the label if there is one
        if label:
            glEnable(GL_TEXTURE_2D)
            label.bind()
            glColor3f(1, 1, 1)
            glMatrixMode(GL_TEXTURE)
            glScalef(1, -1, 1)
            glMatrixMode(GL_MODELVIEW)
            scene.libraryLabel.render()
            glMatrixMode(GL_TEXTURE)
            glLoadIdentity()
            glMatrixMode(GL_MODELVIEW)
            glDisable(GL_TEXTURE_2D)
        glDisable(GL_NORMALIZE)

    def renderAlbumArt(self, scene):
        if not scene.itemLabels:
            return
        if self.setlist_type == 0:
            w, h = scene.geometry
            try:
                glMatrixMode(GL_PROJECTION)
                glPushMatrix()
                glLoadIdentity()
                gluPerspective(60, scene.aspectRatio, 0.1, 1000)

                glMatrixMode(GL_MODELVIEW)
                glLoadIdentity()

                glEnable(GL_DEPTH_TEST)
                glDisable(GL_CULL_FACE)
                glDepthMask(1)

                offset = 0
                if scene.time < 40:
                    offset = 10 * ((40 - scene.time) / 40.0) ** 4
                scene.camera.origin = (-10 + offset, -scene.cameraOffset, 4   - self.song_cd_xpos + offset)
                scene.camera.target = (0 + offset, -scene.cameraOffset, 2.5 - self.song_cd_xpos + offset)
                scene.camera.apply()

                y = 0.0
                for i, item in enumerate(scene.items):
                    c = math.sin(scene.itemRenderAngles[i] * math.pi / 180)

                    if isinstance(item, Song.SongInfo):
                        h = c * 4.0 + (1 - c) * .8
                    elif isinstance(item, Song.LibraryInfo):
                        h = c * 4.0 + (1 - c) * 1.2
                    elif isinstance(item, Song.TitleInfo) or isinstance(item, Song.SortTitleInfo):
                        h = c * 4.0 + (1 - c) * 2.4
                    elif isinstance(item, Song.RandomSongInfo):
                        h = c * 4.0 + (1 - c) * .8
                    else:
                        continue

                    d = (y + h * .5 + scene.camera.origin[1]) / (4 * (scene.camera.target[2] - scene.camera.origin[2]))
                    if i == scene.selectedIndex:
                        scene.selectedOffset = y + h / 2
                        self.theme.setSelectedColor()
                    else:
                        self.theme.setBaseColor()

                    glTranslatef(0, -h / 2, 0)
                    glPushMatrix()
                    if abs(d) < 1.2:
                        label = scene.itemLabels[i]
                        if label == "Random":
                            label = scene.img_random_label
                        if label == False:
                            label = scene.img_empty_label
                        if isinstance(item, Song.SongInfo):
                            glRotate(scene.itemRenderAngles[i], 0, 0, 1)
                            self.renderItem(scene, item.cassetteColor, label)
                        elif isinstance(item, Song.LibraryInfo):
                            #myfingershurt: cd cases are backwards
                            glRotate(-scene.itemRenderAngles[i], 0, 1, 0)    #spin 90 degrees around y axis
                            glRotate(-scene.itemRenderAngles[i], 0, 1, 0)    #spin 90 degrees around y axis again, now case is corrected
                            glRotate(-scene.itemRenderAngles[i], 0, 0, 1)    #bring cd case up for viewing
                            if i == scene.selectedIndex:
                                glRotate(((scene.time - scene.lastTime) * 4 % 360) - 90, 1, 0, 0)
                            self.renderLibrary(scene, item.color, label)
                        elif isinstance(item, Song.TitleInfo):
                            #myfingershurt: cd cases are backwards
                            glRotate(-scene.itemRenderAngles[i], 0, 0.5, 0)    #spin 90 degrees around y axis
                            glRotate(-scene.itemRenderAngles[i], 0, 0.5, 0)    #spin 90 degrees around y axis again, now case is corrected
                            glRotate(-scene.itemRenderAngles[i], 0, 0, 0.5)    #bring cd case up for viewing
                            if i == scene.selectedIndex:
                                glRotate(((scene.time - scene.lastTime) * 4 % 360) - 90, 1, 0, 0)
                            self.renderTitle(scene, item.color, label)
                        elif isinstance(item, Song.RandomSongInfo):
                            #myfingershurt: cd cases are backwards
                            glRotate(scene.itemRenderAngles[i], 0, 0, 1)
                            self.renderRandom(scene, item.color, label)
                    glPopMatrix()

                    glTranslatef(0, -h / 2, 0)
                    y += h
                glDisable(GL_DEPTH_TEST)
                glDisable(GL_CULL_FACE)
                glDepthMask(0)
            finally:
                glMatrixMode(GL_PROJECTION)
                glPopMatrix()
                glMatrixMode(GL_MODELVIEW)

        elif self.setlist_type == 1:
            return
        elif self.setlist_type == 2:
            w, h = scene.geometry
            try:
                glMatrixMode(GL_PROJECTION)
                glPushMatrix()

                glLoadIdentity()
                gluPerspective(60, scene.aspectRatio, 0.1, 1000)
                glMatrixMode(GL_MODELVIEW)
                glLoadIdentity()

                glEnable(GL_DEPTH_TEST)
                glDisable(GL_CULL_FACE)
                glDepthMask(1)

                offset = 0
                if scene.time < 40:
                    offset = 10 * ((40 - scene.time) / 40.0) ** 4
                scene.camera.origin = (-9, (5.196 / scene.aspectRatio) - (5.196 * 2 / scene.aspectRatio) * self.song_listcd_cd_ypos, (5.196 * scene.aspectRatio)-(5.196 * 2 * scene.aspectRatio) * self.song_listcd_cd_xpos)
                scene.camera.target = (0, (5.196 / scene.aspectRatio) - (5.196 * 2 / scene.aspectRatio) * self.song_listcd_cd_ypos, (5.196 * scene.aspectRatio)-(5.196 * 2 * scene.aspectRatio) * self.song_listcd_cd_xpos)
                scene.camera.apply()

                y = 0.0



                glPushMatrix()
                item = scene.selectedItem
                i = scene.selectedIndex
                label = scene.itemLabels[i]
                if label == "Random":
                    label = scene.img_random_label
                if not label:
                    label = scene.img_empty_label
                if isinstance(item, Song.SongInfo):
                    if scene.labelType:
                        self.renderItem(scene, item.cassetteColor, label)
                    else:
                        self.renderLibrary(scene, item.cassetteColor, label)
                elif isinstance(item, Song.LibraryInfo):
                    self.renderLibrary(scene, item.color, label)
                elif isinstance(item, Song.RandomSongInfo):
                    if scene.labelType:
                        self.renderItem(scene, None, label)
                    else:
                        self.renderLibrary(scene, None, label)
                glPopMatrix()

                glTranslatef(0, -h / 2, 0)
                y += h

                glDisable(GL_DEPTH_TEST)
                glDisable(GL_CULL_FACE)
                glDepthMask(0)
            finally:
                glMatrixMode(GL_PROJECTION)
                glPopMatrix()
                glMatrixMode(GL_MODELVIEW)

            #resets the rendering
            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()
            viewport = glGetIntegerv(GL_VIEWPORT)
            w = viewport[2] - viewport[0]
            h = viewport[3] - viewport[1]
            h *= (float(w) / float(h)) / (4.0 / 3.0)
            glOrtho(0, 1, h / w, 0, -100, 100)
            glMatrixMode(GL_MODELVIEW)
            glLoadIdentity()

            glEnable(GL_BLEND)
            glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
            glEnable(GL_COLOR_MATERIAL)
            self.theme.setBaseColor(1)
        elif self.setlist_type == 3:
            w, h = scene.geometry
            item  = scene.items[scene.selectedIndex]
            i = scene.selectedIndex
            img = None
            lockImg = None
            if scene.itemLabels[i] == "Random":
                if scene.img_random_label:
                    img = scene.img_random_label
                    imgwidth = img.width1()
                    wfactor = 155.000 / imgwidth
                elif scene.img_empty_label:
                    img = scene.img_empty_label
                    imgwidth = img.width1()
                    wfactor = 155.000 / imgwidth
            elif not scene.itemLabels[i]:
                if scene.img_empty_label != None:
                    imgwidth = scene.img_empty_label.width1()
                    wfactor = 155.000 / imgwidth
                    img = scene.img_empty_label
            elif scene.itemLabels[i]:
                img = scene.itemLabels[i]
                imgwidth = img.width1()
                wfactor = 155.000 / imgwidth
            if isinstance(item, Song.SongInfo) and item.getLocked():
                if scene.img_locked_label:
                    imgwidth = scene.img_locked_label.width1()
                    wfactor2 = 155.000 / imgwidth
                    lockImg = scene.img_locked_label
                elif scene.img_empty_label:
                    imgwidth = scene.img_empty_label.width1()
                    wfactor = 155.000 / imgwidth
                    img = scene.img_empty_label
            if img:
                scene.drawImage(img, scale=(wfactor, -wfactor), coord=(.21 * w, .59 * h))
            if lockImg:
                scene.drawImage(lockImg, scale=(wfactor2, -wfactor2), coord=(.21 * w, .59 * h))

    def renderForeground(self, scene):
        font = scene.fontDict['songListFont']
        w, h = scene.geometry
        if self.setlist_type == 2:
            text = scene.scorePart.text
            scale = 0.00250
            glColor3f(1, 1, 1)
            font.render(text, (0.95, 0.000), scale=scale, align=2)
        elif self.setlist_type == 3:
            font = scene.fontDict['songListFont']

            c1, c2, c3 = self.song_rb2_diff_color
            glColor3f(c1, c2, c3)

            font.render(_("DIFFICULTY"), (.095, .5325), scale=0.0018)
            scale = 0.0014
            text = _("BAND")
            font.render(text, (.17, .5585), scale=scale, align=2)
            text = _("GUITAR")
            font.render(text, (.17, .5835), scale=scale, align=2)
            text = _("DRUM")
            font.render(text, (.17, .6085), scale=scale, align=2)
            text = _("BASS")
            font.render(text, (.17, .6335), scale=scale, align=2)
            text = _("VOCALS")
            font.render(text, (.17, .6585), scale=scale, align=2)

            #Add support for lead and rhythm diff

            #Qstick - Sorting Text
            text = _("SORTING:") + "     "
            if scene.sortOrder == 0: #title
                text = text + _("ALPHABETICALLY BY TITLE")
            elif scene.sortOrder == 1: #artist
                text = text + _("ALPHABETICALLY BY ARTIST")
            elif scene.sortOrder == 2: #timesplayed
                text = text + _("BY PLAY COUNT")
            elif scene.sortOrder == 3: #album
                text = text + _("ALPHABETICALLY BY ALBUM")
            elif scene.sortOrder == 4: #genre
                text = text + _("ALPHABETICALLY BY GENRE")
            elif scene.sortOrder == 5: #year
                text = text + _("BY YEAR")
            elif scene.sortOrder == 6: #Band Difficulty
                text = text + _("BY BAND DIFFICULTY")
            elif scene.sortOrder == 7: #Band Difficulty
                text = text + _("BY INSTRUMENT DIFFICULTY")
            else:
                text = text + _("BY SONG COLLECTION")

            font.render(text, (.13, .152), scale=0.0017)

            if scene.songLoader:
                font.render(_("Loading Preview..."), (.05, .7), scale=0.001)
            return
        if scene.img_list_button_guide:
            scene.drawImage(scene.img_list_button_guide, scale=(.5, -.5), coord=(w * .5, 0), fit=2)
        if scene.songLoader:
            font.render(_("Loading Preview..."), (.5, .7), align=1)
        if scene.searching:
            font.render(scene.searchText, (.5, .7), align=1)
        if scene.img_list_fg:
            scene.drawImage(scene.img_list_fg, scale=(1.0, -1.0), coord=(w / 2, h / 2), stretched=3)

    def renderSelectedInfo(self, scene):
        if self.setlist_type == 0: #note... clean this up. this was a rush job.
            if not scene.selectedItem:
                return
            font = scene.fontDict['font']
            screenw, screenh = scene.geometry
            v = 0
            try:
                lfont = scene.fontDict['lfont']
            except KeyError:
                lfont = font

            # here we reset the rendering... without pushing the matrices. (they be thar)
            # (otherwise copying engine.view.setOrthogonalProjection)
            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()
            viewport = glGetIntegerv(GL_VIEWPORT)
            w = viewport[2] - viewport[0]
            h = viewport[3] - viewport[1]
            h *= (float(w) / float(h)) / (4.0 / 3.0)
            glOrtho(0, 1, h / w, 0, -100, 100)
            glMatrixMode(GL_MODELVIEW)
            glLoadIdentity()

            glEnable(GL_BLEND)
            glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
            glEnable(GL_COLOR_MATERIAL)
            self.theme.setBaseColor(1)

            if scene.songLoader:
                font.render(_("Loading Preview..."), (.05, .7), scale=0.001)

            #x = .6
            x = self.song_cdscore_xpos
            y = .15

            self.theme.setSelectedColor(1)

            c1, c2, c3 = self.song_name_selected_color
            glColor3f(c1, c2, c3)

            item  = scene.selectedItem

            angle = scene.itemRenderAngles[scene.selectedIndex]
            f = ((90.0 - angle) / 90.0) ** 2

            cText = item.name
            if (isinstance(item, Song.SongInfo) and item.getLocked()):
                cText = _("-- Locked --")

            fh = lfont.getHeight() * 0.0016
            lfont.render(cText, (x, y), scale=0.0016)

            if isinstance(item, Song.SongInfo):
                self.theme.setBaseColor(1)

                c1, c2, c3 = self.artist_selected_color
                glColor3f(c1, c2, c3)

                if not item.year == "":
                    yeartag = ", " + item.year
                else:
                    yeartag = ""

                cText = item.artist + yeartag
                if (item.getLocked()):
                    cText = "" # avoid giving away artist of locked song

                # evilynux - Use font w/o outline
                lfont.render(cText, (x, y + fh), scale=0.0016)

                if item.count:
                    self.theme.setSelectedColor(1)

                    c1, c2, c3 = self.song_name_selected_color
                    glColor3f(c1, c2, c3)

                    count = int(item.count)
                    if count == 1: 
                        text = _("Played %d time") % count
                    else:
                        text = _("Played %d times") % count

                    if item.getLocked():
                        text = item.getUnlockText()
                    elif scene.careerMode and not item.completed:
                        text = _("Play To Advance.")
                    font.render(text, (x, y + 2 * fh), scale=0.001)
                else:
                    text = _("Never Played")
                    if item.getLocked():
                        text = item.getUnlockText()
                    elif scene.careerMode and not item.completed:
                        text = _("Play To Advance.")
                    lfont.render(text, (x, y + 3 * fh), scale=0.001)

                self.theme.setSelectedColor(1 - v)

                c1, c2, c3 = self.songlistcd_score_color
                glColor3f(c1, c2, c3)

                scale = 0.0011

                #x = .6
                x = self.song_cdscore_xpos
                y = .42
                try:
                    difficulties = item.partDifficulties[scene.scorePart.id]
                except KeyError:
                    difficulties = []
                if len(difficulties) > 3:
                    y = .42
                elif len(difficulties) == 0:
                    score, stars, name = "---", 0, "---"

                for d in difficulties:
                    scores = item.getHighscores(d, part=scene.scorePart)

                    if scores:
                        score, stars, name, scoreExt = scores[0]
                        try:
                            notesHit, notesTotal, noteStreak, modVersion, handicap, handicapLong, originalScore = scoreExt
                        except ValueError:
                            notesHit, notesTotal, noteStreak, modVersion, oldScores1, oldScores2 = scoreExt
                            handicap = 0
                            handicapLong = "None"
                            originalScore = score
                    else:
                        score, stars, name = "---", 0, "---"
                    self.theme.setBaseColor(1)
                    font.render(Song.difficulties[d.id].text, (x, y), scale=scale)

                    starscale = 0.02
                    stary = 1.0 - y / scene.fontScreenBottom
                    scene.drawStarScore(screenw, screenh, x + .01, stary-2 * fh, stars, starscale, hqStar=True) #volshebnyi

                    self.theme.setSelectedColor(1)
                    # evilynux - Also use hit%/noteStreak SongList option
                    if scores:
                        if notesTotal != 0:
                            score = "%s %.1f%%" % (score, (float(notesHit) / notesTotal) * 100.0)
                        if noteStreak != 0:
                            score = "%s (%d)" % (score, noteStreak)
                    font.render(unicode(score), (x + .15, y), scale=scale)
                    font.render(name, (x + .15, y + fh), scale=scale)
                    y += 2 * fh
            elif isinstance(item, Song.LibraryInfo):
                self.theme.setBaseColor(1)
                c1, c2, c3 = self.library_selected_color

                glColor3f(c1, c2, c3)

                if item.songCount == 1:
                    songCount = _("One Song In This Setlist")
                else:
                    songCount = _("%d Songs In This Setlist") % item.songCount
                font.render(songCount, (x, y + 3 * fh), scale=0.0016)

            elif isinstance(item, Song.RandomSongInfo):
                self.theme.setBaseColor(1 - v)

                c1, c2, c3 = self.song_name_selected_color
                glColor3f(c1, c2, c3)

                font.render(_("(Random Song)"), (x, y + 3 * fh), scale=0.0016)

            #MFH CD list
            text = scene.scorePart.text
            scale = 0.00250
            #glColor3f(1, 1, 1)
            c1, c2, c3 = self.song_name_selected_color
            glColor3f(c1, c2, c3)
            w, h = font.getStringSize(text, scale=scale)
            font.render(text, (0.95-w, 0.000), scale=scale)
            # finally:
                # pass
        elif self.setlist_type == 1:
            return
        elif self.setlist_type == 2:
            if not scene.selectedItem:
                return
            item = scene.selectedItem
            font = scene.fontDict['font']
            w, h = scene.geometry
            try:
                lfont = scene.fontDict['lfont']
            except KeyError:
                lfont = font
            fh = lfont.getHeight() * 0.0016
            if isinstance(item, Song.SongInfo):
                angle = scene.itemRenderAngles[scene.selectedIndex]
                f = ((90.0 - angle) / 90.0) ** 2

                self.theme.setSelectedColor(1)

                c1, c2, c3 = self.songlistcd_score_color
                glColor4f(c1, c2, c3, 1)

                scale = 0.0013
                x = self.song_listcd_score_xpos
                y = self.song_listcd_score_ypos + f / 2.0
                try:
                    difficulties = item.partDifficulties[scene.scorePart.id]
                except KeyError:
                    difficulties = []
                    score, stars, name = "---", 0, "---"
                if len(difficulties) > 3:
                    y = self.song_listcd_score_ypos + f / 2.0

                #new
                for d in difficulties:
                    scores = item.getHighscores(d, part=scene.scorePart)
                    if scores:
                        score, stars, name, scoreExt = scores[0]
                        try:
                            notesHit, notesTotal, noteStreak, modVersion, handicap, handicapLong, originalScore = scoreExt
                        except ValueError:
                            notesHit, notesTotal, noteStreak, modVersion, oldScores1, oldScores2 = scoreExt
                            handicap = 0
                            handicapLong = "None"
                            originalScore = score
                    else:
                        score, stars, name = "---", 0, "---"

                    font.render(Song.difficulties[d.id].text, (x, y), scale=scale)

                    starscale = 0.02
                    starx = x + starscale / 2
                    stary = 1.0 - (y / scene.fontScreenBottom) - fh - starscale
                    scene.drawStarScore(w, h, starx, stary, stars, starscale) #MFH
                    c1, c2, c3 = self.songlistcd_score_color
                    glColor3f(c1, c2, c3)
                    if scores:
                        if notesTotal != 0:
                            score = "%s %.1f%%" % (score, (float(notesHit) / notesTotal) * 100.0)
                        if noteStreak != 0:
                            score = "%s (%d)" % (score, noteStreak)
                    font.render(unicode(score), (x + .15, y), scale=scale)
                    font.render(name, (x + .15, y + fh), scale=scale)
                    y += 2 * fh + f / 4.0
        elif self.setlist_type == 3:
            w, h = scene.geometry
            font = scene.fontDict['songListFont']
            item = scene.selectedItem
            if isinstance(item, Song.SongInfo):
                text = item.artist
                if (item.getLocked()):
                    text = "" # avoid giving away artist of locked song

                scale = 0.0015
                wt, ht = font.getStringSize(text, scale=scale)

                while wt > .21:
                    tlength = len(text) - 4
                    text = text[:tlength] + "..."
                    wt, ht = font.getStringSize(text, scale=scale)
                    if wt < .22:
                        break

                c1, c2, c3 = self.artist_text_color
                glColor3f(c1, c2, c3)

                text = string.upper(text)
                font.render(text, (.095, .44), scale=scale)

                if scene.img_diff3 != None:
                    imgwidth = scene.img_diff3.width1()
                    imgheight = scene.img_diff3.height1()
                    wfactor1 = 13.0 / imgwidth

                albumtag = item.album
                albumtag = string.upper(albumtag)
                wt, ht = font.getStringSize(albumtag, scale=scale)

                while wt > .21:
                    tlength = len(albumtag) - 4
                    albumtag = albumtag[:tlength] + "..."
                    wt, ht = font.getStringSize(albumtag, scale=scale)
                    if wt < .22:
                        break                    

                font.render(albumtag, (.095, .47), scale=0.0015)

                genretag = item.genre
                font.render(genretag, (.095, .49), scale=0.0015)                                

                yeartag = item.year           
                font.render(yeartag, (.095, .51), scale=0.0015)


                for i in range(5):
                    glColor3f(1, 1, 1) 
                    if i == 0:
                        diff = item.diffSong
                    elif i == 1:
                        diff = item.diffGuitar
                    elif i == 2:
                        diff = item.diffDrums
                    elif i == 3:
                        diff = item.diffBass
                    elif i == 4:
                        diff = item.diffVocals
                    if scene.img_diff1 == None or scene.img_diff2 == None or scene.img_diff3 == None:
                        if diff == -1:
                            font.render("N/A", (.18, .5585 + i * .025), scale=0.0014)
                        elif diff == 6:
                            glColor3f(1, 1, 0)  
                            font.render(str("*" * (diff -1)), (.18, 0.5685 + i * .025), scale=0.003)
                        else:
                            font.render(str("*" * diff + " " * (5 - diff)), (.18, 0.5685 + i * .025), scale=0.003)
                    else:
                        if diff == -1:
                            font.render("N/A", (.18, .5585 + i * .025), scale=0.0014)
                        elif diff == 6:
                            for k in range(0, 5):
                                scene.drawImage(scene.img_diff3, scale=(wfactor1, -wfactor1), coord=((.19 + .03 * k) * w, (0.2354-.0333 * i) * h))
                        else:
                            for k in range(0, diff):
                                scene.drawImage(scene.img_diff2, scale=(wfactor1, -wfactor1), coord=((.19 + .03 * k) * w, (0.2354-.0333 * i) * h))
                            for k in range(0, 5-diff):
                                scene.drawImage(scene.img_diff1, scale=(wfactor1, -wfactor1), coord=((.31-.03 * k) * w, (0.2354-.0333 * i) * h))

    def renderMoreInfo(self, scene):
        if not scene.items:
            return
        if not scene.selectedItem:
            return
        item = scene.selectedItem
        i = scene.selectedIndex
        y = 0
        w, h = scene.geometry
        font = scene.fontDict['songListFont']
        self.theme.fadeScreen(0.25)
        if scene.moreInfoTime < 500:
            y = 1.0-(float(scene.moreInfoTime) / 500.0)
        yI = y * h
        if scene.img_panel:
            scene.drawImage(scene.img_panel, scale=(1.0, -1.0), coord=(w * .5, h * .5 + yI), stretched=3)
        if scene.img_tabs:
            r0 = (0, (1.0 / 3.0), 0, .5)
            r1 = ((1.0 / 3.0), (2.0 / 3.0), 0, .5)
            r2 = ((2.0 / 3.0), 1.0, 0, .5)
            if scene.infoPage == 0:
                r0 = (0, (1.0 / 3.0), .5, 1.0)
                scene.drawImage(scene.img_tab1, scale=(.5, -.5), coord=(w * .5, h * .5 + yI))
                text = item.name
                if item.artist != "":
                    text += " by %s" % item.artist
                if item.year != "":
                    text += " (%s)" % item.year
                scale = font.scaleText(text, .45, .0015)
                font.render(text, (.52, .25-y), scale=scale, align=1)
                if scene.itemLabels[i]:
                    imgwidth = scene.itemLabels[i].width1()
                    wfactor = 95.000 / imgwidth
                    scene.drawImage(scene.itemLabels[i], (wfactor, -wfactor), (w * .375, h * .5 + yI))
                elif scene.img_empty_label:
                    imgwidth = scene.img_empty_label.width1()
                    wfactor = 95.000 / imgwidth
                    scene.drawImage(scene.img_empty_label, (wfactor, -wfactor), (w * .375, h * .5 + yI))
                text = item.album
                if text == "":
                    text = _("No Album")
                scale = font.scaleText(text, .2, .0015)
                font.render(text, (.56, .305-y), scale=scale)
                text = item.genre
                if text == "":
                    text = _("No Genre")
                scale = font.scaleText(text, .2, .0015)
                font.render(text, (.56, .35-y), scale=scale)
            elif scene.infoPage == 1:
                r1 = ((1.0 / 3.0), (2.0 / 3.0), .5, 1.0)
                scene.drawImage(scene.img_tab2, scale=(.5, -.5), coord=(w * .5, h * .5 + yI))
            elif scene.infoPage == 2:
                r2 = ((2.0 / 3.0), 1.0, .5, 1.0)
            scene.drawImage(scene.img_tab3, scale=(.5, -.5), coord=(w * .5, h * .5 + yI))
            scene.drawImage(scene.img_tabs, scale=(.5 * (1.0 / 3.0), -.25), coord=(w * .36, h * .72 + yI), rect=r0)
            scene.drawImage(scene.img_tabs, scale=(.5 * (1.0 / 3.0), -.25), coord=(w * .51, h * .72 + yI), rect=r1)
            scene.drawImage(scene.img_tabs, scale=(.5 * (1.0 / 3.0), -.25), coord=(w * .66, h * .72 + yI), rect=r2)

