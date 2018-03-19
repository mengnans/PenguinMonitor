import time
from datetime import date
import calendar
import pygame

from ScreenPack.IScreen import IScreen
from DataPack.DataWindow import DataWindow


class TimerScreen(IScreen):

    def __init__(self):
        self.canvas = pygame.display.get_surface()
        self.font = pygame.font.Font("src\\Font\\Reckoner.ttf", 200)
        self.imgPillBright = pygame.image.load('src\\Icon\\PillBright.png')
        self.imgPillDark = pygame.image.load('src\\Icon\\PillDark.png')

    def OnUpdate(self):
        pass

    def OnPaint(self):
        # TODO: the code here can be optimized
        self.__PaintTime()
        pygame.draw.line(self.canvas, (64, 64, 64), (0, 175), (DataWindow.WindowsSize[0], 175), 1)
        self.__PaintGadget()

    def __PaintTime(self):
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
        # pygame.draw.line(self.canvas, (64, 64, 64), (0, 175), (DataWindow.WindowsSize[0], 240), 1)
        # pygame.draw.line(self.canvas, (64, 64, 64), (0, 240), (DataWindow.WindowsSize[0], 175), 1)
        self.canvas.blit(self.imgPillDark, (264, 184))

        self.font = pygame.font.Font("src\\Font\\Reckoner.ttf", 58)
        _date_today = date.today()
        _weekdayContent = calendar.day_name[_date_today.weekday()][:3]
        _renderText = self.font.render(_weekdayContent, True, (255, 255, 255))
        _recText = _renderText.get_rect()
        # pygame.draw.rect(self.canvas, (64, 64, 64), (10, 0, _recText[2], _recText[3]), 1)
        # # self.canvas.draw.text(_timeContent, (0, 0), self.font)
        self.canvas.blit(self.font.render(_weekdayContent, True, (128, 128, 128)), (7, 186))
        self.canvas.blit(self.font.render(_weekdayContent, True, (255, 255, 255)), (5, 184))


    def OnKeyDown(self):
        pass
