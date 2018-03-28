from ScreenPack.IScreen import IScreen
from weather import Weather, Unit
import pygame
import time


class WeatherScreen(IScreen):
    def __init__(self):
        self.__canvas = pygame.display.get_surface()
        self.__weather = Weather(unit=Unit.CELSIUS)
        self.__lastUpdateHour = -1
        self.__font = pygame.font.Font("src/Font/Reckoner.ttf", 540)
        self.__currentWeather = 0

    def OnKeyboardUpdate(self):
        pass

    def OnUpdatePerSecond(self):
        _time = time.localtime()
        if self.__lastUpdateHour != _time.tm_hour:
            self.__lastUpdateHour = _time.tm_hour
            _location = self.__weather.lookup_by_location('melbourne')
            self.__currentWeather = _location.condition().temp() + '\'C'

    def OnUpdatePerMinute(self):
        pass

    def OnPaint(self):
        IScreen.PaintShadowText(self.__canvas, self.__font, self.__currentWeather, (255, 255, 255), (10, -17))
