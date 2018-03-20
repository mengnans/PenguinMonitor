import pygame
import time

from DataPack.Enum_ScreenType import ScreenType
from Utility.FpsDisplayItem import FpsDisplayItem
from ScreenPack.AlarmClockScreen import AlarmClockScreen
from ScreenPack.MainScreen import MainScreen
from Utility.KeyboardHelper import KeyboardHelper
from Utility.SoundHelper import SoundHelper


class MyMonitor:
    # TODO 这里要用枚举类型处理当前所在的Screen并做相应的更改
    __isAlarm = False
    __myMonitorItem = None
    __screenType = ScreenType.MainScreen

    def __init__(self):
        MyMonitor.__myMonitorItem = self
        pygame.init()
        KeyboardHelper.Update()
        SoundHelper.SetInitial()
        self.screen = pygame.display.set_mode((320, 240), 0, 32)
        self.gameScreenItem = MainScreen()
        self.fpsItem = FpsDisplayItem()
        self.lastTickSecond = 0
        MyMonitor.__GameLoop(self)

    def __GameLoop(self):
        while True:
            pygame.time.Clock().tick(12)
            KeyboardHelper.Update()
            if int(time.time()) != self.lastTickSecond:
                self.lastTickSecond = int(time.time())
                self.__GamePaint()

            self.__GameEvent()

            pygame.display.update()

    def __GameEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.key.set_repeat(1000, 500)
        _keyPressed = pygame.key.get_pressed()
        if _keyPressed[pygame.K_TAB]:
            if not self.__isAlarm:
                self.gameScreenItem = AlarmClockScreen()
                self.__isAlarm = True
            else:
                self.gameScreenItem = MainScreen()
                self.__isAlarm = False
            MyMonitor.ForceUpdate()

    def __GamePaint(self):
        pygame.display.get_surface().fill((0, 0, 0))
        self.gameScreenItem.OnPaint()
        self.fpsItem.Tick()

    def ForceUpdate():
        MyMonitor.__myMonitorItem.__GamePaint()


_myMonitor = MyMonitor()
