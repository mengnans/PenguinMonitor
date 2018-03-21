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
    __alarmTimeString = '0000'

    def __init__(self):
        self.__canvas = pygame.display.get_surface()
        self.__font = pygame.font.Font("src/Font/Reckoner.ttf", 200)

    def OnUpdate(self):
        for _num in range(0, 10):
            if KeyboardHelper.IsPress(pygame.K_KP0 + _num) | KeyboardHelper.IsPress(pygame.K_0 + _num):
                AlarmClockScreen.__alarmTimeString += str(_num)
                AlarmClockScreen.__alarmTimeString = AlarmClockScreen.__alarmTimeString[1:]
                IScreen.ForceUpdate()
        if KeyboardHelper.IsPress(pygame.K_KP_ENTER) | KeyboardHelper.IsPress(pygame.K_RETURN):
            AlarmClockScreen.__isCounting = True
            SoundHelper.PlaySpeech("AlarmClockStarted")
            IScreen.ForceUpdate()
        if KeyboardHelper.IsPress(pygame.K_ESCAPE):
            if AlarmClockScreen.__isCounting:
                SoundHelper.PlaySpeech("AlarmClockStopped")
                AlarmClockScreen.__isCounting = False
                IScreen.ForceUpdate()
            else:
                AlarmClockScreen.__alarmTimeString = '0000'
                IScreen.ForceUpdate()

    def OnPaint(self):
        if AlarmClockScreen.__isCounting == False:
            self.__PaintTimeSelecting()
        else:
            self.__PaintTimeCounting()

    # Handle the display of "Selecting time"
    def __PaintTimeSelecting(self):
        _timeContentHour = AlarmClockScreen.__alarmTimeString[:2]
        _timeContentMinute = AlarmClockScreen.__alarmTimeString[2:]

        # Draw hour value
        _renderText = self.__font.render(_timeContentHour, True, (255, 255, 255))
        _recText = _renderText.get_rect()
        _locationX = (152 - (_recText[2] - 10)) / 2
        self.__canvas.blit(self.__font.render(_timeContentHour, True, (128, 128, 128)), (_locationX + 2, 7))
        self.__canvas.blit(self.__font.render(_timeContentHour, True, (255, 255, 0)), (_locationX, 5))

        # Draw colon
        if AlarmClockScreen.__timeSecond % 2 == 0:
            self.__canvas.blit(self.__font.render(":", True, (128, 128, 128)), (154, -18))
            self.__canvas.blit(self.__font.render(":", True, (255, 255, 0)), (152, -20))
        else:
            self.__canvas.blit(self.__font.render(":", True, (64, 64, 64)), (154, -18))
            self.__canvas.blit(self.__font.render(":", True, (128, 128, 128)), (152, -20))

        # Draw minute value
        _renderText = self.__font.render(_timeContentMinute, True, (255, 255, 255))
        _recText = _renderText.get_rect()
        _locationX = 168 + (152 - (_recText[2] - 10)) / 2
        self.__canvas.blit(self.__font.render(_timeContentMinute, True, (128, 128, 128)), (_locationX + 2, 7))
        self.__canvas.blit(self.__font.render(_timeContentMinute, True, (255, 255, 0)), (_locationX, 5))

    # Handle the display of "Counting down"
    def __PaintTimeCounting(self):
        pass

    @staticmethod
    def IsCounting():
        return AlarmClockScreen.__isCounting

    @staticmethod
    def IsAboutToEnd():
        return AlarmClockScreen.__isAboutToEnd
