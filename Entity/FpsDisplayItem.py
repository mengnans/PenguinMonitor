import time
import pygame

class FpsDisplayItem:

    def __init__(self):
        self.__fps = 0
        self.__fpsTick = 0
        self.__second = 0
        self.__lastUpdateTick = 0

        self.__canvas = pygame.display.get_surface()
        self.__font = pygame.font.Font("src/Font/Inconsolata.otf", 18)

    def Tick(self):
        self.__fpsTick = self.__fpsTick + 1
        if int(time.time()) != self.__second:
            _currentTime = time.time()
            self.__second = int(_currentTime)
            self.__fps = self.__fpsTick / (_currentTime - self.__lastUpdateTick)
            self.__lastUpdateTick = _currentTime
            self.__fpsTick = 0

        self.__canvas.blit(self.__font.render("%.2f" % self.__fps, True, (255, 255, 255)), (2, -2))
