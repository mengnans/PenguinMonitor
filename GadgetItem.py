import pygame

class GadgetItem:

    def __init__(self):
        self.canvas = pygame.display.get_surface()
        self.font = pygame.font.SysFont("arial", 12);

        self.imgCpu = pygame.image.load('src\\Icon\\Cpu.png')
        self.imgTemperature = pygame.image.load('src\\Icon\\Temperature.png')

    def Tick(self):
        self.canvas.blit(self.imgCpu, (300, 0))
