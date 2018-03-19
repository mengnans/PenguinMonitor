import pygame

from ScreenPack.IScreen import IScreen


class PillReminderScreen(IScreen):

    def __init__(self):
        self.canvas = pygame.display.get_surface()
        self.font = pygame.font.Font("src\\Font\\Targa MS.ttf", 200)

    def OnUpdate(self):
        pass

    def OnPaint(self):
        self.canvas.blit(self.font.render("TIME", True, (128, 128, 128)), (22, 20))
        self.canvas.blit(self.font.render("TIME", True, (255, 255, 0)), (20, 18))

    def OnKeyDown(self):
        pass
