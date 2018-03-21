import pygame
import time

from ScreenPack.IScreen import IScreen
from Utility.KeyboardHelper import KeyboardHelper
from Utility.SoundHelper import SoundHelper


class PillReminderScreen(IScreen):
    __isColinTaken = False
    __isStoneTaken = False

    __dataFileName = "pillData.txt"

    def __init__(self):
        self.__canvas = pygame.display.get_surface()
        self.__font = pygame.font.Font("src/Font/Reckoner.ttf", 111)
        self.__imgPillNotTaken = pygame.image.load('src/Icon/Pill_NotTaken.png')
        self.__imgPillTaken = pygame.image.load('src/Icon/Pill_Taken.png')

    @staticmethod
    def InitDataInfo():
        _readFile = None
        try:
            PillReminderScreen.__isColinTaken = False
            PillReminderScreen.__isStoneTaken = False
            _readFile = open(PillReminderScreen.__dataFileName, "r")
            _rawContent = _readFile.read()

            _time = time.localtime()
            if _rawContent[0:4] == '%02d' % _time.tm_mon + '%02d' % _time.tm_mday:
                if _rawContent[5:6] == "C":
                    PillReminderScreen.__isColinTaken = True
                if _rawContent[6:7] == "S":
                    PillReminderScreen.__isStoneTaken = True
            _readFile.close()
        except:
            if _readFile is not None:
                _readFile.close()

    def OnUpdate(self):
        if KeyboardHelper.IsPress(pygame.K_c):
            PillReminderScreen.__isColinTaken = not PillReminderScreen.__isColinTaken
            self.WriteToFile()
            IScreen.ForceUpdate()
        if KeyboardHelper.IsPress(pygame.K_s):
            PillReminderScreen.__isStoneTaken = not PillReminderScreen.__isStoneTaken
            self.WriteToFile()
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

    def WriteToFile(self):
        __recordFile = open(PillReminderScreen.__dataFileName, "w")

        _time = time.localtime()
        _content = '%02d' % _time.tm_mon + '%02d' % _time.tm_mday + " "
        if PillReminderScreen.__isColinTaken == True:
            _content = _content + "C"
        else:
            _content = _content + "c"
        if PillReminderScreen.__isStoneTaken == True:
            _content = _content + "S"
        else:
            _content = _content + "s"
        __recordFile.write(_content)
        __recordFile.flush()
        __recordFile.close()
        if PillReminderScreen.__isColinTaken and PillReminderScreen.__isStoneTaken:
            SoundHelper.PlaySound("src/Music/Speech_AllMedicineTaken.wav")

    @staticmethod
    def IsNotTakenToday():
        return not PillReminderScreen.__isColinTaken or not PillReminderScreen.__isStoneTaken
