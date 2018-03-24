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
        CourtScreen.screenCountdownTimerItem.OnUpdate()
        CourtScreen.screenPillReminderItem.OnUpdate()
        CourtScreen.screenWeatherItem.OnUpdate()
        CourtScreen.screenPiInfoItem.OnUpdate()

        if self.__lastTickSecond != _time.tm_sec:
            self.__lastTickSecond = _time.tm_sec
            CourtScreen.screenTimeItem.OnUpdatePerSecond()
            CourtScreen.screenAlarmClockItem.OnUpdatePerSecond()
            CourtScreen.screenCountdownTimerItem.OnUpdatePerSecond()
            CourtScreen.screenPillReminderItem.OnUpdatePerSecond()
            CourtScreen.screenWeatherItem.OnUpdatePerSecond()
            CourtScreen.screenPiInfoItem.OnUpdatePerSecond()
            _isPaint = True
            pass

        if self.__lastTickMinute != _time.tm_min:
            self.__lastTickMinute = _time.tm_min
            CourtScreen.screenTimeItem.OnUpdatePerMinute()
            CourtScreen.screenAlarmClockItem.OnUpdatePerMinute()
            CourtScreen.screenCountdownTimerItem.OnUpdatePerMinute()
            CourtScreen.screenPillReminderItem.OnUpdatePerMinute()
            CourtScreen.screenWeatherItem.OnUpdatePerMinute()
            CourtScreen.screenPiInfoItem.OnUpdatePerMinute()
            pass

        if _isPaint:
            IScreen.isForceUpdate = False
            EngineLoop.__isPaint = False
            self.OnPaint()

    def OnPaint(self):
        pygame.display.get_surface().fill((0, 0, 0))
        if CourtScreen.screenType == ScreenType.Time:
            CourtScreen.screenTimeItem.OnPaint()
        if CourtScreen.screenType == ScreenType.AlarmClock:
            CourtScreen.screenAlarmClockItem.OnPaint()
        if CourtScreen.screenType == ScreenType.CountDownTimer:
            CourtScreen.screenCountdownTimerItem.OnPaint()
        if CourtScreen.screenType == ScreenType.PillReminder:
            CourtScreen.screenPillReminderItem.OnPaint()
        if CourtScreen.screenType == ScreenType.Weather:
            CourtScreen.screenWeatherItem.OnPaint()
        if CourtScreen.screenType == ScreenType.PiInfo:
            CourtScreen.screenPiInfoItem.OnPaint()
        CourtScreen.bottomGadget.OnPaint()
        self.__fpsItem.Tick()
