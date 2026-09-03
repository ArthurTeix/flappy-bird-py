import pygame
from random import randint
from game.settings import IMG_PIPE


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

        distance_top = (self.axios_x - bird.axios_x, self.pos_top - round(bird.axios_y) + 5)
        distance_base = (self.axios_x - bird.axios_x, self.pos_base - round(bird.axios_y) + 5)

        top_colide = bird_mask.overlap(top_mask, distance_top)
        base_colide = bird_mask.overlap(base_mask, distance_base)

        if (top_colide or base_colide):
            return True
        else:
            return False
