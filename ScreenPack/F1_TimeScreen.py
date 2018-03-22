import time
import pygame

from ScreenPack.IScreen import IScreen


class TimeScreen(IScreen):

    timeHour = 0
    timeMinute = 0
    timeSecond = 0

    def __init__(self):
        self.__canvas = pygame.display.get_surface()
        self.__font = pygame.font.Font("src/Font/Reckoner.ttf", 540)

    def OnUpdate(self):
        pass

    def OnUpdateSecond(self):
        pass

    def OnUpdateMinute(self):
        pass

    def OnPaint(self):
        _time = time.localtime()
        TimeScreen.timeHour = _time.tm_hour
        TimeScreen.timeMinute = _time.tm_min
        TimeScreen.timeSecond = _time.tm_sec
        _timeContentHour = ('%02d' % TimeScreen.timeHour)
        _timeContentMinute = ('%02d' % TimeScreen.timeMinute)

        # Draw hour value
        _renderText = self.__font.render(_timeContentHour, True, (255, 255, 255))
        _recText = _renderText.get_rect()
        _locationX = (370 - (_recText[2] - 17)) / 2
        IScreen.PaintShadowText(self.__canvas, self.__font, _timeContentHour, (255, 255, 255), (_locationX, -17))

        # Draw colon
        if TimeScreen.timeSecond % 2 == 0:
            IScreen.PaintShadowText(self.__canvas, self.__font, ":", (255, 255, 255), (370, -93))
        else:
            IScreen.PaintShadowText(self.__canvas, self.__font, ":", (64, 64, 64), (370, -93))

        # Draw minute value
        _renderText = self.__font.render(_timeContentMinute, True, (255, 255, 255))
        _recText = _renderText.get_rect()
        _locationX = 430 + (370 - (_recText[2] - 17)) / 2
        IScreen.PaintShadowText(self.__canvas, self.__font, _timeContentMinute, (255, 255, 255), (_locationX, -17))
