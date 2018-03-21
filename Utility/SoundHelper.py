import pygame


class SoundHelper:

    @staticmethod
    def SetInitial():
        pygame.mixer.init()

    @staticmethod
    def PlaySound(argMusicFileAddress):
        _sound = pygame.mixer.Sound(argMusicFileAddress)
        _sound.play()

    @staticmethod
    def PlayAlarmSound():
        SoundHelper.PlaySound("src/Sound/AlarmMusic9.wav")
