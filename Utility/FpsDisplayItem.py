import time
import pygame


class FpsDisplayItem:

    def __init__(self):
        self.fps = 0
        self.fpsTick = 0
        self.second = 0

        self.canvas = pygame.display.get_surface()
        self.font = pygame.font.Font("src\\Font\\Reckoner.ttf", 18)

    def Tick(self):
        if int(time.time()) == self.second:
            self.fpsTick = self.fpsTick + 1
        else:
            self.second = int(time.time())
            self.fps = self.fpsTick
            self.fpsTick = 0

        self.canvas.blit(self.font.render("FPS: " + str(self.fps), True, (128, 128, 128)), (3, 3))
