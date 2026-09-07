import pygame
import os

# config screen
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 800

# title
GAME_TITLE = "Flappy Bird"

# path img
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMGS_DIR = os.path.join(BASE_DIR, 'imgs')

pygame.font.init()

# used imgs 
IMG_PIPE = pygame.transform.scale2x(pygame.image.load(os.path.join(IMGS_DIR, 'pipe.png')))
IMG_GROUND = pygame.transform.scale2x(pygame.image.load(os.path.join(IMGS_DIR, 'ground.png')))
IMG_BACKGROUND_GAME = pygame.transform.scale2x(pygame.image.load(os.path.join(IMGS_DIR, 'bg_game.png')))
IMG_BACKGROUND_RANK = pygame.image.load(os.path.join(IMGS_DIR, 'bg_rank.png'))
IMGS_BIRD = [
    pygame.transform.scale2x(pygame.image.load(os.path.join(IMGS_DIR, 'bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join(IMGS_DIR, 'bird2.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join(IMGS_DIR, 'bird3.png'))),
]

# score
FONT_SCORE = pygame.font.SysFont('arial', 50)
FONT_RANK = pygame.font.SysFont('dfkaisb', 50)
