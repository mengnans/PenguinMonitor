import time
import pygame

from ScreenPack.IScreen import IScreen


class TimerScreen(IScreen):

    def __init__(self):
        self.canvas = pygame.display.get_surface()

        self.font = pygame.font.Font("src\\Font\\Inconsolata.otf", 120)

    def Tick(self):
        _timeContent = time.strftime("%H:%M", time.localtime())
        # _renderText = self.font.render(_timeContent, True, (255, 255, 255))
        # _textpos = _renderText.get_rect()
        self.canvas.blit(self.font.render(_timeContent, True, (128, 128, 128)), (12, 20))
        self.canvas.blit(self.font.render(_timeContent, True, (255, 255, 255)), (10, 18))


    def OnKeydown(self):
        pass
