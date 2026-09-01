import pygame
from random import randint
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
FONT_SCORE = pygame.font.SysFont('arial', 50)

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
        self.img = self.IMGS[0]

    def jump(self):
        self.speed = -10.5
        self.time = 0
        self.heigth = self.axios_y

    def move(self):
        # calculate displacement
        self.time += 1
        displacement = 1.5 * (self.time ** 2) + self.speed * self.time

        # restrict displacement
        if (displacement > 16):
            displacement = 16
        elif (displacement < 0):
            displacement -= 2

        self.axios_y += displacement

        # angle of the bird
        if (displacement < 0 or self.axios_y < (self.heigth + 50)):
            if (self.angle < self.MAX_ROTATION):
                    self.angle = self.MAX_ROTATION
        else:
            if (self.angle > -90):
                self.angle -= self.SPEED_ROTATION

    def draw(self, screen):
        # def imgs
        self.cont_img += 1

        if (self.cont_img < self.ANIMATION_TIME):
            self.img = self.IMGS[0]
        elif (self.cont_img < self.ANIMATION_TIME*2):
            self.img = self.IMGS[1]
        elif (self.cont_img < self.ANIMATION_TIME*3):
            self.img = self.IMGS[2]
        elif (self.cont_img < self.ANIMATION_TIME*4):
            self.img = self.IMGS[1]
        elif (self.cont_img < self.ANIMATION_TIME*4 + 1):
            self.img = self.IMGS[0]
            self.cont_img = 0

        # bird in freefall
        if (self.angle < -80):
            self.img = self.IMGS[1]
            self.cont_img = self.ANIMATION_TIME * 2
        
        # draw img
        img_rotated = pygame.transform.rotate(self.img, self.angle)
        pos_center_img = self.img.get_rect(topleft=(self.axios_x, self.axios_y)).center
        rectangle = img_rotated.get_rect(center=pos_center_img)

        screen.blit(img_rotated, rectangle.topleft)

    def get_mask(self):
        pygame.mask.from_surface(self.img)

class Pipe():
    DISTANCE = 200
    SPEED = 5

    def __init__(self, axios_x):
        self.axios_x = axios_x
        self.heigth = 0
        self.pos_top = 0
        self.pos_base = 0
        self.img_pipe_ground = IMG_PIPE
        self.img_pipe_top = pygame.transform.flip(IMG_PIPE, False, True)
        self.passed = False
        self.defined_heigth()

    def defined_heigth(self):
        self.heigth = randint(50, 400)
        self.pos_top = self.heigth - self.img_pipe_top.get_height()
        self.pos_base = self.heigth + self.DISTANCE

    def move(self):
        self.axios_x -= self.SPEED

    def draw(self, screen):
        screen.blit(self.img_pipe_top, (self.axios_x, self.pos_top))
        screen.blit(self.img_pipe_ground, (self.axios_x, self.pos_base))

    def colide(self, bird):
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.img_pipe_top)
        base_mask = pygame.mask.from_surface(self.img_pipe_ground)

        distance_top = (self.axios_x - bird.axios_x, self.pos_top - round(bird.axios_y))
        distance_base = (self.axios_x - bird.axios_x, self.pos_base - round(bird.axios_y))

        top_colide = bird_mask.overlap(top_mask, distance_top)
        base_colide = bird_mask.overlap(base_mask, distance_base)

        if (top_colide or base_colide):
            return True
        else:
            return False


class Ground():
    SPEED = 5
    WIDTH = IMG_GROUND.get_width()
    IMG = IMG_GROUND

    def __init__(self, axios_y):
        self.axios_y = axios_y
        self.ground1 = 0
        self.ground2 = self.WIDTH

    def move(self):
        self.ground1 -= self.SPEED
        self.ground2 -= self.SPEED

        if (self.ground1 + self.WIDTH < 0):
            self.ground1 += self.WIDTH
        elif (self.ground2 + self.WIDTH < 0):
            self.ground2 += self.WIDTH

    def draw(self, screen):
        screen.blit(self.IMG, (self.ground1, self.axios_y))
        screen.blit(self.IMG, (self.ground2, self.axios_y))


def draw_screen(screen, bird, pipes, ground, score):
    screen.blit(IMG_BACKGROUND, (0, 0))
    bird.draw(screen)
    for pipe in pipes:
        pipe.draw(screen)

    text = FONT_SCORE.render(f"Score: {score}", 1, (255, 255, 255))
    screen.blit(text, (SCREEN_WIDTH - 10 - text.get_width(), 10))
