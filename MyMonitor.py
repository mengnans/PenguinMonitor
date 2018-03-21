import pygame
import time

from DataPack.CourtScreen import CourtScreen
from DataPack.DataWindow import DataWindow
from DataPack.Enum_ScreenType import ScreenType
from ScreenPack.BottomGadgetsItem import BottomGadgetsItem
from ScreenPack.IScreen import IScreen
from ScreenPack.TimeScreen import MainScreen
from ScreenPack.AlarmClockScreen import AlarmClockScreen
from ScreenPack.PillReminderScreen import PillReminderScreen
from Utility.FpsDisplayItem import FpsDisplayItem
from Utility.KeyboardHelper import KeyboardHelper
from Utility.SoundHelper import SoundHelper


class MyMonitor:

    def __init__(self):
        pygame.init()
        KeyboardHelper.Update()
        SoundHelper.SetInitial()
        self.__screen = pygame.display.set_mode((320, 240))
        # self.__screen = pygame.display.set_mode((320, 240), pygame.FULLSCREEN)
        CourtScreen.screenItem = MainScreen()
        # CourtScreen.screenItem = AlarmClockScreen()
        # CourtScreen.screenItem = PillReminderScreen()
        CourtScreen.screenType = ScreenType.MainScreen
        CourtScreen.bottomGadget = BottomGadgetsItem()
        self.__fpsItem = FpsDisplayItem()
        self.__lastTickSecond = 0
        MyMonitor.__GameLoop(self)

    def __GameLoop(self):
        while True:
            pygame.time.Clock().tick(DataWindow.UpdatePerSecond)
            KeyboardHelper.Update()
            self.__GameEvent()
            CourtScreen.screenItem.OnUpdate()
            if IScreen.isForceUpdate or int(time.time()) != self.__lastTickSecond:
                IScreen.isForceUpdate = False
                self.__lastTickSecond = int(time.time())
                self.__GamePaint()
            pygame.display.update()

    def __GameEvent(self):
        if KeyboardHelper.IsPress(pygame.K_TAB):
            MyMonitor.__ChangeScreen()
            IScreen.ForceUpdate()
        if KeyboardHelper.IsPress(pygame.K_q):
            pygame.quit()
            exit()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    @staticmethod
    def __ChangeScreen():
        if CourtScreen.screenType == ScreenType.MainScreen:
            CourtScreen.screenType = ScreenType.AlarmClock
            CourtScreen.screenItem = AlarmClockScreen()
        elif CourtScreen.screenType == ScreenType.AlarmClock:
            CourtScreen.screenType = ScreenType.PillReminder
            CourtScreen.screenItem = PillReminderScreen()
        elif CourtScreen.screenType == ScreenType.PillReminder:
            CourtScreen.screenType = ScreenType.MainScreen
            CourtScreen.screenItem = MainScreen()

    def __GamePaint(self):
        pygame.display.get_surface().fill((0, 0, 0))
        CourtScreen.screenItem.OnPaint()
        CourtScreen.bottomGadget.OnPaint()
        self.__fpsItem.Tick()


_myMonitor = MyMonitor()
