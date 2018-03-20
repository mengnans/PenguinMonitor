import pygame


class KeyboardHelper:
    __keyPro = None
    __key = None

    def Initial():
        KeyboardHelper.__keyPro = pygame.key.get_pressed()
        KeyboardHelper.__key = pygame.key.get_pressed()

    def Update():
        KeyboardHelper.__keyPro = KeyboardHelper.__key
        KeyboardHelper.__key = pygame.key.get_pressed()

    def IsPressing(argKey):
        return KeyboardHelper.__key[argKey]

    def IsPress(argKey):
        return KeyboardHelper.__key[argKey] and not KeyboardHelper.__keyPro[argKey]

    def IsReleaseing(argKey):
        return not KeyboardHelper.__key[argKey]

    def IsRelease(argKey):
        return not KeyboardHelper.__key[argKey] and KeyboardHelper.__keyPro[argKey]
