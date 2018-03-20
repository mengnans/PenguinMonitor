import time
from datetime import date
import calendar
import pygame

from ScreenPack.IScreen import IScreen
from DataPack.DataWindow import DataWindow


class MainScreen(IScreen):

    def __init__(self):
        self.__canvas = pygame.display.get_surface()
        self.__font = pygame.font.Font("src\\Font\\Reckoner.ttf", 200)
        self.__fontSmall = pygame.font.Font("src\\Font\\Reckoner.ttf", 58)
        self.__imgPillBright = pygame.image.load('src\\Icon\\PillBright.png')
        self.__imgPillDark = pygame.image.load('src\\Icon\\PillDark.png')

    def OnUpdate(self):
        pass

    def OnPaint(self):
        self.__PaintTime()
        pygame.draw.line(self.__canvas, (64, 64, 64), (0, 175), (DataWindow.WindowsSize[0], 175), 1)
        self.__PaintGadget()

    def __PaintTime(self):
        # TODO: the code here can be optimized

        _time = time.localtime()
        _timeHour = _time.tm_hour
        _timeMinute = _time.tm_min
        _timeContent = str(_timeHour) + ":" + str(_timeMinute)

        _renderText = self.__font.render(_timeContent, True, (255, 255, 255))
        _recText = _renderText.get_rect()
        _locationX = (DataWindow.WindowsSize[0] - (_recText[2] - 10)) / 2
        # TODO: try to change the name of attribute, it's hard to understand
        # pygame.draw.rect(self.canvas, (64, 64, 64), (10, 0, _recText[2], _recText[3]), 1)
        # # self.canvas.draw.text(_timeContent, (0, 0), self.font)
        self.__canvas.blit(self.__font.render(_timeContent, True, (128, 128, 128)), (_locationX + 2, 8))
        self.__canvas.blit(self.__font.render(_timeContent, True, (255, 255, 255)), (_locationX, 5))

    def __PaintGadget(self):
        self.__canvas.blit(self.__imgPillDark, (264, 184))
        _dateToday = date.today()
        _bottomContent = calendar.month_name[_dateToday.month]
        _bottomContent += ' ' + calendar.day_name[_dateToday.weekday()]
        _bottomContent = _bottomContent.upper()
        self.__canvas.blit(self.__fontSmall.render(_bottomContent, True, (128, 128, 128)), (9, 186))
        self.__canvas.blit(self.__fontSmall.render(_bottomContent, True, (255, 255, 255)), (7, 184))

    def OnKeyDown(self):
        pass
