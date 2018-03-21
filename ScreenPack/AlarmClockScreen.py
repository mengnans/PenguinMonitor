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
        self.__font = pygame.font.Font("src/Font/Reckoner.ttf", 200)
        self.__alarmTimeString = '0000'

    def OnUpdate(self):
        if AlarmClockScreen.__isCounting is False:
            for _num in range(0, 10):
                if KeyboardHelper.IsPress(pygame.K_KP0 + _num) | KeyboardHelper.IsPress(pygame.K_0 + _num):
                    self.__alarmTimeString += str(_num)
                    self.__alarmTimeString = self.__alarmTimeString[1:]
                    IScreen.ForceUpdate()
                    break
        if KeyboardHelper.IsPress(pygame.K_KP_ENTER) | KeyboardHelper.IsPress(pygame.K_RETURN):
            if self.__alarmTimeString.__eq__('0000'):
                return
            if AlarmClockScreen.__isCounting:
                return
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
        if KeyboardHelper.IsPress(pygame.K_ESCAPE):
            if AlarmClockScreen.__isCounting:
                SoundHelper.PlaySpeech("AlarmClockStopped")
                AlarmClockScreen.__isCounting = False
                AlarmClockScreen.__isAboutToEnd = False
                IScreen.ForceUpdate()
            else:
                self.__alarmTimeString = '0000'
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

            if _timeSecondDiff <= 0:
                # TODO: make a noise
                AlarmClockScreen.__isAboutToEnd = False
                AlarmClockScreen.__isCounting = False
                self.__alarmTimeString = '0000'
                _leftContent = self.__alarmTimeString[:2]
                _rightContent = self.__alarmTimeString[2:]
                self.__PaintTime(str(_leftContent), str(_rightContent), (255, 255, 0))
            else:
                if _timeSecondDiff >= 3600:
                    _leftContent = int(_timeSecondDiff / 3600)
                    _timeSecondDiff %= 3600
                    _rightContent = int(_timeSecondDiff / 60)
                    self.__PaintTime(str(_leftContent), str(_rightContent), (255, 255, 0))
                else:
                    _leftContent = int(_timeSecondDiff / 60)
                    _rightContent = _timeSecondDiff % 60
                    if _timeSecondDiff <= 60 and AlarmClockScreen.__isAboutToEnd is False:
                        AlarmClockScreen.__isAboutToEnd = True
                        SoundHelper.PlaySpeech("AlarmClockIsAboutToEnd")
                    self.__PaintTime(str(_leftContent), str(_rightContent), (255, 165, 165))

    def __PaintTime(self, argLeftContent, argRightContent, argRightContentColor):
        if len(argLeftContent) == 1:
            argLeftContent = '0' + argLeftContent
        if len(argRightContent) == 1:
            argRightContent = '0' + argRightContent
        # Draw hour value
        _renderText = self.__font.render(argLeftContent, True, (255, 255, 255))
        _recText = _renderText.get_rect()
        _locationX = (152 - (_recText[2] - 10)) / 2
        self.__canvas.blit(self.__font.render(argLeftContent, True, (128, 128, 128)), (_locationX + 2, 7))
        self.__canvas.blit(self.__font.render(argLeftContent, True, (255, 255, 0)), (_locationX, 5))

        # Draw colon
        if AlarmClockScreen.__timeSecond % 2 == 0:
            self.__canvas.blit(self.__font.render(":", True, (128, 128, 128)), (154, -18))
            self.__canvas.blit(self.__font.render(":", True, (255, 255, 255)), (152, -20))
        else:
            self.__canvas.blit(self.__font.render(":", True, (64, 64, 64)), (154, -18))
            self.__canvas.blit(self.__font.render(":", True, (128, 128, 128)), (152, -20))

        # Draw minute value
        _renderText = self.__font.render(argRightContent, True, (255, 255, 255))
        _recText = _renderText.get_rect()
        _locationX = 168 + (152 - (_recText[2] - 10)) / 2
        self.__canvas.blit(self.__font.render(argRightContent, True, (128, 128, 128)), (_locationX + 2, 7))
        self.__canvas.blit(self.__font.render(argRightContent, True, argRightContentColor), (_locationX, 5))

    @staticmethod
    def IsCounting():
        return AlarmClockScreen.__isCounting

    @staticmethod
    def IsAboutToEnd():
        return AlarmClockScreen.__isAboutToEnd
