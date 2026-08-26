import pygame
import random
import os 

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 800

IMG_PIPE = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'pipe.png')))
IMG_GROUND = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'ground.png')))
IMG_BACKGROUND = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bg.png')))
IMGS_BIRD = [
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird2.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird3.png')))
]

pygame.font.init()
FONTE_PONTOS = pygame.font.SysFont('arial', 50)

class Bird():
    IMGS = IMGS_BIRD

    # rotation animation
    MAX_ROTATION = 25
    SPEED_ROTATION = 20
    ANIMATION_TIME = 5

    def __init__(self, axios_x, axios_y):
        self.axios_x = axios_x
        self.axios_y = axios_y
        self.angle = 0
        self.speed = 0
        self.heigth = self.axios_y
        self.time = 0
        self.cont_img = 0
        self.first_img = self.IMGS[0]

        def jump(self):
            self.speed = -10.5
            self.time = 0
            self.heigth = self.axios_y


class Pipe():
    pass


class Ground():
    pass
