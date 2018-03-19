import time
from datetime import date
import calendar
import pygame

from ScreenPack.IScreen import IScreen
from DataPack.DataWindow import DataWindow


class MainScreen(IScreen):

    def __init__(self):
        self.canvas = pygame.display.get_surface()
        self.font = pygame.font.Font("src\\Font\\Reckoner.ttf", 200)
        self.fontSmall = pygame.font.Font("src\\Font\\Reckoner.ttf", 58)
        self.imgPillBright = pygame.image.load('src\\Icon\\PillBright.png')
        self.imgPillDark = pygame.image.load('src\\Icon\\PillDark.png')

    def OnUpdate(self):
        pass

    def OnPaint(self):
        self.__PaintTime()
        pygame.draw.line(self.canvas, (64, 64, 64), (0, 175), (DataWindow.WindowsSize[0], 175), 1)
        self.__PaintGadget()

    def __PaintTime(self):
        # TODO: the code here can be optimized
        self.font = pygame.font.Font("src\\Font\\Reckoner.ttf", 200)
        _timeContent = time.strftime("%H:%M", time.localtime())
        _renderText = self.font.render(_timeContent, True, (255, 255, 255))
        _recText = _renderText.get_rect()
        # TODO: try to change the name of attribute, it's hard to understand
        _locationX = (DataWindow.WindowsSize[0] - (_recText[2] - 10)) / 2
        # pygame.draw.rect(self.canvas, (64, 64, 64), (10, 0, _recText[2], _recText[3]), 1)
        # # self.canvas.draw.text(_timeContent, (0, 0), self.font)
        self.canvas.blit(self.font.render(_timeContent, True, (128, 128, 128)), (_locationX + 2, 8))
        self.canvas.blit(self.font.render(_timeContent, True, (255, 255, 255)), (_locationX, 5))

    def __PaintGadget(self):
        self.canvas.blit(self.imgPillDark, (264, 184))
        _dateToday = date.today()
        _bottomContent = calendar.month_name[_dateToday.month]
        _bottomContent += ' ' + calendar.day_name[_dateToday.weekday()]
        _bottomContent = _bottomContent.upper()
        self.canvas.blit(self.fontSmall.render(_bottomContent, True, (128, 128, 128)), (9, 186))
        self.canvas.blit(self.fontSmall.render(_bottomContent, True, (255, 255, 255)), (7, 184))

    def OnKeyDown(self):
        pass
