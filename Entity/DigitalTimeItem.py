import pygame


class FontColorType(Enum):
    White = 1
    Grey = 2
    Yellow = 3
    Red = 4


class FpsDisplayItem:
    __imgWhite = None
    __imgGrey = None
    __imgYellow = None
    __imgRed = None
    __canvas = None

    @staticmethod
    def Init():
        # __imgWhite = pygame.image.load('src/Icon/TimeWhite.png')
        # __imgGrey = pygame.image.load('src/Icon/TimeWhite.png')
        # __imgYellow = pygame.image.load('src/Icon/TimeWhite.png')
        # __imgRed = pygame.image.load('src/Icon/TimeWhite.png')
        __canvas = pygame.display.get_surface()
        pass

    def __init__(self):
        self.hour = "00"
        self.minute = "00"
        self.hourColor = FontColorType.White
        self.minuteColor = FontColorType.White
        self.colonColor = FontColorType.White

    def SetPaint(self):
        pass
