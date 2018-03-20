import pygame


class SoundHelper:
   
    def SetInitial():
        pygame.mixer.init()

    def PlaySound(argName):
        _sound = pygame.mixer.Sound(argName)
        _sound.play()

    def PlayAlarmSound():
        SoundHelper.PlaySound("src\\Sound\\AlarmMusic9.wav")
