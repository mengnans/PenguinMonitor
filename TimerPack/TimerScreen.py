import time
import pygame

from EnginePack.IScreen import IScreen


class TimerScreen(IScreen):

    def __init__(self):
        self.canvas = pygame.display.get_surface()
        self.font = pygame.font.SysFont("arial", 128)

    def Tick(self):
        _timeContent = time.strftime("%H:%M", time.localtime())
        _renderText = self.font.render(_timeContent, True, (255, 255, 255))
        # _textpos = _renderText.get_rect()
        pygame.display.get_surface().blit(_renderText, (0, 8))

    def OnKeydown(self):
        pass
