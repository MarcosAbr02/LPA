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
ENTITY_SPEED = {'Level1Bg0': 0,
                'Level1Bg1': 1,
                'Level1Bg2': 2,
                'Level1Bg3': 3,
                'Level1Bg4': 4,
                'Level1Bg5': 5,
                'Level1Bg6': 6,
                'Player1': 3,
                'Player2': 3,
                'Entity': 4
                }

# P
PLAYER_KEYS = {
    "Player1":
        {"UP": pygame.K_UP, "DOWN": pygame.K_DOWN, "LEFT": pygame.K_LEFT, "RIGHT": pygame.K_RIGHT},
    "Player2":
        {"UP": pygame.K_w, "DOWN": pygame.K_s, "LEFT": pygame.K_a, "RIGHT": pygame.K_d}
    }
