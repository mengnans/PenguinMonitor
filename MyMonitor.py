import pygame
import time

from DataPack.DataWindow import DataWindow
from DataPack.Enum_ScreenType import ScreenType
from ScreenPack.PillReminderScreen import PillReminderScreen
from Utility.FpsDisplayItem import FpsDisplayItem
from ScreenPack.AlarmClockScreen import AlarmClockScreen
from ScreenPack.MainScreen import MainScreen
from Utility.KeyboardHelper import KeyboardHelper
from Utility.SoundHelper import SoundHelper


class MyMonitor:
    # TODO 这里要用枚举类型处理当前所在的Screen并做相应的更改

    __isAlarm = False
    __myMonitorItem = None

    def __init__(self):
        MyMonitor.__myMonitorItem = self
        pygame.init()
        KeyboardHelper.Update()
        SoundHelper.SetInitial()
        self.__screen = pygame.display.set_mode((320, 240), 0, 32)
        self.__gameScreenItem = MainScreen()
        self.__screenType = ScreenType.MainScreen
        self.__fpsItem = FpsDisplayItem()
        self.__lastTickSecond = 0
        MyMonitor.__GameLoop(self)

    def __GameLoop(self):
        while True:
            pygame.time.Clock().tick(DataWindow.UpdatePerSecond)
            KeyboardHelper.Update()
            self.__GameEvent()
            if int(time.time()) != self.__lastTickSecond:
                self.__lastTickSecond = int(time.time())
                self.__GamePaint()
            pygame.display.update()

    def __GameEvent(self):
        if KeyboardHelper.IsPress(pygame.K_TAB):
            self.__ChangeScreen()
            MyMonitor.ForceUpdate()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


    def __ChangeScreen(self):
        if self.__screenType == ScreenType.MainScreen:
            self.__screenType = ScreenType.AlarmClock
            self.__gameScreenItem = AlarmClockScreen()
        elif self.__screenType == ScreenType.AlarmClock:
            self.__screenType = ScreenType.PillReminder
            self.__gameScreenItem = PillReminderScreen()
        elif self.__screenType == ScreenType.PillReminder:
            self.__screenType = ScreenType.MainScreen
            self.__gameScreenItem = MainScreen()

    def __GamePaint(self):
        pygame.display.get_surface().fill((0, 0, 0))
        self.__gameScreenItem.OnPaint()
        self.__fpsItem.Tick()

    def ForceUpdate():
        MyMonitor.__myMonitorItem.__GamePaint()


_myMonitor = MyMonitor()
