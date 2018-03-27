from ScreenPack.IScreen import IScreen
from weather import Weather, Unit
import pygame


class WeatherScreen(IScreen):
    def __init__(self):
        self.__canvas = pygame.display.get_surface()
        self.__weather = Weather(unit=Unit.CELSIUS)

        self.__font = pygame.font.Font("src/Font/Reckoner.ttf", 540)
        self.__currentWeather = 0

    def OnUpdate(self):
        pass

    def OnUpdatePerSecond(self):
        _location = self.__weather.lookup_by_location('melbourne')
        # self.__currentWeather = self.__location.condition().temp() + '\'C'
        self.__currentWeather = _location.condition().temp() + '\'C'

    def OnUpdatePerMinute(self):
        pass

    def OnPaint(self):
        IScreen.PaintShadowText(self.__canvas, self.__font, self.__currentWeather, (255, 255, 255), (10, -17))
