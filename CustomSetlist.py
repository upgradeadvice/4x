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
__date__   = "$Aug 23, 2010 02:28:05 AM$"

import string
from OpenGL.raw.GL import glColor3f
from OpenGL.raw.GL import glColor4f
import Song as Song
from Theme import _

class CustomSetlist:

    def __init__(self, theme):
        self.theme = theme
        self.setlist_type = 3
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
        self.song_name_selected_color = \
            self.theme.song_name_selected_colorVar
        self.song_rb2_diff_color = self.theme.song_rb2_diff_colorVar
        self.artist_text_color = self.theme.artist_text_colorVar
        self.artist_selected_color = self.theme.artist_selected_colorVar
        self.library_text_color = self.theme.library_text_colorVar
        self.library_selected_color = \
            self.theme.library_selected_colorVar
        self.songlist_score_color = self.theme.songlist_score_colorVar
        self.songlistcd_score_color = \
            self.theme.songlistcd_score_colorVar
        self.song_cd_xpos = 0.20000000000000001
        self.song_cdscore_xpos = 0.20000000000000001
        self.song_list_xpos = 0.20000000000000001
        self.song_listscore_xpos = 0.20000000000000001
        self.song_listcd_list_xpos = 0.20000000000000001
        self.song_listcd_cd_xpos = 0.20000000000000001
        self.song_listcd_cd_ypos = .6
        self.song_listcd_score_xpos = 0.20000000000000001
        self.song_listcd_score_ypos = .6

        if self.setlist_type is None:
            self.setlist_type = 3
        if self.setlist_type == 3:
            self.setlistStyle = 0
            self.headerSkip = 1
            self.footerSkip = 1
            self.labelType = 0
            self.labelDistance = 1
            self.showMoreLabels = False
            self.texturedLabels = False
            self.itemsPerPage = 10
            self.showLockedSongs = True
            self.showSortTiers = True
            self.selectTiers = False
            self.itemSize = (0, 0.20000000000000001)

    def run(self, ticks):
        pass

    def renderHeader(self, scene):
        pass

    def renderUnselectedItem(
        self,
        scene,
        i,
        n,
        ):
        (w, h) = scene.geometry
        font = scene.fontDict['songListFont']
        if self.setlist_type == 3:
            font = scene.fontDict['songListFont']
            if not scene.items or scene.itemIcons is None:
                return
            item = scene.items[i]

            if scene.img_tier:
                imgwidth = scene.img_tier.width1()
                imgheight = scene.img_tier.height1()
                wfactor = 381 / imgwidth
                hfactor = 24.000 / imgheight
                if isinstance(item, Song.TitleInfo) or isinstance(item,
                        Song.SortTitleInfo) and scene.img_tier:
                    scene.drawImage(scene.img_tier, scale=(wfactor,
                                    -hfactor), coord=(w / 1.587, h
                                    - 0.055 * h * (n + 1) - 0.219 * h))

            icon = None
            if isinstance(item, Song.SongInfo):
                if item.icon != '':
                    try:
                        icon = scene.itemIcons[item.icon]
                        imgwidth = icon.width1()
                        wfactor = 14.000 / imgwidth
                        scene.drawImage(icon, scale=(1,
                                -1), coord=(w / 1.02, h - 0.0563
                                * h * (n + 1) - 0.2
                                * h))
                    except KeyError:
                        pass
            elif isinstance(item, Song.LibraryInfo):
                try:
                    icon = scene.itemIcons['Library']
                    imgwidth = icon.width1()
                    wfactor = 14.000 / imgwidth
                    scene.drawImage(icon, scale=(1, -1),
                                    coord=(w / 1.02, h - 0.0563 * h
                                    * (n + 1) - 0.2
                                    * h))
                except KeyError:
                    pass
            elif isinstance(item, Song.RandomSongInfo):
                try:
                    icon = scene.itemIcons['Random']
                    imgwidth = icon.width1()
                    wfactor = 14.000 / imgwidth
                    scene.drawImage(icon, scale=(1, -1),
                                    coord=(w / 1.02, h - 0.0563 * h
                                    * (n + 1) - 0.2
                                    * h))
                except KeyError:
                    pass

            if isinstance(item, Song.SongInfo) or isinstance(item,
                    Song.LibraryInfo):
                (c1, c2, c3) = self.song_name_text_color
                glColor4f(c1, c2, c3, 1)
            elif isinstance(item, Song.TitleInfo) or isinstance(item,
                    Song.SortTitleInfo):
                (c1, c2, c3) = self.career_title_color
                glColor4f(c1, c2, c3, 1)
            elif isinstance(item, Song.RandomSongInfo):
                (c1, c2, c3) = self.song_name_text_color
                glColor4f(c1, c2, c3, 1)

            text = item.name

            if isinstance(item, Song.SongInfo) and item.getLocked():
                text = _('-- Locked --')

            if isinstance(item, Song.SongInfo):
                if scene.tiersPresent or icon:
                    text = '    ' + text

            maxwidth = .3

            if isinstance(item, Song.TitleInfo) or isinstance(item,
                    Song.SortTitleInfo):
                text = string.upper(text)

            scale = 0.00080000000000000004
            (wt, ht) = font.getStringSize(text, scale=scale)

            while wt > maxwidth:
                tlength = len(text) - 4
                text = text[:tlength] + '...'
                (wt, ht) = font.getStringSize(text, scale=scale)
                if wt < .45:
                    break

            font.render(text, (.05, .042 * (n + 1) + .15), scale=scale)

            if isinstance(item, Song.SongInfo):
                score = _("Nil")
                stars = 0
                name = ""
                if not item.getLocked():
                    try:
                        difficulties = \
                            item.partDifficulties[scene.scorePart.id]
                    except KeyError:
                        difficulties = []
                    for d in difficulties:
                        if d.id == scene.scoreDifficulty.id:
                            scores = item.getHighscores(d,
                                    part=scene.scorePart)
                            if scores:
                                (score, stars, name, scoreExt) = \
                                    scores[0]
                                try:
                                    (
                                        notesHit,
                                        notesTotal,
                                        noteStreak,
                                        modVersion,
                                        handicap,
                                        handicapLong,
                                        originalScore,
                                        ) = scoreExt
                                except ValueError:
                                    (
                                        notesHit,
                                        notesTotal,
                                        noteStreak,
                                        modVersion,
                                        oldScores1,
                                        oldScores2,
                                        ) = scoreExt

                                break
                            else:
                                (score, stars, name) = (0, 0, '---')

                    if score == _('Nil') and scene.nilShowNextScore:
                        for d in difficulties:
                            scores = item.getHighscores(d,
                                    part=scene.scorePart)
                            if scores:
                                (score, stars, name, scoreExt) = \
                                    scores[0]
                                try:
                                    (
                                        notesHit,
                                        notesTotal,
                                        noteStreak,
                                        modVersion,
                                        handicap,
                                        handicapLong,
                                        originalScore,
                                        ) = scoreExt
                                except ValueError:
                                    (
                                        notesHit,
                                        notesTotal,
                                        noteStreak,
                                        modVersion,
                                        oldScores1,
                                        oldScores2,
                                        ) = scoreExt

                                break
                            else:
                                (score, stars, name) = (0, 0, '---')
                        else:
                            (score, stars, name) = (_('Nil'), 0, '---')

                    scale = 0.0007
                    if score != _('Nil') and score > 0 \
                        and notesTotal != 0:
                        text = '%.1f%% (%d)' % (float(notesHit)
                                / notesTotal * 100.0, noteStreak)
                        font.render(text, (0.93000000000000003, .042
                                    * (n + 1) + .15), scale=scale,
                                    align=2)

                    text = str(score)

                    font.render(text, (0.75000000000000003, .042 * (n
                                + 1) + .15), scale=scale, align=2)

    def renderSelectedItem(self, scene, n):
        (w, h) = scene.geometry
        font = scene.fontDict['songListFont']

        item = scene.selectedItem
        if not item:
            return
        if isinstance(item, Song.BlankSpaceInfo):
            return
        if self.setlist_type == 3:
            y = h * (.7825 - .0459 * n)

            if scene.img_tier:
                imgwidth = scene.img_tier.width1()
                imgheight = scene.img_tier.height1()
                wfactor = 381.1 / imgwidth
                hfactor = 24.000 / imgheight
                if isinstance(item, Song.TitleInfo) or isinstance(item,
                        Song.SortTitleInfo):
                    scene.drawImage(scene.img_tier, scale=(wfactor,
                                    -hfactor), coord=(w / 1.587, h
                                    - 0.055 * h * (n + 1) - 0.219 * h))

            if scene.img_selected:
                imgwidth = scene.img_selected.width1()
                imgheight = scene.img_selected.height1()
                wfactor = 381.5 / imgwidth
                hfactor = 36.000 / imgheight

                scene.drawImage(scene.img_selected, scale=(wfactor,
                                -hfactor), coord=(w / 1.587, y * 1.2
                                - h * .213))

            icon = None
            if isinstance(item, Song.SongInfo):
                if item.icon != '':
                    try:
                        icon = scene.itemIcons[item.icon]
                        imgwidth = icon.width1()
                        wfactor = 15.000 / imgwidth
                        scene.drawImage(icon, scale=(1,
                                -1), coord=(w / 1.02, h - 0.0563
                                * h * (n + 1) - 0.2
                                * h))
                    except KeyError:
                        pass

                (c1, c2, c3) = self.song_name_selected_color
                glColor3f(c1, c2, c3)
                if item.getLocked():
                    text = item.getUnlockText()
                elif scene.careerMode and not item.completed:
                    text = _('Play To Advance')
                elif scene.practiceMode:
                    text = _('Practice')
                elif item.count:
                    count = int(item.count)
                    if count == 1:
                        text = _('Played Once')
                    else:
                        text = _('Played %d times.') % count
                else:
                    text = _('Quickplay')
            elif isinstance(item, Song.LibraryInfo):
                try:
                    icon = scene.itemIcons['Library']
                    imgwidth = icon.width1()
                    wfactor = 15.000 / imgwidth
                    scene.drawImage(icon, scale=(wfactor, -wfactor),
                                    coord=(w / 1.02, h - 0.0563 * h
                                    * (n + 1) - 0.20000000000000001
                                    * h))
                except KeyError:
                    pass
                (c1, c2, c3) = self.library_selected_color
                glColor3f(c1, c2, c3)
                if item.songCount == 1:
                    text = _('There Is 1 Song In This Setlist.')
                elif item.songCount > 1:
                    text = _('There Are %d Songs In This Setlist.') \
                        % item.songCount
                else:
                    text = ''
            elif isinstance(item, Song.TitleInfo) or isinstance(item,
                    Song.SortTitleInfo):
                text = _('Tier')
                (c1, c2, c3) = self.career_title_color
                glColor3f(c1, c2, c3)
            elif isinstance(item, Song.RandomSongInfo):
                try:
                    icon = scene.itemIcons['Random']
                    imgwidth = icon.width1()
                    wfactor = 15.000 / imgwidth
                    scene.drawImage(icon, scale=(1, -1),
                                    coord=(w / 1.02, h - 0.0563 * h
                                    * (n + 1) - 0.20000000000000001
                                    * h))
                except KeyError:
                    pass
                text = _('Random Song')
                (c1, c2, c3) = self.career_title_color
                glColor3f(c1, c2, c3)

            font.render(text, (0.93000000000000003, .169),
                        scale=0.00080000000000000004, align=2)

            maxwidth = 0.20000000000000001
            if isinstance(item, Song.SongInfo) or isinstance(item,
                    Song.LibraryInfo) or isinstance(item,
                    Song.RandomSongInfo):
                (c1, c2, c3) = self.song_name_selected_color
                glColor4f(c1, c2, c3, 1)
            if isinstance(item, Song.TitleInfo) or isinstance(item,
                    Song.SortTitleInfo):
                (c1, c2, c3) = self.career_title_color
                glColor4f(c1, c2, c3, 1)

            text = item.name

            if isinstance(item, Song.SongInfo) and item.getLocked():
                text = _('-- Locked --')

            if isinstance(item, Song.SongInfo):
                if scene.tiersPresent or icon:
                    text = '    ' + text

            if isinstance(item, Song.TitleInfo) or isinstance(item,
                    Song.SortTitleInfo):
                maxwidth = 0.20000000000000001
                text = string.upper(text)

            scale = 0.00080000000000000004
            (wt, ht) = font.getStringSize(text, scale=scale)

            while wt > maxwidth:
                tlength = len(text) - 4
                text = text[:tlength] + '...'
                (wt, ht) = font.getStringSize(text, scale=scale)
                if wt < .45:
                    break

            font.render(text, (.053, .042 * (n + 1) + .15), scale=scale)

            if isinstance(item, Song.SongInfo):
                score = _("Nil")
                stars = 0
                name = ""
                if not item.getLocked():
                    try:
                        difficulties = \
                            item.partDifficulties[scene.scorePart.id]
                    except KeyError:
                        difficulties = []
                    for d in difficulties:
                        if d.id == scene.scoreDifficulty.id:
                            scores = item.getHighscores(d,
                                    part=scene.scorePart)
                            if scores:
                                (score, stars, name, scoreExt) = \
                                    scores[0]
                                try:
                                    (
                                        notesHit,
                                        notesTotal,
                                        noteStreak,
                                        modVersion,
                                        handicap,
                                        handicapLong,
                                        originalScore,
                                        ) = scoreExt
                                except ValueError:
                                    (
                                        notesHit,
                                        notesTotal,
                                        noteStreak,
                                        modVersion,
                                        oldScores1,
                                        oldScores2,
                                        ) = scoreExt

                                break
                            else:
                                (score, stars, name) = (0, 0, '---')

                    if score == _('Nil') and scene.nilShowNextScore:
                        for d in difficulties:
                            scores = item.getHighscores(d,
                                    part=scene.scorePart)
                            if scores:
                                (score, stars, name, scoreExt) = \
                                    scores[0]
                                try:
                                    (
                                        notesHit,
                                        notesTotal,
                                        noteStreak,
                                        modVersion,
                                        handicap,
                                        handicapLong,
                                        originalScore,
                                        ) = scoreExt
                                except ValueError:
                                    (
                                        notesHit,
                                        notesTotal,
                                        noteStreak,
                                        modVersion,
                                        oldScores1,
                                        oldScores2,
                                        ) = scoreExt
                                break
                            else:
                                (score, stars, name) = (0, 0, '---')
                        else:
                            (score, stars, name) = (_('Nil'), 0, '---')

                    scale = 0.0007
                    if score != _('Nil') and score > 0 \
                        and notesTotal != 0:
                        text = '%.1f%% (%d)' % (float(notesHit)
                                / notesTotal * 100.0, noteStreak)
                        (w, h) = font.getStringSize(text, scale=scale)
                        font.render(text, (0.93000000000000003, .042
                                    * (n + 1) + .15), scale=scale,
                                    align=2)
                    text = str(score)

                    font.render(text, (0.75000000000000003, .042 * (n
                                + 1) + .15), scale=scale, align=2)
                    height = 0.0

    def renderAlbumArt(self, scene):
        if not scene.itemLabels:
            return
        if self.setlist_type == 3:
            (w, h) = scene.geometry
            item = scene.items[scene.selectedIndex]
            i = scene.selectedIndex
            img = None
            lockImg = None
            if scene.itemLabels[i] == 'Random':
                if scene.img_random_label:
                    img = scene.img_random_label
                    imgwidth = img.width1()
                    wfactor = 150.000 / imgwidth
                elif scene.img_empty_label:
                    img = scene.img_empty_label
                    imgwidth = img.width1()
                    wfactor = 150.000 / imgwidth
            elif not scene.itemLabels[i]:
                if scene.img_empty_label != None:
                    imgwidth = scene.img_empty_label.width1()
                    wfactor = 150.000 / imgwidth
                    img = scene.img_empty_label
            elif scene.itemLabels[i]:
                img = scene.itemLabels[i]
                imgwidth = img.width1()
                wfactor = 150.000 / imgwidth
            if isinstance(item, Song.SongInfo) and item.getLocked():
                if scene.img_locked_label:
                    imgwidth = scene.img_locked_label.width1()
                    wfactor2 = 150.000 / imgwidth
                    lockImg = scene.img_locked_label
                elif scene.img_empty_label:
                    imgwidth = scene.img_empty_label.width1()
                    wfactor = 150.000 / imgwidth
                    img = scene.img_empty_label
            if img:
                scene.drawImage(img, scale=(wfactor, -wfactor),
                                coord=(.078 * w, .902 * h))
            if lockImg:
                scene.drawImage(lockImg, scale=(wfactor2, -wfactor2),
                                coord=(.078 * w, .902 * h))

    def renderForeground(self, scene):
        font = scene.fontDict['songListFont']
        (w, h) = scene.geometry
        if self.setlist_type == 3:
            font = scene.fontDict['songListFont']

            (c1, c2, c3) = self.song_rb2_diff_color
            glColor3f(c1, c2, c3)

            scale = 0.00080000000000000004
            text = _('BAND:')
            font.render(text, (.785, .035), scale=scale)
            text = _('GUITAR:')
            font.render(text, (.785, .055), scale=scale)
            text = _('DRUM:')
            font.render(text, (.785, .075), scale=scale)
            text = _('BASS:')
            font.render(text, (.785, .095), scale=scale)
            text = _('VOCALS:')
            font.render(text, (.785, .115), scale=scale)

            text = _('SORTING:') + '     '
            if scene.sortOrder == 0: 
                text = text + _('ALPHABETICALLY BY TITLE')
            elif scene.sortOrder == 1:


                text = text + _('ALPHABETICALLY BY ARTIST')
            elif scene.sortOrder == 2:


                text = text + _('BY PLAY COUNT')
            elif scene.sortOrder == 3:


                text = text + _('ALPHABETICALLY BY ALBUM')
            elif scene.sortOrder == 4:


                text = text + _('ALPHABETICALLY BY GENRE')
            elif scene.sortOrder == 5:


                text = text + _('BY YEAR')
            elif scene.sortOrder == 6:


                text = text + _('BY BAND DIFFICULTY')
            elif scene.sortOrder == 7:


                text = text + _('BY INSTRUMENT DIFFICULTY')
            else:
                text = text + _('BY SONG COLLECTION')

            font.render(text, (.04, .169), scale=0.00080000000000000004)

            if scene.songLoader:
                font.render(_('Loading Preview...'), (.05, .7),
                            scale=0.00080000000000000004)
            return
        if scene.img_list_button_guide:
            scene.drawImage(scene.img_list_button_guide, scale=(.5,
                            -.5), coord=(w * .5, 0), fit=2)
        if scene.songLoader:
            font.render(_('Loading Preview...'), (.5, .7), align=1)
        if scene.searching:
            font.render(scene.searchText, (.5, .7), align=1)
        if scene.img_list_fg:
            scene.drawImage(scene.img_list_fg, scale=(1.0, -1.0),
                            coord=(w / 2, h / 2), stretched=0)

    def renderSelectedInfo(self, scene):
        if self.setlist_type == 3:
            (w, h) = scene.geometry
            font = scene.fontDict['songListFont']
            item = scene.selectedItem
            if isinstance(item, Song.SongInfo):
                text = item.artist
                if item.getLocked():
                    text = ''  

                scale = 0.00080000000000000004
                (wt, ht) = font.getStringSize(text, scale=scale)

                while wt > .21:
                    tlength = len(text) - 4
                    text = text[:tlength] + '...'
                    (wt, ht) = font.getStringSize(text, scale=scale)
                    if wt < .22:
                        break

                (c1, c2, c3) = self.artist_text_color
                glColor3f(c1, c2, c3)

                text = string.upper(text)
                font.render(text, (.15, .03), scale=scale)

                if scene.img_diff3 != None:
                    imgwidth = scene.img_diff3.width1()

                    wfactor1 = 13.0 / imgwidth

                albumtag = item.album
                albumtag = string.upper(albumtag)
                (wt, ht) = font.getStringSize(albumtag, scale=scale)

                while wt > .21:
                    tlength = len(albumtag) - 4
                    albumtag = albumtag[:tlength] + '...'
                    (wt, ht) = font.getStringSize(albumtag, scale=scale)
                    if wt < .22:
                        break

                font.render(albumtag, (.15, .05),
                            scale=0.00080000000000000004)

                genretag = item.genre
                font.render(genretag, (.15, .10),
                            scale=0.00080000000000000004)

                yeartag = item.year
                font.render(yeartag, (.15, .12),
                            scale=0.00080000000000000004)

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
                    if scene.img_diff1 == None or scene.img_diff2 \
                        == None or scene.img_diff3 == None:
                        if diff == -1:
                            font.render(' ', (.3, .5585 + i * .025),
                                    scale=0.00080000000000000004)
                        elif diff == 6:
                            glColor3f(1, 1, 0)
                            font.render(str('*' * (diff - 1)), (.3,
                                    0.5525 + i * .025),
                                    scale=0.00080000000000000004)
                        else:
                            font.render(str('*' * diff + ' ' * (5
                                    - diff)), (.3, 0.5525 + i * .025),
                                    scale=0.00080000000000000004)
                    else:
                        if diff == -1:
                            font.render(' ', (.3, .5585 + i * .025),
                                    scale=0.00080000000000000004)
                        elif diff == 6:
                            for k in range(0, 5):
                                scene.drawImage(scene.img_diff3,
                                        scale=(wfactor1 * 1, -wfactor1
                                        * 1), coord=((.85 + .03 * k)
                                        * w, (0.955 - .028 * i) * h))
                        else:
                            for k in range(0, diff):
                                scene.drawImage(scene.img_diff2,
                                        scale=(wfactor1 * 1, -wfactor1
                                        * 1), coord=((.85 + .03 * k)
                                        * w, (0.955 - .028 * i) * h))
                            for k in range(0, 5 - diff):
                                scene.drawImage(scene.img_diff1,
                                        scale=(wfactor1 * 1, -wfactor1
                                        * 1), coord=((.97 - .03 * k)
                                        * w, (0.955 - .028 * i) * h))

    def renderMoreInfo(self, scene):
        if not scene.items:
            return
        if not scene.selectedItem:
            return
        item = scene.selectedItem
        i = scene.selectedIndex
        y = 0
        (w, h) = scene.geometry
        font = scene.fontDict['songListFont']
        self.theme.fadeScreen(.25)
        if scene.moreInfoTime < 500:
            y = 1.0 - float(scene.moreInfoTime) / 500.0
        yI = y * h
        if scene.img_panel:
            scene.drawImage(scene.img_panel, scale=(1.0, -1.0),
                            coord=(w * .5, h * .5 + yI), stretched=0)
        if scene.img_tabs:
            r0 = (0, 1.0 / 3.0, 0, .5)
            r1 = (1.0 / 3.0, 2.0 / 3.0, 0, .5)
            r2 = (2.0 / 3.0, 1.0, 0, .5)
            if scene.infoPage == 0:
                r0 = (0, 1.0 / 3.0, .5, 1.0)
                scene.drawImage(scene.img_tab1, scale=(.5, -.5),
                                coord=(w * .5, h * .5 + yI))
                text = item.name
                if item.artist != '':
                    text += ' by %s' % item.artist
                if item.year != '':
                    text += ' (%s)' % item.year
                scale = font.scaleText(text, .22,
                        0.00080000000000000004)
                font.render(text, (.22, .25 - y), scale=scale, align=1)
                if scene.itemLabels[i]:
                    imgwidth = scene.itemLabels[i].width1()
                    wfactor = 75.000 / imgwidth
                    scene.drawImage(scene.itemLabels[i], (wfactor,
                                    -wfactor), (w * .375, h * .5 + yI))
                elif scene.img_empty_label:
                    imgwidth = scene.img_empty_label.width1()
                    wfactor = 75.000 / imgwidth
                    scene.drawImage(scene.img_empty_label, (wfactor,
                                    -wfactor), (w * .375, h * .5 + yI))
                text = item.album
                if text == '':
                    text = _('No Album')
                scale = font.scaleText(text, 0.20000000000000001,
                        0.00080000000000000004)
                font.render(text, (.56, .305 - y), scale=scale)
                text = item.genre
                if text == '':
                    text = _('No Genre')
                scale = font.scaleText(text, 0.20000000000000001,
                        .00085)
                font.render(text, (.56, .35 - y), scale=scale)
            elif scene.infoPage == 1:
                r1 = (1.0 / 3.0, 2.0 / 3.0, .5, 1.0)
                scene.drawImage(scene.img_tab2, scale=(.5, -.5),
                                coord=(w * .5, h * .5 + yI))
            elif scene.infoPage == 2:
                r2 = (2.0 / 3.0, 1.0, .5, 1.0)
                scene.drawImage(scene.img_tab3, scale=(.5, -.5),
                                coord=(w * .5, h * .5 + yI))
            scene.drawImage(scene.img_tabs, scale=(.5 * (1.0 / 3.0),
                            -.25), coord=(w * .36, h * .72 + yI),
                            rect=r0)
            scene.drawImage(scene.img_tabs, scale=(.5 * (1.0 / 3.0),
                            -.25), coord=(w * .51, h * .72 + yI),
                            rect=r1)
            scene.drawImage(scene.img_tabs, scale=(.5 * (1.0 / 3.0),
                            -.25), coord=(w * .66, h * .72 + yI),
                            rect=r2)

    def renderMiniLobby(self, scene):
        return


