import time
import pygame

from ScreenPack.IScreen import IScreen


class TimeScreen(IScreen):
    # <editor-fold desc="Declaration and Initial / Constructor">

    def __init__(self):
        self.__canvas = pygame.display.get_surface()
        self.__font = pygame.font.Font("src/Font/Reckoner.ttf", 540)
        self.timeHour = 0
        self.timeMinute = 0
        self.timeSecond = 0

    # </editor-fold>

    # <editor-fold desc="Update Logic">

    def OnKeyboardUpdate(self):
        pass

    def OnUpdatePerSecond(self):
        pass

    def OnUpdatePerMinute(self):
        pass

    # </editor-fold>

    # <editor-fold desc="Paint Logic">

    def OnPaint(self):
        _time = time.localtime()
        self.timeHour = _time.tm_hour
        self.timeMinute = _time.tm_min
        self.timeSecond = _time.tm_sec
        _timeContentHour = ('%02d' % self.timeHour)
        _timeContentMinute = ('%02d' % self.timeMinute)

        # Draw hour value
        _renderText = self.__font.render(_timeContentHour, True, (255, 255, 255))
        _recText = _renderText.get_rect()
        _locationX = (381 - (_recText[2] - 17)) / 2
        IScreen.PaintShadowText(self.__canvas, self.__font, _timeContentHour, (255, 255, 255), (_locationX, -17))

        # Draw colon
        if self.timeSecond % 2 == 0:
            IScreen.PaintShadowText(self.__canvas, self.__font, ":", (255, 255, 255), (381, -93))
        else:
            IScreen.PaintShadowText(self.__canvas, self.__font, ":", (64, 64, 64), (381, -93))

        # Draw minute value
        _renderText = self.__font.render(_timeContentMinute, True, (255, 255, 255))
        _recText = _renderText.get_rect()
        _locationX = 419 + (381 - (_recText[2] - 17)) / 2
        IScreen.PaintShadowText(self.__canvas, self.__font, _timeContentMinute, (255, 255, 255), (_locationX, -17))

    # </editor-fold>
