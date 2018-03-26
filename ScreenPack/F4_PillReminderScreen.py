import pygame
import time

from DataPack.Court import Court
from ScreenPack.IScreen import IScreen
from Utility.ConfigHelper import ConfigHelper
from Utility.KeyboardHelper import KeyboardHelper
from Utility.SoundHelper import SoundHelper


class PillReminderScreen(IScreen):
    # <editor-fold desc="Declaration and Initial / Constructor">

    def __init__(self):
        self.__canvas = pygame.display.get_surface()
        self.__font = pygame.font.Font("src/Font/Reckoner.ttf", 268)
        self.__imgPillNotTaken = pygame.image.load('src/Icon/Pill_NotTaken.png')
        self.__imgPillTaken = pygame.image.load('src/Icon/Pill_Taken.png')
        self.__isColinTaken = None
        self.__isStoneTaken = None
        self.__InitData()

    def __InitData(self):
        _time = time.localtime()
        _currentDate = '%02d' % _time.tm_mon + '%02d' % _time.tm_mday
        if Court.configItemPill["date"] != _currentDate:
            Court.configItemPill["date"] = _currentDate
            Court.configItemPill["isColinTaken"] = False
            Court.configItemPill["isStoneTaken"] = False
        self.__isColinTaken = Court.configItemPill["isColinTaken"]
        self.__isStoneTaken = Court.configItemPill["isStoneTaken"]

    # </editor-fold>

    # <editor-fold desc="Key Related Logic">

    def OnUpdate(self):
        if KeyboardHelper.IsPress(pygame.K_c):
            self.__isColinTaken = not self.__isColinTaken
            self.__UpdateData()
        if KeyboardHelper.IsPress(pygame.K_s):
            self.__isStoneTaken = not self.__isStoneTaken
            self.__UpdateData()

    def __UpdateData(self):
        IScreen.ForceUpdate()
        if self.__isColinTaken and self.__isStoneTaken:
            SoundHelper.PlaySpeech("AllMedicineTaken")
        Court.configItemPill["isColinTaken"] = self.__isColinTaken
        Court.configItemPill["isStoneTaken"] = self.__isStoneTaken
        ConfigHelper.SaveToFile()

    # </editor-fold>

    # <editor-fold desc="Update Logic">

    def OnUpdatePerSecond(self):
        pass

    def OnUpdatePerMinute(self):
        _time = time.localtime()
        if _time.tm_hour is 21 and _time.tm_min is 0:
            if self.__isColinTaken is False or self.__isStoneTaken is False:
                SoundHelper.PlayMusic("AlarmMusic9")

    # </editor-fold>

    # <editor-fold desc="Paint Logic">

    def OnPaint(self):
        if self.__isColinTaken:
            self.__canvas.blit(self.__imgPillTaken, (4, 4))
            IScreen.PaintShadowTextOffset(self.__canvas, self.__font, "COLIN", (64, 64, 64), (208, -9), 4)
        else:
            self.__canvas.blit(self.__imgPillNotTaken, (4, 4))
            IScreen.PaintShadowTextOffset(self.__canvas, self.__font, "COLIN", (255, 255, 255), (208, -9), 4)

        if self.__isStoneTaken:
            self.__canvas.blit(self.__imgPillTaken, (4, 204))
            IScreen.PaintShadowTextOffset(self.__canvas, self.__font, "STONE", (64, 64, 64), (208, 191), 4)
        else:
            self.__canvas.blit(self.__imgPillNotTaken, (4, 204))
            IScreen.PaintShadowTextOffset(self.__canvas, self.__font, "STONE", (255, 255, 255), (208, 191), 4)

    # </editor-fold>
