import time
import pygame

from DataPack.Court import Court
from DataPack.Enum_ScreenType import ScreenType
from ScreenPack.IScreen import IScreen
from Utility.FpsDisplayItem import FpsDisplayItem


class EngineLoop:

    def __init__(self):
        self.__lastTickSecond = 0
        self.__lastTickMinute = 0
        self.__fpsItemPaint = FpsDisplayItem()

    def OnUpdate(self):
        self.__fpsItemPaint.Tick()
        _time = time.localtime()
        _isPaint = IScreen.isForceUpdate

        if Court.screenType == ScreenType.Time:
            Court.screenTimeItem.OnKeyboardUpdate()
        if Court.screenType == ScreenType.AlarmClock:
            Court.screenAlarmClockItem.OnKeyboardUpdate()
        if Court.screenType == ScreenType.CountDownTimer:
            Court.screenCountdownTimerItem.OnKeyboardUpdate()
        if Court.screenType == ScreenType.PillReminder:
            Court.screenPillReminderItem.OnKeyboardUpdate()
        if Court.screenType == ScreenType.Weather:
            Court.screenWeatherItem.OnKeyboardUpdate()
        if Court.screenType == ScreenType.PiInfo:
            Court.screenPiInfoItem.OnKeyboardUpdate()

        if self.__lastTickSecond != _time.tm_sec:
            self.__lastTickSecond = _time.tm_sec
            Court.screenTimeItem.OnUpdatePerSecond()
            Court.screenAlarmClockItem.OnUpdatePerSecond()
            Court.screenCountdownTimerItem.OnUpdatePerSecond()
            Court.screenPillReminderItem.OnUpdatePerSecond()
            Court.screenWeatherItem.OnUpdatePerSecond()
            Court.screenPiInfoItem.OnUpdatePerSecond()
            _isPaint = True
            pass

        if self.__lastTickMinute != _time.tm_min:
            self.__lastTickMinute = _time.tm_min
            Court.screenTimeItem.OnUpdatePerMinute()
            Court.screenAlarmClockItem.OnUpdatePerMinute()
            Court.screenCountdownTimerItem.OnUpdatePerMinute()
            Court.screenPillReminderItem.OnUpdatePerMinute()
            Court.screenWeatherItem.OnUpdatePerMinute()
            Court.screenPiInfoItem.OnUpdatePerMinute()
            pass

        if _isPaint:
            IScreen.isForceUpdate = False
            EngineLoop.__isPaint = False
            self.OnPaint()

    def OnPaint(self):
        pygame.display.get_surface().fill((0, 0, 0))
        if Court.screenType == ScreenType.Time:
            Court.screenTimeItem.OnPaint()
        if Court.screenType == ScreenType.AlarmClock:
            Court.screenAlarmClockItem.OnPaint()
        if Court.screenType == ScreenType.CountDownTimer:
            Court.screenCountdownTimerItem.OnPaint()
        if Court.screenType == ScreenType.PillReminder:
            Court.screenPillReminderItem.OnPaint()
        if Court.screenType == ScreenType.Weather:
            Court.screenWeatherItem.OnPaint()
        if Court.screenType == ScreenType.PiInfo:
            Court.screenPiInfoItem.OnPaint()
        Court.bottomGadget.OnPaint()
