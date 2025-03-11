# C
import pygame

C_YELLOW = (255, 215, 0)
C_WHITE = (255, 255, 255)
C_ORANGE = (255, 128, 0)
C_GREEN = (0, 128, 0)
C_CYAN = (0, 128, 128)

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
ENTITY_DAMAGE = {
    'level-um-bg1': 0,
    'level-um-bg2': 0,
    'level-um-bg3': 0,
    'level-um-bg4': 0,
    'level-um-bg5': 0,
    'level-um-bg6': 0,
    'level-um-bg7': 0,
    'Player1': 1,
    'Player1Shot': 25,
    'Player2': 1,
    'Player2Shot': 10,
    'Enemy1': 1,
    'Enemy1Shot': 20,
    'Enemy2': 1,
    'Enemy2Shot': 15
}
ENTITY_SCORE = {
    'level-um-bg1': 0,
    'level-um-bg2': 0,
    'level-um-bg3': 0,
    'level-um-bg4': 0,
    'level-um-bg5': 0,
    'level-um-bg6': 0,
    'level-um-bg7': 0,
    'Player1': 0,
    'Player1Shot': 0,
    'Player2': 0,
    'Player2Shot': 0,
    'Enemy1': 100,
    'Enemy1Shot': 0,
    'Enemy2': 125,
    'Enemy2Shot': 0
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
