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
    'Player2': 3,
    'Enemy1': random.randint(1, 2)
}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Player1': 300,
    'Player2': 300,
    'Enemy1': 30
}

# M
MENU_OPTION = ('PLAY',
               'SCORE',
               'EXIT')

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324
