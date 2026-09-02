import pygame
from game.settings import IMGS_BIRD


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
        return pygame.mask.from_surface(self.img)
