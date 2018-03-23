import pygame
import time

from DataPack.CourtScreen import CourtScreen
from DataPack.DataProgram import DataProgram
from DataPack.Enum_ScreenType import ScreenType
from EnginePack.EngineKeybord import EngineKeyboard
from EnginePack.EngineLoop import EngineLoop
from ScreenPack.BottomGadgetsItem import BottomGadgetsItem
from ScreenPack.F3_CountDownTimerScreen import CountDownTimerScreen
from ScreenPack.F9_PiInfoScreen import PiInfoScreen
from ScreenPack.IScreen import IScreen
from ScreenPack.F1_TimeScreen import TimeScreen
from ScreenPack.F2_AlarmClockScreen import AlarmClockScreen
from ScreenPack.F4_PillReminderScreen import PillReminderScreen
from ScreenPack.F5_WeatherScreen import WeatherScreen
from Utility.FpsDisplayItem import FpsDisplayItem
from Utility.InternetHelper import InternetHelper
from Utility.KeyboardHelper import KeyboardHelper
from Utility.SoundHelper import SoundHelper


class MyMonitor:

    def __init__(self):
        pygame.init()

        KeyboardHelper.Initial()
        SoundHelper.SetInitial()

        if DataProgram.IsDebugMode == True:
            self.__screen = pygame.display.set_mode((800, 600))
        else:
            self.__screen = pygame.display.set_mode((800, 600), pygame.FULLSCREEN)
        self.__InitScreens()
        self.__gameLoopItem = EngineLoop()
        self.__gameKeyboard = EngineKeyboard()
        MyMonitor.__GameLoop(self)

    def __InitScreens(self):
        PillReminderScreen.InitDataInfo()
        CourtScreen.screenTimeItem = TimeScreen()
        CourtScreen.screenAlarmClockItem = AlarmClockScreen()
        CourtScreen.screenCountdownTimerItem = CountDownTimerScreen()
        CourtScreen.screenPillReminderItem = PillReminderScreen()
        CourtScreen.screenWeatherItem = WeatherScreen()
        CourtScreen.screenPiInfoItem = PiInfoScreen()
        CourtScreen.screenType = ScreenType.Time
        CourtScreen.bottomGadget = BottomGadgetsItem()

    def __GameLoop(self):
        while True:
            pygame.time.Clock().tick(DataProgram.UpdatePerSecond)
            self.__gameKeyboard.OnUpdate()
            self.__gameLoopItem.OnUpdate()
            self.__GameEvent()
            pygame.display.update()

    def __GameEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
