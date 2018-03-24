import pygame
import time

from ScreenPack.IScreen import IScreen
from Utility.KeyboardHelper import KeyboardHelper
from Utility.SoundHelper import SoundHelper


class AlarmClockScreen(IScreen):
    __isCounting = False
    __isAboutToEnd = False
    __timeHour = 0
    __timeMinute = 0
    __timeSecond = 0

    def __init__(self):
        self.__canvas = pygame.display.get_surface()
        self.__font = pygame.font.Font("src/Font/Reckoner.ttf", 540)
        self.__alarmTimeString = '0000'
        self.totalSecondDiff = 0

    def OnUpdate(self):
        if AlarmClockScreen.__isCounting is False:
            self.__OnKeyDownSelecting()
        elif KeyboardHelper.IsPress(pygame.K_ESCAPE):
            SoundHelper.PlaySpeech("AlarmClockStopped")
            AlarmClockScreen.__isCounting = False
            AlarmClockScreen.__isAboutToEnd = False
            IScreen.ForceUpdate()

    def OnUpdatePerSecond(self):
        pass

    def OnUpdatePerMinute(self):
        pass

    def __OnKeyDownSelecting(self):
        for _num in range(0, 10):
            if KeyboardHelper.IsPress(pygame.K_KP0 + _num) | KeyboardHelper.IsPress(pygame.K_0 + _num):
                self.__alarmTimeString += str(_num)
                self.__alarmTimeString = self.__alarmTimeString[1:]
                IScreen.ForceUpdate()
                break
        if KeyboardHelper.IsPress(pygame.K_ESCAPE):
            self.__alarmTimeString = '0000'
            IScreen.ForceUpdate()

        if (KeyboardHelper.IsPress(pygame.K_KP_ENTER) | KeyboardHelper.IsPress(pygame.K_RETURN)) \
                and self.__alarmTimeString.__eq__('0000') is False:
            AlarmClockScreen.__isCounting = True
            SoundHelper.PlaySpeech("AlarmClockStarted")
            AlarmClockScreen.__timeHour = int(self.__alarmTimeString[:2])
            AlarmClockScreen.__timeMinute = int(self.__alarmTimeString[2:])
            AlarmClockScreen.__timeSecond = 0
            _timeMinuteDiff = 0
            _timeMinuteDiff += AlarmClockScreen.__timeMinute
            _timeMinuteDiff += AlarmClockScreen.__timeHour * 60
            if _timeMinuteDiff <= 1:
                AlarmClockScreen.__isAboutToEnd = True
            _time = time.localtime()
            AlarmClockScreen.__timeHour += _time.tm_hour
            AlarmClockScreen.__timeMinute += _time.tm_min
            AlarmClockScreen.__timeSecond += _time.tm_sec
            IScreen.ForceUpdate()

    def OnPaint(self):
        if AlarmClockScreen.__isCounting is False:
            _leftContent = self.__alarmTimeString[:2]
            _rightContent = self.__alarmTimeString[2:]
            self.__PaintTime(_leftContent, _rightContent, (255, 255, 0))
        else:
            _time = time.localtime()
            _timeHourDiff = AlarmClockScreen.__timeHour - _time.tm_hour
            _timeMinuteDiff = AlarmClockScreen.__timeMinute - _time.tm_min
            _timeSecondDiff = AlarmClockScreen.__timeSecond - _time.tm_sec
            _timeSecondDiff += _timeMinuteDiff * 60
            _timeSecondDiff += _timeHourDiff * 60 * 60
            self.totalSecondDiff = _timeSecondDiff

            if _timeSecondDiff >= 3600:
                _leftContent = int(_timeSecondDiff / 3600)
                _timeSecondDiff %= 3600
                _rightContent = int(_timeSecondDiff / 60)
                self.__PaintTime('%02d' % _leftContent, '%02d' % _rightContent, (255, 255, 0))
            else:
                _leftContent = int(_timeSecondDiff / 60)
                _rightContent = _timeSecondDiff % 60
                self.__PaintTime('%02d' % _leftContent, '%02d' % _rightContent, (255, 165, 165))

    def __PaintTime(self, argLeftContent, argRightContent, argRightContentColor):
        # Draw left value
        _renderText = self.__font.render(argLeftContent, True, (255, 255, 255))
        _recText = _renderText.get_rect()
        _locationX = (370 - (_recText[2] - 17)) / 2
        IScreen.PaintShadowText(self.__canvas, self.__font, argLeftContent, (255, 255, 128), (_locationX, -17))

        # Draw colon
        if self.totalSecondDiff % 2 == 0:
            IScreen.PaintShadowText(self.__canvas, self.__font, ":", (255, 255, 128), (370, -93))
        else:
            IScreen.PaintShadowText(self.__canvas, self.__font, ":", (64, 64, 64), (370, -93))

        # Draw right value
        _renderText = self.__font.render(argRightContent, True, (255, 255, 255))
        _recText = _renderText.get_rect()
        _locationX = 430 + (370 - (_recText[2] - 17)) / 2
        IScreen.PaintShadowText(self.__canvas, self.__font, argRightContent, (255, 255, 128), (_locationX, -17))

    @staticmethod
    def IsCounting():
        return AlarmClockScreen.__isCounting

    @staticmethod
    def IsAboutToEnd():
        return AlarmClockScreen.__isAboutToEnd
