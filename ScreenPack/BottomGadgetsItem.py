import pygame

from DataPack.CourtScreen import CourtScreen
from DataPack.Enum_ScreenType import ScreenType
from ScreenPack.F2_AlarmClockScreen import AlarmClockScreen
from ScreenPack.IScreen import IScreen
from ScreenPack.F1_TimeScreen import TimeScreen
from ScreenPack.F4_PillReminderScreen import PillReminderScreen
from Utility.SystemInfoHelper import SystemInfoHelper


class BottomGadgetsItem:

    def __init__(self):
        self.__canvas = pygame.display.get_surface()
        self.__font = pygame.font.Font("src/Font/Reckoner.ttf", 72)

        self.__imgAlarmClock = pygame.image.load('src/Icon/Bottom_Clock.png')
        self.__imgAlarmClockHalo = pygame.image.load('src/Icon/Bottom_ClockHalo.png')
        self.__imgAlarmClockWarning = pygame.image.load('src/Icon/Bottom_ClockWarning.png')
        self.__imgAlarmClockWorking = pygame.image.load('src/Icon/Bottom_ClockWorking.png')

        self.__imgPill = pygame.image.load('src/Icon/Bottom_Pill.png')
        self.__imgPillHalo = pygame.image.load('src/Icon/Bottom_PillHalo.png')
        self.__imgPillNotTaken = pygame.image.load('src/Icon/Bottom_PillNotTaken.png')

        self.__imgWeather = pygame.image.load('src/Icon/Bottom_Weather.png')
        self.__imgWeatherHalo = pygame.image.load('src/Icon/Bottom_WeatherHalo.png')

    def OnPaint(self):
        pygame.draw.line(self.__canvas, (96, 96, 96), (0, 400), (800, 400), 2)

        # Print current temperature
        _temperature = SystemInfoHelper.GetTemperature()
        _temperatureContent = str(_temperature) + "'C"
        if _temperature <= 60:
            IScreen.PaintShadowTextOffset(self.__canvas, self.__font, _temperatureContent, (255, 255, 224), (6, 403), 2)
        else:
            IScreen.PaintShadowTextOffset(self.__canvas, self.__font, _temperatureContent, (255, 255, 128), (6, 403), 2)

        # Print alarm clock related icon
        _location = (6, 466)
        if CourtScreen.screenType == ScreenType.AlarmClock:
            self.__canvas.blit(self.__imgAlarmClockHalo, (_location[0] - 4, _location[1] - 4))
        if AlarmClockScreen.IsCounting():
            if AlarmClockScreen.IsAboutToEnd() and TimeScreen.timeSecond % 2 == 0:
                self.__canvas.blit(self.__imgAlarmClockWarning, _location)
            else:
                self.__canvas.blit(self.__imgAlarmClockWorking, _location)
        else:
            self.__canvas.blit(self.__imgAlarmClock, _location)

        # Print pill related icon
        _location = (_location[0] + 132, _location[1])
        if CourtScreen.screenType == ScreenType.PillReminder:
            self.__canvas.blit(self.__imgPillHalo, (_location[0] - 4, _location[1] - 4))
        if PillReminderScreen.IsNotTakenToday():
            self.__canvas.blit(self.__imgPillNotTaken, _location)
        else:
            self.__canvas.blit(self.__imgPill, _location)

        # Print weather related icon
        _location = (_location[0] + 132, _location[1])
        if CourtScreen.screenType == ScreenType.Weather:
            self.__canvas.blit(self.__imgWeatherHalo, (_location[0] - 4, _location[1] - 4))
        self.__canvas.blit(self.__imgWeather, _location)
