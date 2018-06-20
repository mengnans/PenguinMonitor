import pygame

from Entity.Court import Court
from DataPack.Enum_ScreenType import ScreenType
from ScreenPack.F5_PiInfoScreen import PiInfoScreen
from ScreenPack.IScreen import IScreen


class BottomGadgetsItem:

    def __init__(self):
        self.__canvas = pygame.display.get_surface()
        self.__font = pygame.font.Font("src/Font/Reckoner.ttf", 72)

        self.__imgAlarmClock = pygame.image.load('src/Icon/Bottom_Clock.png')
        self.__imgAlarmClockSelected = pygame.image.load('src/Icon/Bottom_ClockSelected.png')

        self.__imgCountDown = pygame.image.load('src/Icon/Bottom_Countdown.png')
        self.__imgCountDownSelected = pygame.image.load('src/Icon/Bottom_CountdownSelected.png')

        self.__imgPill = pygame.image.load('src/Icon/Bottom_Pill.png')
        self.__imgPillSelected = pygame.image.load('src/Icon/Bottom_PillSelected.png')

        self.__imgWeather = pygame.image.load('src/Icon/Bottom_Weather.png')
        self.__imgWeatherSelected = pygame.image.load('src/Icon/Bottom_WeatherSelected.png')

    def OnPaint(self):
        pygame.draw.line(self.__canvas, (192, 192, 192), (0, 400), (800, 400), 2)

        # Print current temperature
        _temperature = PiInfoScreen.GetTemperatureAverage()
        _temperatureContent = '%.2f' % _temperature + "'C"
        if _temperature <= 60:
            IScreen.PaintShadowTextOffset(self.__canvas, self.__font, _temperatureContent, (255, 255, 224), (6, 403), 2)
        else:
            IScreen.PaintShadowTextOffset(self.__canvas, self.__font, _temperatureContent, (255, 255, 128), (6, 403), 2)

        # Print alarm clock related icon
        _location = (2, 462)

        # Print pill related icon
        _location = (_location[0] + 132, _location[1])
        if Court.screenType == ScreenType.CountDownTimer:
            self.__canvas.blit(self.__imgCountDownSelected, (_location[0], _location[1]))
        else:
            self.__canvas.blit(self.__imgCountDown, _location)

        # Print pill related icon
        _location = (_location[0] + 132, _location[1])
        if Court.screenType == ScreenType.PillReminder:
            self.__canvas.blit(self.__imgPillSelected, (_location[0], _location[1]))
        else:
            self.__canvas.blit(self.__imgPill, _location)
