import pygame

from ScreenPack.AlarmClockScreen import AlarmClockScreen
from DataPack.DataWindow import DataWindow
from ScreenPack.MainScreen import MainScreen
from ScreenPack.PillReminderScreen import PillReminderScreen
from Utility.SystemInfoHelper import SystemInfoHelper


class BottomGadgetsItem:

    def __init__(self):
        self.__canvas = pygame.display.get_surface()
        self.__fontSmall = pygame.font.Font("src/Font/Reckoner.ttf", 58)
        self.__imgPillBright = pygame.image.load('src/Icon/PillBright.png')
        self.__imgPillDark = pygame.image.load('src/Icon/PillDark.png')
        self.__imgAlarmClockWarning = pygame.image.load('src/Icon/ClockWarning.png')
        self.__imgAlarmClockBright = pygame.image.load('src/Icon/ClockBright.png')
        self.__imgAlarmClockDark = pygame.image.load('src/Icon/ClockDark.png')

    def OnPaint(self):
        pygame.draw.line(self.__canvas, (64, 64, 64), (0, 175), (DataWindow.WindowsSize[0], 175), 1)
        self.__PaintGadget()

    def __PaintGadget(self):
        # Print pill related icon
        if PillReminderScreen.IsNotTakenToday():
            self.__canvas.blit(self.__imgPillBright, (264, 184))
        else:
            self.__canvas.blit(self.__imgPillDark, (264, 184))

        # Print alarm clock related icon
        if AlarmClockScreen.isCounting:
            if AlarmClockScreen.isAboutToEnd and MainScreen.timeSecond % 2 == 0:
                self.__canvas.blit(self.__imgAlarmClockWarning, (200, 184))
            else:
                self.__canvas.blit(self.__imgAlarmClockBright, (200, 184))
        else:
            self.__canvas.blit(self.__imgAlarmClockDark, (200, 184))

        _temperature = SystemInfoHelper.GetTemperature()
        _temperatureContent = str(_temperature) + "'C"
        self.__canvas.blit(self.__fontSmall.render(_temperatureContent, True, (64, 64, 64)), (9, 186))
        if _temperature <= 60:
            self.__canvas.blit(self.__fontSmall.render(_temperatureContent, True, (192, 192, 192)), (7, 184))
        else:
            self.__canvas.blit(self.__fontSmall.render(_temperatureContent, True, (255, 255, 0)), (7, 184))
