import time
import pygame

from ScreenPack.IScreen import IScreen


class TimerScreen(IScreen):

    def __init__(self):
        self.canvas = pygame.display.get_surface()
        self.font = pygame.font.Font("src\\Font\\Reckoner.ttf", 200)

    def OnUpdate(self):
        pass

    def OnPaint(self):
        _timeContent = time.strftime("%H:%M", time.localtime())
        # _renderText = self.font.render(_timeContent, True, (255, 255, 255))
        # _textpos = _renderText.get_rect()
        # pygame.draw.rect(self.canvas, (64, 64, 64), (20,18,_textpos[2],_textpos[3]), 1)
        self.canvas.blit(self.font.render(_timeContent, True, (128, 128, 128)), (22, 20))
        self.canvas.blit(self.font.render(_timeContent, True, (255, 255, 255)), (20, 18))

    def OnKeyDown(self):
        pass
