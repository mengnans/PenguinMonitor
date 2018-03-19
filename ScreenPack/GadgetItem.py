import pygame

from Utility.SystemInfoHelper import *


class GadgetItem:

    def __init__(self):
        self.canvas = pygame.display.get_surface()
        self.font = pygame.font.Font("src\\Font\\Inconsolata.otf", 18)

        self.imgCpu = pygame.image.load('src\\Icon\\Cpu.png')
        self.imgTemperature = pygame.image.load('src\\Icon\\Temperature.png')

    def OnPaint(self):
        # self.canvas.blit(self.imgCpu, (250, 190))
        # _cpuUsage = GetTemperature()
        # self.canvas.blit(self.font.render(_cpuUsage, True, (128, 128, 128)), (260, 190))
        pass
