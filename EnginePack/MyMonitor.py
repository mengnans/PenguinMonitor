import pygame

from Entity.Court import Court
from DataPack.DataProgram import DataProgram
from DataPack.Enum_ScreenType import ScreenType
from EnginePack.EngineKeybord import EngineKeyboard
from EnginePack.EngineLoop import EngineLoop
from ScreenPack.BottomGadgetsItem import BottomGadgetsItem
from ScreenPack.F1_TimeScreenAnalog import TimeScreenAnalog
from ScreenPack.F2_TimeScreenDigital import TimeScreenDigital
from ScreenPack.F3_CountDownTimerScreen import CountDownTimerScreen
from ScreenPack.F4_PillReminderScreen import PillReminderScreen
from ScreenPack.F5_PiInfoScreen import PiInfoScreen
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
    def __InitScreens():
        Court.screenTimeAnalogItem = TimeScreenAnalog()
        Court.screenTimeDigitalItem = TimeScreenDigital()
        Court.screenCountdownTimerItem = CountDownTimerScreen()
        Court.screenPillReminderItem = PillReminderScreen()
        Court.screenPiInfoItem = PiInfoScreen()
        Court.screenType = ScreenType.TimeAnalog
        Court.bottomGadget = BottomGadgetsItem()

    def __GameLoop(self):
        while True:
            pygame.time.Clock().tick(24)
            self.__gameKeyboard.OnUpdate()
            self.__gameLoopItem.OnUpdate()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            pygame.display.update()
