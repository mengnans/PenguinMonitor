import pygame

from DataPack.DataWindow import DataWindow
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
            self.__canvas.blit(self.__imgPillTaken, (5, 4))
            self.__canvas.blit(self.__font.render("Colin", True, (16, 16, 16)), (102, 0))
            self.__canvas.blit(self.__font.render("Colin", True, (64, 64, 64)), (100, -2))
        else:
            self.__canvas.blit(self.__imgPillNotTaken, (5, 4))
            self.__canvas.blit(self.__font.render("Colin", True, (128, 128, 128)), (102, 0))
            self.__canvas.blit(self.__font.render("Colin", True, (255, 255, 255)), (100, -2))

        if PillReminderScreen.isStoneTaken:
            self.__canvas.blit(self.__imgPillTaken, (5, 90))
            self.__canvas.blit(self.__font.render("STONE", True, (16, 16, 16)), (102, 86))
            self.__canvas.blit(self.__font.render("STONE", True, (64, 64, 64)), (100, 84))
        else:
            self.__canvas.blit(self.__imgPillNotTaken, (5, 90))
            self.__canvas.blit(self.__font.render("STONE", True, (128, 128, 128)), (102, 86))
            self.__canvas.blit(self.__font.render("STONE", True, (255, 255, 255)), (100, 84))

        pygame.draw.line(self.__canvas, (64, 64, 64), (0, 175), (DataWindow.WindowsSize[0], 175), 1)

    @staticmethod
    def IsNotTakenToday():
        return not PillReminderScreen.isColinTaken or not PillReminderScreen.isStoneTaken
