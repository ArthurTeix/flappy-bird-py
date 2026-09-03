from game.settings import IMG_GROUND



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
            self.ground1 = self.ground2 + self.WIDTH
        elif (self.ground2 + self.WIDTH < 0):
            self.ground2 = self.ground1 + self.WIDTH

    def draw(self, screen):
        screen.blit(self.IMG, (self.ground1, self.axios_y))
        screen.blit(self.IMG, (self.ground2, self.axios_y))

