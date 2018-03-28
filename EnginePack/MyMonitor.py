import json

import pygame

from DataPack.Court import Court
from DataPack.DataProgram import DataProgram
from DataPack.Enum_ScreenType import ScreenType
from EnginePack.EngineKeybord import EngineKeyboard
from EnginePack.EngineLoop import EngineLoop
from ScreenPack.BottomGadgetsItem import BottomGadgetsItem
from ScreenPack.F1_TimeScreen import TimeScreen
from ScreenPack.F2_AlarmClockScreen import AlarmClockScreen
from ScreenPack.F3_CountDownTimerScreen import CountDownTimerScreen
from ScreenPack.F4_PillReminderScreen import PillReminderScreen
from ScreenPack.F5_WeatherScreen import WeatherScreen
from ScreenPack.F9_PiInfoScreen import PiInfoScreen
from Utility.ConfigHelper import ConfigHelper
from Utility.KeyboardHelper import KeyboardHelper
from Utility.SoundHelper import SoundHelper


class MyMonitor:

    def __init__(self):
        pygame.init()

        ConfigHelper.LoadFromFile()
        KeyboardHelper.Initial()
        SoundHelper.SetInitial()

        if DataProgram.IsDebugMode is True:
            self.__screen = pygame.display.set_mode((800, 600))
        else:
            self.__screen = pygame.display.set_mode((800, 600), pygame.FULLSCREEN)
        self.__InitScreens()
        self.__gameLoopItem = EngineLoop()
        self.__gameKeyboard = EngineKeyboard()
        MyMonitor.__GameLoop(self)

    @staticmethod
    def __InitialData():
        print(json.dumps(Court.configItem))

    @staticmethod
    def __InitScreens():
        Court.screenTimeItem = TimeScreen()
        Court.screenAlarmClockItem = AlarmClockScreen()
        Court.screenCountdownTimerItem = CountDownTimerScreen()
        Court.screenPillReminderItem = PillReminderScreen()
        Court.screenWeatherItem = WeatherScreen()
        Court.screenPiInfoItem = PiInfoScreen()
        Court.screenType = ScreenType.Time
        Court.bottomGadget = BottomGadgetsItem()

    def __GameLoop(self):
        while True:
            pygame.time.Clock().tick(24)
            self.__gameKeyboard.OnUpdate()
            self.__gameLoopItem.OnUpdate()
            self.__GameEvent()
            pygame.display.update()

    def __GameEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
