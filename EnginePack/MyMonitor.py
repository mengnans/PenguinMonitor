import pygame

from AlarmClockPack.AlarmClockScreen import AlarmClockScreen
from EnginePack.GadgetItem import GadgetItem
from TimerPack.TimerScreen import TimerScreen
from Utility.FpsDisplayItem import FpsDisplayItem


class MyMonitor:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((320, 240), 0, 32)
        self.gameScreenItem = TimerScreen()
        self.fpsItem = FpsDisplayItem()
        self.gadgetItem = GadgetItem()

        self.font = pygame.font.SysFont("arial", 38);
        MyMonitor.__GameLoop(self)

    def __GameLoop(self):
        while True:
            pygame.time.Clock().tick(8)
            pygame.display.get_surface().fill((0, 0, 0))

            self.gadgetItem.Tick()
            self.fpsItem.Tick()

            self.__GameEvent()
            self.gameScreenItem.Tick()

            pygame.display.update()

    def __GameEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.K_0:
                print("000000000000000")
        _keyPressed = pygame.key.get_pressed()
        if _keyPressed[pygame.K_TAB]:
            self.gameScreenItem = AlarmClockScreen()
            print("000000000000000")
