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
    def PlaySpeech(argSpeechName):
        SoundHelper.PlaySound("src/Music/Speech_" + argSpeechName + ".wav")
