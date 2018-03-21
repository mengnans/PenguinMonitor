import pygame
import time

from ScreenPack.IScreen import IScreen
from Utility.KeyboardHelper import KeyboardHelper


class AlarmClockScreen(IScreen):
    isCounting = False
    isAboutToEnd = False
    timeHour = 0
    timeMinute = 0
    timeSecond = 0
    alarmTimeString = '0000'

    def __init__(self):
        self.__canvas = pygame.display.get_surface()
        self.__font = pygame.font.Font("src/Font/Reckoner.ttf", 200)

    def OnUpdate(self):
        for _num in range(0, 10):
            if KeyboardHelper.IsPress(pygame.K_KP0 + _num) | KeyboardHelper.IsPress(pygame.K_0 + _num):
                AlarmClockScreen.alarmTimeString += str(_num)
                AlarmClockScreen.alarmTimeString = AlarmClockScreen.alarmTimeString[1:]
                IScreen.ForceUpdate()
        # if KeyboardHelper.IsPress(pygame.K_KP1) | KeyboardHelper.IsPress(pygame.K_1):
        #     AlarmClockScreen.alarmTimeString += '1'
        # if KeyboardHelper.IsPress(pygame.K_KP1) | KeyboardHelper.IsPress(pygame.K_2):
        #     AlarmClockScreen.alarmTimeString += '2'
        # if KeyboardHelper.IsPress(pygame.K_KP1) | KeyboardHelper.IsPress(pygame.K_3):
        #     AlarmClockScreen.alarmTimeString += '3'
        # if KeyboardHelper.IsPress(pygame.K_KP1) | KeyboardHelper.IsPress(pygame.K_4):
        #     AlarmClockScreen.alarmTimeString += '4'
        # if KeyboardHelper.IsPress(pygame.K_KP1) | KeyboardHelper.IsPress(pygame.K_5):
        #     AlarmClockScreen.alarmTimeString += '5'
        # if KeyboardHelper.IsPress(pygame.K_KP1) | KeyboardHelper.IsPress(pygame.K_6):
        #     AlarmClockScreen.alarmTimeString += '6'
        # if KeyboardHelper.IsPress(pygame.K_KP1) | KeyboardHelper.IsPress(pygame.K_7):
        #     AlarmClockScreen.alarmTimeString += '7'
        # if KeyboardHelper.IsPress(pygame.K_KP1) | KeyboardHelper.IsPress(pygame.K_8):
        #     AlarmClockScreen.alarmTimeString += '8'
        # if KeyboardHelper.IsPress(pygame.K_KP1) | KeyboardHelper.IsPress(pygame.K_9):
        #     AlarmClockScreen.alarmTimeString += '9'
        #     AlarmClockScreen.alarmTimeString = AlarmClockScreen.alarmTimeString[1:]
        #     IScreen.ForceUpdate()
        # if KeyboardHelper.IsPress(pygame.K_KP1) | KeyboardHelper.IsPress(pygame.K_0):
        #     AlarmClockScreen.alarmTimeString += '0'


        pass

    def OnPaint(self):
        self.__PaintTime()

    def __PaintTime(self):
        _timeContentHour = AlarmClockScreen.alarmTimeString[:2]
        _timeContentMinute = AlarmClockScreen.alarmTimeString[2:]

        # Draw hour value
        _renderText = self.__font.render(_timeContentHour, True, (255, 255, 255))
        _recText = _renderText.get_rect()
        _locationX = (152 - (_recText[2] - 10)) / 2
        self.__canvas.blit(self.__font.render(_timeContentHour, True, (128, 128, 128)), (_locationX + 2, 7))
        self.__canvas.blit(self.__font.render(_timeContentHour, True, (255, 255, 255)), (_locationX, 5))

        # Draw colon
        if AlarmClockScreen.timeSecond % 2 == 0:
            self.__canvas.blit(self.__font.render(":", True, (128, 128, 128)), (154, -18))
            self.__canvas.blit(self.__font.render(":", True, (255, 255, 255)), (152, -20))
        else:
            self.__canvas.blit(self.__font.render(":", True, (64, 64, 64)), (154, -18))
            self.__canvas.blit(self.__font.render(":", True, (128, 128, 128)), (152, -20))

        # Draw minute value
        _renderText = self.__font.render(_timeContentMinute, True, (255, 255, 255))
        _recText = _renderText.get_rect()
        _locationX = 168 + (152 - (_recText[2] - 10)) / 2
        self.__canvas.blit(self.__font.render(_timeContentMinute, True, (128, 128, 128)), (_locationX + 2, 7))
        self.__canvas.blit(self.__font.render(_timeContentMinute, True, (255, 255, 255)), (_locationX, 5))
