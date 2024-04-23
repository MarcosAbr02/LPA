import pygame

# C
COLOR = {"ORANGE": (255, 128, 0), "WHITE": (255, 255, 255), "YELLOW": (255, 255, 128), "GREEN": (0, 128, 0),
         "CYAN": (0, 128, 128)}
# (RED, GREEN, BLUE)

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
EVENT_TIMEOUT = pygame.USEREVENT + 2

ENTITY_SPEED = {
    'Level1Bg0': 0,
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
    'Enemy2Shot': 3,
    'Level2Bg0': 0,
    'Level2Bg1': 1,
    'Level2Bg2': 2,
    'Level2Bg3': 3,
    'Level2Bg4': 4,
}

ENTITY_HEALTH = {
    'Level1Bg0': 1,
    'Level1Bg1': 1,
    'Level1Bg2': 1,
    'Level1Bg3': 1,
    'Level1Bg4': 1,
    'Level1Bg5': 1,
    'Level1Bg6': 1,
    'Player1': 300,
    'Player2': 300,
    'Enemy1': 300,
    'Enemy2': 400,
    'Player1Shot': 1,
    'Player2Shot': 1,
    'Enemy1Shot': 1,
    'Enemy2Shot': 1,
    'Level2Bg0': 1,
    'Level2Bg1': 1,
    'Level2Bg2': 1,
    'Level2Bg3': 1,
    'Level2Bg4': 1,
}

ENTITY_SHOT_DELAY = {
    'Player1': 20,
    'Player2': 30,
    'Enemy1': 40,
    'Enemy2': 50
}

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Player1': 1,
    'Player2': 1,
    'Enemy1': 1,
    'Enemy2': 1,
    'Player1Shot': 100,
    'Player2Shot': 200,
    'Enemy1Shot': 50,
    'Enemy2Shot': 100,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
}

ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Player1': 0,
    'Player2': 0,
    'Enemy1': 100,
    'Enemy2': 50,
    'Player1Shot': 0,
    'Player2Shot': 0,
    'Enemy1Shot': 0,
    'Enemy2Shot': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0
}

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
