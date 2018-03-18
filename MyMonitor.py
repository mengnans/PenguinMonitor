import pygame

from GadgetItem import GadgetItem
from Utility.FpsDisplayItem import FpsDisplayItem
from ScreenPack.AlarmClockPack.AlarmClockScreen import AlarmClockScreen
from ScreenPack.TimerPack.TimerScreen import TimerScreen


class MyMonitor:
    isAlarm = False

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((320, 240), 0, 32)
        self.gameScreenItem = TimerScreen()
        self.fpsItem = FpsDisplayItem()
        self.gadgetItem = GadgetItem()

        self.font = pygame.font.Font("src\\Font\\Inconsolata.otf", 38);
        MyMonitor.__GameLoop(self)

    def __GameLoop(self):
        while True:
            pygame.time.Clock().tick(5)
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

        _keyPressed = pygame.key.get_pressed()
        if _keyPressed[pygame.K_TAB]:
            if not self.isAlarm:
                self.gameScreenItem = AlarmClockScreen()
                self.isAlarm = True
            else:
                self.gameScreenItem = TimerScreen()
                self.isAlarm = False
