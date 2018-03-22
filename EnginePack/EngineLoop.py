import time
import pygame

from DataPack.CourtScreen import CourtScreen
from DataPack.Enum_ScreenType import ScreenType
from ScreenPack.IScreen import IScreen
from Utility.FpsDisplayItem import FpsDisplayItem


class EngineLoop:

    def __init__(self):
        self.__lastTickSecond = 0
        self.__lastTickMinute = 0
        self.__fpsItem = FpsDisplayItem()

    def OnUpdate(self):
        _time = time.localtime()
        _isPaint = IScreen.isForceUpdate

        CourtScreen.screenTimeItem.OnUpdate()
        CourtScreen.screenAlarmClockItem.OnUpdate()
        CourtScreen.screenPillReminderItem.OnUpdate()
        CourtScreen.screenWeatherItem.OnUpdate()

        if self.__lastTickSecond != _time.tm_sec:
            CourtScreen.screenTimeItem.OnUpdateSecond()
            CourtScreen.screenAlarmClockItem.OnUpdateSecond()
            CourtScreen.screenPillReminderItem.OnUpdateSecond()
            CourtScreen.screenWeatherItem.OnUpdateSecond()
            _isPaint = True
            self.__lastTickSecond = True
            pass

        if self.__lastTickSecond != _time.tm_min:
            CourtScreen.screenTimeItem.OnUpdateMinute()
            CourtScreen.screenAlarmClockItem.OnUpdateMinute()
            CourtScreen.screenPillReminderItem.OnUpdateMinute()
            CourtScreen.screenWeatherItem.OnUpdateMinute()
            _isPaint = True
            self.__lastTickMinute = True
            pass

        if _isPaint:
            EngineLoop.__isPaint = False
            self.OnPaint()

    def OnPaint(self):
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
