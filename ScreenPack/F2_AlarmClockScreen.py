import pygame
import time

from ScreenPack.IScreen import IScreen
from Utility.KeyboardHelper import KeyboardHelper
from Utility.SoundHelper import SoundHelper


class AlarmClockScreen(IScreen):
    # <editor-fold desc="Declaration and Initial / Constructor">

    FONT_COLOR = ((255, 192, 192), (192, 255, 192), (192, 192, 255))
    __LOCATION_Y = (2, 135, 268)

    __timeData = ["01:23", "09:00", "21:00"]
    __alarmType = [0, 1, 2]

    __isAlarmed = [False, False, False]

    def __init__(self):
        self.__canvas = pygame.display.get_surface()
        self.__font = pygame.font.Font("src/Font/Consola.ttf", 195)
        self.__imageClockType = (pygame.image.load('src/Icon/AlarmClock_Disabled.png'), pygame.image.load('src/Icon/AlarmClock_Once.png'), pygame.image.load('src/Icon/AlarmClock_Infinite.png'))
        self.__imgArrows = pygame.image.load('src/Icon/AlarmClock_LRArrow.png')

        self.__selectIndex = 0

    # </editor-fold>

    # <editor-fold desc="Key Related Logic">

    def OnUpdate(self):
        self.__KeyActionArrow()
        self.__KeyActionNumber()

    def __KeyActionArrow(self):
        if KeyboardHelper.IsPress(pygame.K_UP):
            self.__selectIndex = (self.__selectIndex + 2) % 3
            IScreen.ForceUpdate()
        if KeyboardHelper.IsPress(pygame.K_DOWN):
            self.__selectIndex = (self.__selectIndex + 4) % 3
            IScreen.ForceUpdate()
        if KeyboardHelper.IsPress(pygame.K_LEFT):
            self.__alarmType[self.__selectIndex] = (self.__alarmType[self.__selectIndex] + 2) % 3
            IScreen.ForceUpdate()
        if KeyboardHelper.IsPress(pygame.K_RIGHT):
            self.__alarmType[self.__selectIndex] = (self.__alarmType[self.__selectIndex] + 4) % 3
            IScreen.ForceUpdate()

    def __KeyActionNumber(self):
        for _num in range(0, 10):
            if KeyboardHelper.IsPress(pygame.K_KP0 + _num) | KeyboardHelper.IsPress(pygame.K_0 + _num):
                _srcContent = AlarmClockScreen.__timeData[self.__selectIndex]
                _dstContent = _srcContent[1:2] + _srcContent[3:4] + ":" + _srcContent[4:5] + str(_num)
                AlarmClockScreen.__timeData[self.__selectIndex] = _dstContent
                IScreen.ForceUpdate()

    def __UpdateToNewData(self):
        pass

    # </editor-fold>

    # <editor-fold desc="Update Logic">

    def OnUpdatePerSecond(self):
        pass

    def OnUpdatePerMinute(self):
        pass
        pass
        pass

    # </editor-fold>

    # <editor-fold desc="Paint Logic">

    def OnPaint(self):
        for i in range(0, 3):
            if i is self.__selectIndex:
                self.__canvas.blit(self.__imgArrows, (22, AlarmClockScreen.__LOCATION_Y[i] + 27))
            self.__canvas.blit(self.__imageClockType[AlarmClockScreen.__alarmType[i]], (61, AlarmClockScreen.__LOCATION_Y[i]))
            IScreen.PaintShadowTextOffset(self.__canvas, self.__font, AlarmClockScreen.__timeData[i], AlarmClockScreen.FONT_COLOR[i], (258, AlarmClockScreen.__LOCATION_Y[i] - 19), 3)

    def __PaintTime(self, argLeftContent, argRightContent, argRightContentColor):
        pass

    # </editor-fold>
