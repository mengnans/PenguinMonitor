import time
import pygame

from ScreenPack.IScreen import IScreen
from DataPack.DataWindow import DataWindow


class TimerScreen(IScreen):

    def __init__(self):
        self.canvas = pygame.display.get_surface()
        self.font = pygame.font.Font("src\\Font\\Reckoner.ttf", 200)

    def OnUpdate(self):
        pass

    def OnPaint(self):
        # 这里可以做性能优化，这个优化很重要
        self.__PaintTime()
        pygame.draw.line(self.canvas, (64, 64, 64), (0, 174), (DataWindow.WindowsSize[0], 174), 1)
        self.__PaintGadget()

    def __PaintTime(self):
        _timeContent = time.strftime("%H:%M", time.localtime())
        _renderText = self.font.render(_timeContent, True, (255, 255, 255))
        _recText = _renderText.get_rect()
        _locationX = (DataWindow.WindowsSize[0] - (_recText[2] - 10)) / 2
        # pygame.draw.rect(self.canvas, (64, 64, 64), (10, 0, _recText[2], _recText[3]), 1)
        # # self.canvas.draw.text(_timeContent, (0, 0), self.font)
        self.canvas.blit(self.font.render(_timeContent, True, (128, 128, 128)), (_locationX + 2, 8))
        self.canvas.blit(self.font.render(_timeContent, True, (255, 255, 255)), (_locationX, 5))

    def __PaintGadget(self):
        pygame.draw.line(self.canvas, (64, 64, 64), (0, 174), (DataWindow.WindowsSize[0], 240), 1)
        pygame.draw.line(self.canvas, (64, 64, 64), (0, 240), (DataWindow.WindowsSize[0], 174), 1)

    def OnKeyDown(self):
        pass
