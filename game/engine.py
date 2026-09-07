import pygame

from game.settings import SCREEN_WIDTH, SCREEN_HEIGHT, GAME_TITLE
from game.elements import Bird, Pipe, Ground
from game.ui.button import Button
from game.rendering import draw_screen


class Engine:
    GROUND_Y = 730
    FPS = 30

    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(GAME_TITLE)
        self.watch = pygame.time.Clock()

        self.birds = [Bird(230, 350)]
        self.ground = Ground(self.GROUND_Y)
        self.pipes = [Pipe(700)]
        self.score = 0

        self.botao_start = Button('./imgs/button/start_btn.png', (250, 250))
        self.botao_exit = Button('./imgs/button/exit_btn.png', (250, 550))
        self.state = "menu"

        self.running = True

    def run(self):
        while self.running:
            self.watch.tick(self.FPS)

            self.handle_events()
            
            if self.state == "menu":
                self.screen.fill((50, 150, 200))
                self.botao_start.draw(self.screen)
                self.botao_exit.draw(self.screen)
                pygame.display.update()
            else:
                self.update()
                
                draw_screen(self.screen, self.birds, self.pipes, self.ground, self.score)

    # events
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    for bird in self.birds:
                        bird.jump()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.state == "menu" and self.botao_start.clicked(event.pos):
                    self.state = "jogo"
            
                elif self.state == "menu" and self.botao_exit.clicked(event.pos):
                    self.running = False

    # per-frame update
    def update(self):
        self.move_elements()
        self.update_pipes()
        self.check_out_of_bounds()

    def move_elements(self):
        for bird in self.birds:
            bird.move()
        self.ground.move()

    def update_pipes(self):
        add_pipe = False
        removed_pipe = []

        for pipe in self.pipes:
            for i, bird in enumerate(self.birds):
                if pipe.colide(bird):
                    self.birds.pop(i)
                    self.quit_game()

                if not pipe.passed and bird.axios_x > pipe.axios_x:
                    pipe.passed = True
                    add_pipe = True

            pipe.move()
            if pipe.axios_x + pipe.img_pipe_top.get_width() < 0:
                removed_pipe.append(pipe)

        if add_pipe:
            self.score += 1
            self.pipes.append(Pipe(600))

        for pipe in removed_pipe:
            self.pipes.remove(pipe)

    def check_out_of_bounds(self):
        for i, bird in enumerate(self.birds):
            if (bird.axios_y + bird.img.get_height() > self.GROUND_Y) or (bird.axios_y < 0):
                self.birds.pop(i)
                self.quit_game()

    # final
    def quit_game(self):
        self.running = False
        pygame.quit()
        quit()
