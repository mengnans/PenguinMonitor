import pygame

from DataPack.CourtScreen import CourtScreen
from DataPack.Enum_ScreenType import ScreenType
from ScreenPack.IScreen import IScreen
from Utility.KeyboardHelper import KeyboardHelper


class EngineKeyboard:
    def __init__(self):
        pass

    def OnUpdate(self):
        KeyboardHelper.Update()
        self.__FuncKeyChangeScreen()
        if KeyboardHelper.IsPress(pygame.K_TAB):
            self.__ChangeNextScreen()
        if KeyboardHelper.IsPress(pygame.K_q):
            pygame.quit()
            exit()

    def __FuncKeyChangeScreen(self):
        if KeyboardHelper.IsPress(pygame.K_F1):
            CourtScreen.screenType = ScreenType.Time
        if KeyboardHelper.IsPress(pygame.K_F2):
            CourtScreen.screenType = ScreenType.AlarmClock
        if KeyboardHelper.IsPress(pygame.K_F3):
            CourtScreen.screenType = ScreenType.PillReminder
        if KeyboardHelper.IsPress(pygame.K_F4):
            CourtScreen.screenType = ScreenType.Weather
        # if KeyboardHelper.IsPress(pygame.K_F9):
        #     CourtScreen.screenType = ScreenType.Time

    def __ChangeNextScreen(self):
        if CourtScreen.screenType == ScreenType.Time:
            CourtScreen.screenType = ScreenType.AlarmClock
        elif CourtScreen.screenType == ScreenType.AlarmClock:
            CourtScreen.screenType = ScreenType.PillReminder
        elif CourtScreen.screenType == ScreenType.PillReminder:
            CourtScreen.screenType = ScreenType.Weather
        elif CourtScreen.screenType == ScreenType.Weather:
            CourtScreen.screenType = ScreenType.Time
        IScreen.ForceUpdate()
