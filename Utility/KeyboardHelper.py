import pygame


class KeyboardHelper:
    __keyPro = None
    __key = None

    @staticmethod
    def Initial():
        KeyboardHelper.__keyPro = pygame.key.get_pressed()
        KeyboardHelper.__key = pygame.key.get_pressed()

    @staticmethod
    def Update():
        KeyboardHelper.__keyPro = KeyboardHelper.__key
        KeyboardHelper.__key = pygame.key.get_pressed()

    @staticmethod
    def IsPressing(argKey):
        return KeyboardHelper.__key[argKey]

    @staticmethod
    def IsPress(argKey):
        return KeyboardHelper.__key[argKey] and not KeyboardHelper.__keyPro[argKey]

    @staticmethod
    def IsReleaseing(argKey):
        return not KeyboardHelper.__key[argKey]

    @staticmethod
    def IsRelease(argKey):
        return not KeyboardHelper.__key[argKey] and KeyboardHelper.__keyPro[argKey]
