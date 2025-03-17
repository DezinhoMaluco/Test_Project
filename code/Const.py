# C
import random

import pygame

COLOR_BLACK = (0, 0, 0)
COLOR_PURPLE = (240, 0, 255)
COLOR_ORANGE = (255, 128, 0)
COLOR_WHITE = (255, 255, 255)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 4,
    'Level1Bg4': 6,
    'Level1Bg5': 0,
    'Player1': 3,
    'Enemy1': random.randint(1, 2)
}
# M
MENU_OPTION = ('PLAY',
               'SCORE',
               'EXIT')

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324
