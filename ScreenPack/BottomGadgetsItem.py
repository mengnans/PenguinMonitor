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
        self.__imgAlarmClockSelected = pygame.image.load('src/Icon/Bottom_ClockSelected.png')
        self.__imgAlarmClockWorking = pygame.image.load('src/Icon/Bottom_ClockWorking.png')

        self.__imgPill = pygame.image.load('src/Icon/Bottom_Pill.png')
        self.__imgPillSelected = pygame.image.load('src/Icon/Bottom_PillSelected.png')

        self.__imgWeather = pygame.image.load('src/Icon/Bottom_Weather.png')
        self.__imgWeatherSelected = pygame.image.load('src/Icon/Bottom_WeatherSelected.png')

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
        _location = (2, 462)
        if CourtScreen.screenType == ScreenType.AlarmClock:
            self.__canvas.blit(self.__imgAlarmClockSelected, (_location[0], _location[1]))
        else:
            if AlarmClockScreen.IsCounting():
                self.__canvas.blit(self.__imgAlarmClockWorking, _location)
            else:
                self.__canvas.blit(self.__imgAlarmClock, _location)

        # Print pill related icon
        _location = (_location[0] + 132, _location[1])
        if CourtScreen.screenType == ScreenType.PillReminder:
            self.__canvas.blit(self.__imgPillSelected, (_location[0], _location[1]))
        else:
            self.__canvas.blit(self.__imgPill, _location)

        # Print weather related icon
        _location = (_location[0] + 132, _location[1])
        if CourtScreen.screenType == ScreenType.Weather:
            self.__canvas.blit(self.__imgWeatherSelected, (_location[0], _location[1]))
        else:
            self.__canvas.blit(self.__imgWeather, _location)
