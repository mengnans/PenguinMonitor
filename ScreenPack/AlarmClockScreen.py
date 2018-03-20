import pygame

from ScreenPack.IScreen import IScreen


class AlarmClockScreen(IScreen):
    isCounting = False
    isAboutToEnd = False

    def __init__(self):
        self.__canvas = pygame.display.get_surface()
        self.__font = pygame.font.Font("src/Font/Reckoner.ttf", 200)

    def OnUpdate(self):
        pass

    def OnPaint(self):
        self.__canvas.blit(self.__font.render("TIME", True, (128, 128, 128)), (22, 20))
        self.__canvas.blit(self.__font.render("TIME", True, (255, 255, 0)), (20, 18))
