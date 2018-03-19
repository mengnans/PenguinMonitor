import time
import pygame

from DataPack.DataProgram import DataProgram


class FpsDisplayItem:

    def __init__(self):
        self.__fps = 0
        self.__fpsTick = 0
        self.__second = 0
        self.__lastUpdateTick = 0

        self.__canvas = pygame.display.get_surface()
        self.__font = pygame.font.Font("src\\Font\\Inconsolata.otf", 18)

    def Tick(self):
        if DataProgram.IsDebugMode == False:
            return
        if int(time.time()) == self.__second:
            self.__fpsTick = self.__fpsTick + 1
        else:
            _currentTime = time.time()
            self.__second = int(_currentTime)
            self.__fps = self.__fpsTick / (_currentTime - self.__lastUpdateTick)
            self.__lastUpdateTick = _currentTime
            self.__fpsTick = 0

        self.__canvas.blit(self.__font.render(str(self.__fps), True, (128, 128, 128)), (2, -2))
