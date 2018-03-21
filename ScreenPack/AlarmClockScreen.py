import pygame
import time

from ScreenPack.IScreen import IScreen
from Utility.KeyboardHelper import KeyboardHelper


class AlarmClockScreen(IScreen):
    isCounting = False
    isAboutToEnd = False
    timeHour = 0
    timeMinute = 0
    timeSecond = 0

    def __init__(self):
        self.__canvas = pygame.display.get_surface()
        self.__font = pygame.font.Font("src/Font/Reckoner.ttf", 200)

    def OnUpdate(self):
        if KeyboardHelper.IsPress(pygame.K_KP1) | KeyboardHelper.IsPress(pygame.K_1):
            AlarmClockScreen.timeHour += 1
            IScreen.ForceUpdate()
        if KeyboardHelper.IsPress(pygame.K_KP2) | KeyboardHelper.IsPress(pygame.K_2):
            AlarmClockScreen.timeMinute += 10
            if AlarmClockScreen.timeMinute > 60:
                AlarmClockScreen.timeHour += 1
                AlarmClockScreen.timeMinute -= 60
            IScreen.ForceUpdate()
        if KeyboardHelper.IsPress(pygame.K_KP3) | KeyboardHelper.IsPress(pygame.K_3):
            AlarmClockScreen.timeMinute += 1
            if AlarmClockScreen.timeMinute > 60:
                AlarmClockScreen.timeHour += 1
                AlarmClockScreen.timeMinute -= 60
            IScreen.ForceUpdate()
        if KeyboardHelper.IsPress(pygame.K_ESCAPE):
            AlarmClockScreen.timeHour = 0
            AlarmClockScreen.timeMinute = 0
            AlarmClockScreen.timeSecond = 0
            AlarmClockScreen.isCounting = False
        if KeyboardHelper.IsPress(pygame.K_KP_ENTER) | KeyboardHelper.IsPress(pygame.K_RETURN):
            AlarmClockScreen.isCounting = True
        pass

    def OnPaint(self):
        self.__PaintTime()

    def __PaintTime(self):
        _timeContentHour = ('%02d' % AlarmClockScreen.timeHour)
        _timeContentMinute = ('%02d' % AlarmClockScreen.timeMinute)

        # Draw hour value
        _renderText = self.__font.render(_timeContentHour, True, (255, 255, 255))
        _recText = _renderText.get_rect()
        _locationX = (152 - (_recText[2] - 10)) / 2
        self.__canvas.blit(self.__font.render(_timeContentHour, True, (128, 128, 128)), (_locationX + 2, 7))
        self.__canvas.blit(self.__font.render(_timeContentHour, True, (255, 255, 255)), (_locationX, 5))

        # Draw colon
        if AlarmClockScreen.timeSecond % 2 == 0:
            self.__canvas.blit(self.__font.render(":", True, (128, 128, 128)), (154, -18))
            self.__canvas.blit(self.__font.render(":", True, (255, 255, 255)), (152, -20))
        else:
            self.__canvas.blit(self.__font.render(":", True, (64, 64, 64)), (154, -18))
            self.__canvas.blit(self.__font.render(":", True, (128, 128, 128)), (152, -20))

        # Draw minute value
        _renderText = self.__font.render(_timeContentMinute, True, (255, 255, 255))
        _recText = _renderText.get_rect()
        _locationX = 168 + (152 - (_recText[2] - 10)) / 2
        self.__canvas.blit(self.__font.render(_timeContentMinute, True, (128, 128, 128)), (_locationX + 2, 7))
        self.__canvas.blit(self.__font.render(_timeContentMinute, True, (255, 255, 255)), (_locationX, 5))
