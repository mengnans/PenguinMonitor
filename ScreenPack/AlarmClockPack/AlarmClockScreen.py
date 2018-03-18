import pygame

from ScreenPack.IScreen import IScreen


class AlarmClockScreen(IScreen):

    def __init__(self):
        self.canvas = pygame.display.get_surface()
        self.font = pygame.font.Font("src\\Font\\Inconsolata.otf", 128);

    def Tick(self):
        self.canvas.blit(self.font.render("Alarm Clock", True, (128, 128, 128)), (12, 20))
        self.canvas.blit(self.font.render("Alarm Clock", True, (255, 255, 255)), (10, 18))
        pass

    def OnKeydown(self):
        pass
