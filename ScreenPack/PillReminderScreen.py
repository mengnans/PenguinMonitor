import pygame

from ScreenPack.IScreen import IScreen
from Utility.KeyboardHelper import KeyboardHelper


class PillReminderScreen(IScreen):
    __isColinTaken = False
    __isStoneTaken = False

    def __init__(self):
        self.__canvas = pygame.display.get_surface()
        self.__font = pygame.font.Font("src/Font/Reckoner.ttf", 111)
        self.__imgPillNotTaken = pygame.image.load('src/Icon/Pill_NotTaken.png')
        self.__imgPillTaken = pygame.image.load('src/Icon/Pill_Taken.png')

    def OnUpdate(self):
        if KeyboardHelper.IsPress(pygame.K_c):
            PillReminderScreen.__isColinTaken = not PillReminderScreen.__isColinTaken
            IScreen.ForceUpdate()
        if KeyboardHelper.IsPress(pygame.K_s):
            PillReminderScreen.__isStoneTaken = not PillReminderScreen.__isStoneTaken
            IScreen.ForceUpdate()

    def OnPaint(self):
        if PillReminderScreen.__isColinTaken:
            self.__canvas.blit(self.__imgPillTaken, (5, 4))
            self.__canvas.blit(self.__font.render("Colin", True, (16, 16, 16)), (102, 0))
            self.__canvas.blit(self.__font.render("Colin", True, (64, 64, 64)), (100, -2))
        else:
            self.__canvas.blit(self.__imgPillNotTaken, (5, 4))
            self.__canvas.blit(self.__font.render("Colin", True, (128, 128, 128)), (102, 0))
            self.__canvas.blit(self.__font.render("Colin", True, (255, 255, 255)), (100, -2))

        if PillReminderScreen.__isStoneTaken:
            self.__canvas.blit(self.__imgPillTaken, (5, 90))
            self.__canvas.blit(self.__font.render("STONE", True, (16, 16, 16)), (102, 86))
            self.__canvas.blit(self.__font.render("STONE", True, (64, 64, 64)), (100, 84))
        else:
            self.__canvas.blit(self.__imgPillNotTaken, (5, 90))
            self.__canvas.blit(self.__font.render("STONE", True, (128, 128, 128)), (102, 86))
            self.__canvas.blit(self.__font.render("STONE", True, (255, 255, 255)), (100, 84))

    @staticmethod
    def IsNotTakenToday():
        return not PillReminderScreen.__isColinTaken or not PillReminderScreen.__isStoneTaken
