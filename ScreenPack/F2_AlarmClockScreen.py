import pygame
import time

from DataPack.Court import Court
from ScreenPack.IScreen import IScreen
from Utility.ConfigHelper import ConfigHelper
from Utility.KeyboardHelper import KeyboardHelper
from Utility.SoundHelper import SoundHelper


class AlarmClockScreen(IScreen):
    # <editor-fold desc="Declaration and Initial / Constructor">

    __FONT_COLOR = ((255, 192, 192), (192, 255, 192), (192, 192, 255))
    __LOCATION_Y = (2, 135, 268)

    def __init__(self):
        self.__canvas = pygame.display.get_surface()
        self.__font = pygame.font.Font("src/Font/Consola.ttf", 195)
        self.__imageClockType = (pygame.image.load('src/Icon/AlarmClock_Disabled.png'), pygame.image.load('src/Icon/AlarmClock_Once.png'), pygame.image.load('src/Icon/AlarmClock_Infinite.png'))
        self.__imgArrows = pygame.image.load('src/Icon/AlarmClock_LRArrow.png')
        self.__selectIndex = 0
        self.__timeData = None
        self.__alarmType = None
        self.__InitData()

    def __InitData(self):
        self.__timeData = Court.configItemAlarmClock["time"]
        self.__alarmType = Court.configItemAlarmClock["type"]

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
            self.__UpdateData()
        if KeyboardHelper.IsPress(pygame.K_RIGHT):
            self.__alarmType[self.__selectIndex] = (self.__alarmType[self.__selectIndex] + 4) % 3
            self.__UpdateData()

    def __KeyActionNumber(self):
        for i in range(0, 10):
            if KeyboardHelper.IsPress(pygame.K_KP0 + i) | KeyboardHelper.IsPress(pygame.K_0 + i):
                _srcContent = self.__timeData[self.__selectIndex]
                _dstContent = _srcContent[1:2] + _srcContent[3:4] + ":" + _srcContent[4:5] + str(i)
                self.__timeData[self.__selectIndex] = _dstContent
                self.__UpdateData()

    @staticmethod
    def __UpdateData():
        IScreen.ForceUpdate()
        ConfigHelper.SaveToFile()

    # </editor-fold>

    # <editor-fold desc="Update Logic">

    def OnUpdatePerSecond(self):
        pass

    def OnUpdatePerMinute(self):
        _time = time.localtime()
        _currentTime = '%02d' % _time.tm_hour + ":" + '%02d' % _time.tm_min
        for i in range(0, 3):
            if self.__timeData[i] == _currentTime and self.__alarmType[i] != 0:
                self.__OnAlarm(i)

    def __OnAlarm(self, argIndex):
        SoundHelper.PlayMusic("AlarmMusic9")
        if self.__alarmType[argIndex] == 1:
            self.__alarmType[argIndex] = 0
            IScreen.ForceUpdate()
            ConfigHelper.SaveToFile()

    # </editor-fold>

    # <editor-fold desc="Paint Logic">

    def OnPaint(self):
        for i in range(0, 3):
            if i is self.__selectIndex:
                self.__canvas.blit(self.__imgArrows, (22, AlarmClockScreen.__LOCATION_Y[i] + 27))
            self.__canvas.blit(self.__imageClockType[self.__alarmType[i]], (61, AlarmClockScreen.__LOCATION_Y[i]))
            IScreen.PaintShadowTextOffset(self.__canvas, self.__font, self.__timeData[i], AlarmClockScreen.__FONT_COLOR[i], (258, AlarmClockScreen.__LOCATION_Y[i] - 19), 3)

    def __PaintTime(self, argLeftContent, argRightContent, argRightContentColor):
        pass

    # </editor-fold>
