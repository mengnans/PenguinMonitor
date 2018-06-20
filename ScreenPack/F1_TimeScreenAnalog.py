import time
import pygame

from ScreenPack.IScreen import IScreen


class TimeScreenAnalog(IScreen):
    # <editor-fold desc="Declaration and Initial / Constructor">

    def __init__(self):
        self.__canvas = pygame.display.get_surface()
        self.__imgBasic = pygame.image.load('src/Icon/BasicShape.png')
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
        self.__canvas.blit(self.__imgBasic, (0, 0))

    # </editor-fold>
