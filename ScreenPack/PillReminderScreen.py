import pygame

from ScreenPack.IScreen import IScreen


class PillReminderScreen(IScreen):
    isColinTaken = True
    isStoneTaken = True

    def __init__(self):
        self.__canvas = pygame.display.get_surface()
        self.__font = pygame.font.Font("src\\Font\\Targa MS.ttf", 64)

    def OnUpdate(self):
        pass

    def OnPaint(self):
        self.__canvas.blit(self.__font.render("PILL", True, (128, 128, 128)), (22, 2))
        self.__canvas.blit(self.__font.render("PILL", True, (255, 255, 0)), (20, 0))

    @staticmethod
    def IsNotTakenToday():
        return not PillReminderScreen.isColinTaken or not PillReminderScreen.isStoneTaken
