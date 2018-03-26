import pygame

from DataPack.Court import Court
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
            Court.screenType = ScreenType.Time
            IScreen.ForceUpdate()
        if KeyboardHelper.IsPress(pygame.K_F2):
            Court.screenType = ScreenType.AlarmClock
            IScreen.ForceUpdate()
        if KeyboardHelper.IsPress(pygame.K_F3):
            Court.screenType = ScreenType.CountDownTimer
            IScreen.ForceUpdate()
        if KeyboardHelper.IsPress(pygame.K_F4):
            Court.screenType = ScreenType.PillReminder
            IScreen.ForceUpdate()
        if KeyboardHelper.IsPress(pygame.K_F5):
            Court.screenType = ScreenType.Weather
            IScreen.ForceUpdate()
        if KeyboardHelper.IsPress(pygame.K_F9):
            Court.screenType = ScreenType.PiInfo
            IScreen.ForceUpdate()

    def __ChangeNextScreen(self):
        if Court.screenType == ScreenType.Time:
            Court.screenType = ScreenType.AlarmClock
        elif Court.screenType == ScreenType.AlarmClock:
            Court.screenType = ScreenType.CountDownTimer
        elif Court.screenType == ScreenType.CountDownTimer:
            Court.screenType = ScreenType.PillReminder
        elif Court.screenType == ScreenType.PillReminder:
            Court.screenType = ScreenType.Weather
        elif Court.screenType == ScreenType.Weather:
            Court.screenType = ScreenType.Time
        IScreen.ForceUpdate()
