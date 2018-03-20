import time
import pygame

from DataPack.DataProgram import DataProgram
from DataPack.Decorator import OnDebug


class FpsDisplayItem:

    @OnDebug
    def __init__(self):
        self.__fps = 0
        self.__fpsTick = 0
        self.__second = 0
        self.__lastUpdateTick = 0

        self.__canvas = pygame.display.get_surface()
        self.__font = pygame.font.Font("src\\Font\\Inconsolata.otf", 18)

    @OnDebug
    def Tick(self):
        if DataProgram.IsDebugMode == False:
            return
        self.__fpsTick = self.__fpsTick + 1
        if int(time.time()) != self.__second:
            _currentTime = time.time()
            self.__second = int(_currentTime)
            self.__fps = self.__fpsTick / (_currentTime - self.__lastUpdateTick)
            self.__lastUpdateTick = _currentTime
            self.__fpsTick = 0

        self.__canvas.blit(self.__font.render("%.2f" % self.__fps, True, (128, 128, 128)), (2, -2))
