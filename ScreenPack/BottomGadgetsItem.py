import pygame

from DataPack.CourtScreen import CourtScreen
from DataPack.Enum_ScreenType import ScreenType
from ScreenPack.AlarmClockScreen import AlarmClockScreen
from DataPack.DataWindow import DataWindow
from ScreenPack.TimeScreen import MainScreen
from ScreenPack.PillReminderScreen import PillReminderScreen
from Utility.SystemInfoHelper import SystemInfoHelper


class BottomGadgetsItem:

    def __init__(self):
        self.__canvas = pygame.display.get_surface()
        self.__fontSmall = pygame.font.Font("src/Font/Reckoner.ttf", 58)

        self.__imgAlarmClock = pygame.image.load('src/Icon/Bottom_Clock.png')
        self.__imgAlarmClockHalo = pygame.image.load('src/Icon/Bottom_ClockHalo.png')
        self.__imgAlarmClockWarning = pygame.image.load('src/Icon/Bottom_ClockWarning.png')
        self.__imgAlarmClockWorking = pygame.image.load('src/Icon/Bottom_ClockWorking.png')

        self.__imgPillNotTaken = pygame.image.load('src/Icon/Bottom_PillNotTaken.png')
        self.__imgPill = pygame.image.load('src/Icon/Bottom_Pill.png')

    def OnPaint(self):
        pygame.draw.line(self.__canvas, (64, 64, 64), (0, 175), (DataWindow.WindowsSize[0], 175), 1)

        # # Print pill related icon
        # if CourtScreen.screenType == ScreenType.PillReminder:
        #     pygame.draw.line(self.__canvas, (64, 64, 64), (264, 184), (264 + 48, 184 + 48), 10)
        # if PillReminderScreen.IsNotTakenToday():
        #     self.__canvas.blit(self.__imgPillBright, (264, 184))
        # else:
        #     self.__canvas.blit(self.__imgPillDark, (264, 184))

        # Print alarm clock related icon
        if CourtScreen.screenType == ScreenType.AlarmClock:
            self.__canvas.blit(self.__imgAlarmClockHalo, (200 - 8, 184 - 8))
        if AlarmClockScreen.isCounting:
            if AlarmClockScreen.isAboutToEnd and MainScreen.timeSecond % 2 == 0:
                self.__canvas.blit(self.__imgAlarmClockWarning, (200, 184))
            else:
                self.__canvas.blit(self.__imgAlarmClockWorking, (200, 184))
        else:
            self.__canvas.blit(self.__imgAlarmClock, (200, 184))

        _temperature = SystemInfoHelper.GetTemperature()
        _temperatureContent = str(_temperature) + "'C"
        self.__canvas.blit(self.__fontSmall.render(_temperatureContent, True, (64, 64, 64)), (9, 186))
        if _temperature <= 60:
            self.__canvas.blit(self.__fontSmall.render(_temperatureContent, True, (192, 192, 192)), (7, 184))
        else:
            self.__canvas.blit(self.__fontSmall.render(_temperatureContent, True, (255, 255, 0)), (7, 184))
