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


def draw_screen(screen, birds, pipes, ground, score):
    screen.blit(IMG_BACKGROUND, (0, 0))

    for bird in birds:
        bird.draw(screen)
    
    for pipe in pipes:
        pipe.draw(screen)

    text = FONT_SCORE.render(f"Score: {score}", 1, (255, 255, 0))
    screen.blit(text, (SCREEN_WIDTH - 10 - text.get_width(), 10))

    ground.draw(screen)

    pygame.display.update()


def main():
    birds = [Bird(230, 350)]
    ground = Ground(730)
    pipes = [Pipe(700)]
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    score = 0
    watch = pygame.time.Clock()

    end_game = False
    while not end_game:
        watch.tick(30) # fps

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                end_game = True
                pygame.quit()
                quit()

            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_SPACE):
                    for bird in birds:
                        bird.jump()

        # move elements
        for bird in birds:
            bird.move()
        ground.move()

        add_pipe = False
        removed_pipe = []
        for pipe in pipes:
            for i, bird in enumerate(birds):
                if (pipe.colide(bird)):
                    birds.pop(i)
                    pygame.quit()
                    quit()

                if (not pipe.passed and bird.axios_x > pipe.axios_x):
                    pipe.passed = True
                    add_pipe = True

            pipe.move()
            if (pipe.axios_x + pipe.img_pipe_top.get_width() < 0):
                removed_pipe.append(pipe)

        if add_pipe:
            score += 1
            pipes.append(Pipe(600))

        for pipe in removed_pipe:
            pipes.remove(pipe)

        for i, bird in enumerate(birds):
            if (bird.axios_y + bird.img.get_height() > 730) or (bird.axios_y < 0):
                birds.pop(i)
                pygame.quit()
                quit()
                

        draw_screen(screen, birds, pipes, ground, score)


if __name__ == '__main__':
    main()
