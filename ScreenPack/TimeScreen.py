import time
import pygame

from ScreenPack.IScreen import IScreen


class MainScreen(IScreen):
    timeHour = 0
    timeMinute = 0
    timeSecond = 0

    def __init__(self):
        self.__canvas = pygame.display.get_surface()
        self.__font = pygame.font.Font("src/Font/Reckoner.ttf", 200)

    def OnUpdate(self):
        pass

    def OnPaint(self):
        _time = time.localtime()
        MainScreen.timeHour = _time.tm_hour
        MainScreen.timeMinute = _time.tm_min
        MainScreen.timeSecond = _time.tm_sec
        _timeContentHour = ('%02d' % MainScreen.timeHour)
        _timeContentMinute = ('%02d' % MainScreen.timeMinute)

        # Draw hour value
        _renderText = self.__font.render(_timeContentHour, True, (255, 255, 255))
        _recText = _renderText.get_rect()
        _locationX = (152 - (_recText[2] - 10)) / 2
        self.__canvas.blit(self.__font.render(_timeContentHour, True, (128, 128, 128)), (_locationX + 2, 7))
        self.__canvas.blit(_renderText, (_locationX, 5))

        # Draw colon
        if MainScreen.timeSecond % 2 == 0:
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
        self.__canvas.blit(_renderText, (_locationX, 5))
