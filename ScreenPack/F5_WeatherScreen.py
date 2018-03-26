
from ScreenPack.IScreen import IScreen
from weather import Weather, Unit
import pygame



class WeatherScreen(IScreen):

    def __init__(self):
        self.__canvas = pygame.display.get_surface()
        _weather = Weather(unit=Unit.CELSIUS)
        self.__location = _weather.lookup_by_location('melbourne')
        self.__font = pygame.font.Font("src/Font/Reckoner.ttf", 540)
        self.__currentWeather = 0

    def OnUpdate(self):
        pass

    def OnUpdatePerSecond(self):
        pass

    def OnUpdatePerMinute(self):
        # self.__currentWeather = self.__location.condition().temp() + '\'C'
        self.__currentWeather = self.__location.condition().temp() + '\''
        pass

    def OnPaint(self):
        # Draw temp value
        _renderText = self.__font.render(self.__currentWeather, True, (255, 255, 255))
        _recText = _renderText.get_rect()
        _locationX = 419 + (381 - (_recText[2] - 17)) / 2
        IScreen.PaintShadowText(self.__canvas, self.__font, self.__currentWeather, (255, 255, 255), (_locationX, -17))

