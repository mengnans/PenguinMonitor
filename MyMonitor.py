import pygame
import time

from DataPack.CourtScreen import CourtScreen
from DataPack.DataWindow import DataWindow
from DataPack.Enum_ScreenType import ScreenType
from ScreenPack.BottomGadgetsItem import BottomGadgetsItem
from ScreenPack.IScreen import IScreen
from ScreenPack.TimeScreen import TimeScreen
from ScreenPack.AlarmClockScreen import AlarmClockScreen
from ScreenPack.PillReminderScreen import PillReminderScreen
from ScreenPack.WeatherScreen import WeatherScreen
from Utility.FpsDisplayItem import FpsDisplayItem
from Utility.KeyboardHelper import KeyboardHelper
from Utility.SoundHelper import SoundHelper


class MyMonitor:

    def __init__(self):
        pygame.init()
        KeyboardHelper.Update()
        SoundHelper.SetInitial()

        PillReminderScreen.InitDataInfo()

        self.__screen = pygame.display.set_mode((320, 240))
        # self.__screen = pygame.display.set_mode((320, 240), pygame.FULLSCREEN)
        CourtScreen.screenTimeItem = TimeScreen()
        CourtScreen.screenAlarmClockItem = AlarmClockScreen()
        CourtScreen.screenPillReminderItem = PillReminderScreen()
        CourtScreen.screenWeatherItem = WeatherScreen()
        CourtScreen.screenType = ScreenType.Time
        CourtScreen.bottomGadget = BottomGadgetsItem()
        self.__fpsItem = FpsDisplayItem()
        self.__lastTickSecond = 0
        MyMonitor.__GameLoop(self)

    def __GameLoop(self):
        while True:
            pygame.time.Clock().tick(DataWindow.UpdatePerSecond)
            KeyboardHelper.Update()
            self.__GameEvent()
            CourtScreen.screenTimeItem.OnUpdate()
            CourtScreen.screenAlarmClockItem.OnUpdate()
            CourtScreen.screenPillReminderItem.OnUpdate()
            CourtScreen.screenWeatherItem.OnUpdate()
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
        if CourtScreen.screenType == ScreenType.Time:
            CourtScreen.screenType = ScreenType.AlarmClock
        elif CourtScreen.screenType == ScreenType.AlarmClock:
            CourtScreen.screenType = ScreenType.PillReminder
        elif CourtScreen.screenType == ScreenType.PillReminder:
            CourtScreen.screenType = ScreenType.Weather
        elif CourtScreen.screenType == ScreenType.Weather:
            CourtScreen.screenType = ScreenType.Time

    def __GamePaint(self):
        pygame.display.get_surface().fill((0, 0, 0))
        if CourtScreen.screenType == ScreenType.Time:
            CourtScreen.screenTimeItem.OnPaint()
        if CourtScreen.screenType == ScreenType.AlarmClock:
            CourtScreen.screenAlarmClockItem.OnPaint()
        if CourtScreen.screenType == ScreenType.PillReminder:
            CourtScreen.screenPillReminderItem.OnPaint()
        if CourtScreen.screenType == ScreenType.Weather:
            CourtScreen.screenWeatherItem.OnPaint()
        CourtScreen.bottomGadget.OnPaint()
        self.__fpsItem.Tick()


_myMonitor = MyMonitor()
