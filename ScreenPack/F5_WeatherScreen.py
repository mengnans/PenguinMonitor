
from ScreenPack.IScreen import IScreen
from weather import Weather, Unit
import pygame



class WeatherScreen(IScreen):

    def __init__(self):
        self.__canvas = pygame.display.get_surface()
        weather = Weather(unit=Unit.CELSIUS)
        lookup = weather.lookup(560743)
        condition = lookup.condition()
        print(condition.text())
        location = weather.lookup_by_location('melbourne')
        location.print_obj()
        print(location.wind())
        print(location.atmosphere())
        print(location.astronomy())
        print(location.image())
        print(location.condition())
        print(location.description())
        print(location.forecast())
        print(location.units())
        print(location.title())



    def OnUpdate(self):
        pass
        # _imagerect = self._image
        # self.__canvas.blit(self._image,_imagerect)

    def OnUpdatePerSecond(self):
        pass

    def OnUpdatePerMinute(self):
        pass

    def OnPaint(self):
        pass
