import pygame


class SoundHelper:

    @staticmethod
    def SetInitial():
        pygame.mixer.init()

    @staticmethod
    def PlaySound(argName):
        _sound = pygame.mixer.Sound(argName)
        _sound.play()

    @staticmethod
    def PlayAlarmSound():
        SoundHelper.PlaySound("src/Sound/AlarmMusic9.wav")
