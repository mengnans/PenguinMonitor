import pygame

from ScreenPack.IScreen import IScreen
from Utility.KeyboardHelper import KeyboardHelper


class PillReminderScreen(IScreen):
    isColinTaken = False
    isStoneTaken = False

    def __init__(self):
        self.__canvas = pygame.display.get_surface()
        self.__font = pygame.font.Font("src/Font/Reckoner.ttf", 111)
        self.__imgPillNotTaken = pygame.image.load('src/Icon/Pill_NotTaken.png')
        self.__imgPillTaken = pygame.image.load('src/Icon/Pill_Taken.png')

    def OnUpdate(self):
        if KeyboardHelper.IsPress(pygame.K_c):
            PillReminderScreen.isColinTaken = not PillReminderScreen.isColinTaken
            IScreen.ForceUpdate()
        if KeyboardHelper.IsPress(pygame.K_s):
            PillReminderScreen.isStoneTaken = not PillReminderScreen.isStoneTaken
            IScreen.ForceUpdate()

    def OnPaint(self):
        if PillReminderScreen.isColinTaken:
            self.__canvas.blit(self.__imgPillTaken, (5, 5))
            self.__canvas.blit(self.__font.render("Colin", True, (16, 16, 16)), (102, 1))
            self.__canvas.blit(self.__font.render("Colin", True, (64, 64, 64)), (100, -1))
        else:
            self.__canvas.blit(self.__imgPillNotTaken, (5, 5))
            self.__canvas.blit(self.__font.render("Colin", True, (128, 128, 128)), (102, 1))
            self.__canvas.blit(self.__font.render("Colin", True, (255, 255, 255)), (100, -1))

        if PillReminderScreen.isStoneTaken:
            self.__canvas.blit(self.__imgPillTaken, (5, 105))
            self.__canvas.blit(self.__font.render("STONE", True, (16, 16, 16)), (102, 101))
            self.__canvas.blit(self.__font.render("STONE", True, (64, 64, 64)), (100, 99))
        else:
            self.__canvas.blit(self.__imgPillNotTaken, (5, 105))
            self.__canvas.blit(self.__font.render("STONE", True, (128, 128, 128)), (102, 101))
            self.__canvas.blit(self.__font.render("STONE", True, (255, 255, 255)), (100, 99))

        # if PillReminderScreen.isStoneTaken:
        #     self.__canvas.blit(self.__imgPillDark, (5, 95))
        #     self.__canvas.blit(self.__font.render("Stone", True, (128, 128, 128)), (22, 2))
        # else:
        #     self.__canvas.blit(self.__imgPillBright, (5, 95))
        #     self.__canvas.blit(self.__font.render("Stone", True, (128, 128, 128)), (22, 2))

    @staticmethod
    def IsNotTakenToday():
        return not PillReminderScreen.isColinTaken or not PillReminderScreen.isStoneTaken
