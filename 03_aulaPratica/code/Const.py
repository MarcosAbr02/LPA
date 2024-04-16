# C
import pygame

COLOR = {"ORANGE": (255, 128, 0), "WHITE": (255, 255, 255), "YELLOW": (255, 255, 128)}

# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'EXIT')

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324

# E
EVENT_ENEMY = pygame.USEREVENT + 1

ENTITY_SPEED = {'Level1Bg0': 0,
                'Level1Bg1': 1,
                'Level1Bg2': 2,
                'Level1Bg3': 3,
                'Level1Bg4': 4,
                'Level1Bg5': 5,
                'Level1Bg6': 6,
                'Player1': 3,
                'Player1Shot': 6,
                'Player2': 3,
                'Player2Shot': 5,
                'Enemy1': 2,
                'Enemy1Shot': 4,
                'Enemy2': 1,
                'Enemy2Shot': 3
                }

ENTITY_HEALTH = {'Level1Bg0': 1,
                 'Level1Bg1': 1,
                 'Level1Bg2': 1,
                 'Level1Bg3': 1,
                 'Level1Bg4': 1,
                 'Level1Bg5': 1,
                 'Level1Bg6': 1,
                 'Player1': 300,
                 'Player2': 300,
                 'Enemy1': 200,
                 'Enemy2': 200,
                 'Player1Shot': 1,
                 'Player2Shot': 1,
                 'Enemy1Shot': 1,
                 'Enemy2Shot': 1,
                 }

ENTITY_SHOT_DELAY = {'Player1': 30,
                     'Player2': 30,
                     'Enemy1': 70,
                     'Enemy2': 70}

# P
PLAYER_KEYS = {
    "Player1":
        {"UP": pygame.K_UP, "DOWN": pygame.K_DOWN, "LEFT": pygame.K_LEFT, "RIGHT": pygame.K_RIGHT,
         "SHOOT": pygame.K_l},
    "Player2":
        {"UP": pygame.K_w, "DOWN": pygame.K_s, "LEFT": pygame.K_a, "RIGHT": pygame.K_d, "SHOOT": pygame.K_LSHIFT}

}
# G
GAME_SPEED = {"NORMAL": 60, "TURBO": 120}
