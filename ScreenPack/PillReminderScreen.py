import pygame

from ScreenPack.IScreen import IScreen
from Utility.KeyboardHelper import KeyboardHelper


class PillReminderScreen(IScreen):
    isColinTaken = True
    isStoneTaken = True

    def __init__(self):
        self.__canvas = pygame.display.get_surface()
        self.__font = pygame.font.Font("src/Font/Reckoner.ttf", 64)
        self.__imgPillBright = pygame.image.load('src/Icon/Pill80Bright.png')
        self.__imgPillDark = pygame.image.load('src/Icon/Pill80Dark.png')

    def OnUpdate(self):
        if KeyboardHelper.IsPress(pygame.K_c):
            PillReminderScreen.isColinTaken = not PillReminderScreen.isColinTaken
            IScreen.ForceUpdate()
        pass

    def OnPaint(self):
        if PillReminderScreen.isColinTaken:
            self.__canvas.blit(self.__imgPillDark, (5, 5))
            self.__canvas.blit(self.__font.render("Colin", True, (128, 128, 128)), (100, 2))
        else:
            self.__canvas.blit(self.__imgPillBright, (5, 5))
            self.__canvas.blit(self.__font.render("Colin", True, (128, 128, 128)), (22, 2))

        # if PillReminderScreen.isStoneTaken:
        #     self.__canvas.blit(self.__imgPillDark, (5, 95))
        #     self.__canvas.blit(self.__font.render("Stone", True, (128, 128, 128)), (22, 2))
        # else:
        #     self.__canvas.blit(self.__imgPillBright, (5, 95))
        #     self.__canvas.blit(self.__font.render("Stone", True, (128, 128, 128)), (22, 2))

    @staticmethod
    def IsNotTakenToday():
        return not PillReminderScreen.isColinTaken or not PillReminderScreen.isStoneTaken
