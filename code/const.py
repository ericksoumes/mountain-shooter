# C
import pygame

COLOR_YELLOW = (255, 215, 0)
COLOR_WHITE = (255, 255, 255)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {
    'level-um-bg1': 0,
    'level-um-bg2': 1,
    'level-um-bg3': 2,
    'level-um-bg4': 3,
    'level-um-bg5': 4,
    'level-um-bg6': 5,
    'level-um-bg7': 6,
    'Player1': 3,
    'Player1Shot': 1,
    'Player2': 3,
    'Player2Shot': 3,
    'Enemy1': 1,
    'Enemy1Shot': 3,
    'Enemy2': 1,
    'Enemy2Shot': 3
}

ENTITY_HEALTH = {
    'level-um-bg1': 999,
    'level-um-bg2': 999,
    'level-um-bg3': 999,
    'level-um-bg4': 999,
    'level-um-bg5': 999,
    'level-um-bg6': 999,
    'level-um-bg7': 999,
    'Player1': 300,
    'Player1Shot': 1,
    'Player2': 300,
    'Player2Shot': 1,
    'Enemy1': 50,
    'Enemy1Shot': 1,
    'Enemy2': 60,
    'Enemy2Shot': 60
}

ENTITY_SHOT_DELAY = {
    'Player1': 20,
    'Player2': 15,
    'Enemy1': 100,
    'Enemy2': 200
}

# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE', 'EXIT')

# P
PLAYER_KEY_UP = {
    'Player1': pygame.K_UP,
    'Player2': pygame.K_w
}
PLAYER_KEY_DOWN = {
    'Player1': pygame.K_DOWN,
    'Player2': pygame.K_s
}
PLAYER_KEY_LEFT = {
    'Player1': pygame.K_LEFT,
    'Player2': pygame.K_a
}
PLAYER_KEY_RIGHT = {
    'Player1': pygame.K_RIGHT,
    'Player2': pygame.K_d
}
PLAYER_KEY_SHOOT = {
    'Player1': pygame.K_RCTRL,
    'Player2': pygame.K_LCTRL
}

# S
SPAWN_TIME = 4000

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324
