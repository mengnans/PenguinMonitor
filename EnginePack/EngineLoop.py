import time
import pygame

from Entity.Court import Court
from DataPack.Enum_ScreenType import ScreenType
from ScreenPack.IScreen import IScreen
from Entity.FpsDisplayItem import FpsDisplayItem


class EngineLoop:

    def __init__(self):
        self.__lastTickSecond = 0
        self.__lastTickMinute = 0
        self.__fpsItemPaint = FpsDisplayItem()

    def OnUpdate(self):
        self.__fpsItemPaint.Tick()
        _time = time.localtime()
        _isPaint = IScreen.isForceUpdate

        if Court.screenType == ScreenType.TimeAnalog:
            Court.screenTimeAnalogItem.OnKeyboardUpdate()
        if Court.screenType == ScreenType.TimeDigital:
            Court.screenTimeDigitalItem.OnKeyboardUpdate()
        if Court.screenType == ScreenType.CountDownTimer:
            Court.screenCountdownTimerItem.OnKeyboardUpdate()
        if Court.screenType == ScreenType.PillReminder:
            Court.screenPillReminderItem.OnKeyboardUpdate()
        if Court.screenType == ScreenType.PiInfo:
            Court.screenPiInfoItem.OnKeyboardUpdate()

        if self.__lastTickSecond != _time.tm_sec:
            self.__lastTickSecond = _time.tm_sec
            Court.screenTimeAnalogItem.OnUpdatePerSecond()
            Court.screenTimeDigitalItem.OnUpdatePerSecond()
            Court.screenCountdownTimerItem.OnUpdatePerSecond()
            Court.screenPillReminderItem.OnUpdatePerSecond()
            Court.screenPiInfoItem.OnUpdatePerSecond()
            _isPaint = True
            pass

        if self.__lastTickMinute != _time.tm_min:
            self.__lastTickMinute = _time.tm_min
            Court.screenTimeAnalogItem.OnUpdatePerMinute()
            Court.screenTimeDigitalItem.OnUpdatePerMinute()
            Court.screenCountdownTimerItem.OnUpdatePerMinute()
            Court.screenPillReminderItem.OnUpdatePerMinute()
            Court.screenPiInfoItem.OnUpdatePerMinute()
            pass

        if _isPaint:
            IScreen.isForceUpdate = False
            EngineLoop.__isPaint = False
            self.OnPaint()

    def OnPaint(self):
        pygame.display.get_surface().fill((0, 0, 0))
        Court.bottomGadget.OnPaint()
        if Court.screenType == ScreenType.TimeAnalog:
            Court.screenTimeAnalogItem.OnPaint()
        if Court.screenType == ScreenType.TimeDigital:
            Court.screenTimeDigitalItem.OnPaint()
        if Court.screenType == ScreenType.CountDownTimer:
            Court.screenCountdownTimerItem.OnPaint()
        if Court.screenType == ScreenType.PillReminder:
            Court.screenPillReminderItem.OnPaint()
        if Court.screenType == ScreenType.PiInfo:
            Court.screenPiInfoItem.OnPaint()
