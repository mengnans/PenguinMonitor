import pygame


class KeyboardHelper:
    __keyPressed = None

    def Initial():
        KeyboardHelper.Update()

    def Update():
        KeyboardHelper.__keyPressed = pygame.key.get_pressed()

    def IsPress(argKey):
        return __keyPressed[argKey]
