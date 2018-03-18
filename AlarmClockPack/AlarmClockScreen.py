import pygame

from EnginePack.IScreen import IScreen


class AlarmClockScreen(IScreen):

    def __init__(self):
        self.canvas = pygame.display.get_surface()
        self.font = pygame.font.SysFont("arial", 128);

    def Tick(self):
        print("AlarmClock")
        pass

    def OnKeydown(self):
        pass
