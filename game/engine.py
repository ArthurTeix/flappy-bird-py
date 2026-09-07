import pygame

from game.settings import SCREEN_WIDTH, SCREEN_HEIGHT, GAME_TITLE
from game.elements import Bird, Pipe, Ground
from game.ui.button import Button
from game.rendering import draw_game
from game.database.db import create_table, save_score


class Engine:
    GROUND_Y = 730
    FPS = 30

    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(GAME_TITLE)
        self.watch = pygame.time.Clock()

        self.reset_game()

        create_table()

        self.button_start = Button('./imgs/button/start_btn.png', (250, 250))
        self.button_rank = Button('./imgs/button/rank_btn.png', (250, 400))
        self.button_exit = Button('./imgs/button/exit_btn.png', (250, 550))
        self.button_retry = Button('./imgs/button/retry_btn.png', (250, 250))
        self.button_menu = Button('./imgs/button/menu_btn.png', (250, 400))

        self.state = "menu"

        self.running = True

    def run(self):
        while self.running:
            self.watch.tick(self.FPS)

            self.handle_events()

            if self.state == "menu":
                self.screen.fill((50, 150, 200))
                self.button_start.draw(self.screen)
                self.button_rank.draw(self.screen)
                self.button_exit.draw(self.screen)
                pygame.display.update()

            elif self.state == "play":
                self.update()
                draw_game(self.screen, self.birds, self.pipes, self.ground, self.score)

            elif self.state == "game_over":
                self.screen.fill((50, 150, 200))
                self.button_retry.draw(self.screen)
                self.button_menu.draw(self.screen)
                self.button_exit.draw(self.screen)
                pygame.display.update()

            elif self.state == "rank":
                pass


    # events
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()

            if event.type == pygame.KEYDOWN and self.state == "play":
                if event.key == pygame.K_SPACE:
                    for bird in self.birds:
                        bird.jump()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.state == "menu" and self.button_start.clicked(event.pos):
                    self.reset_game()
                    self.state = "play"
                elif self.state == "menu" and self.button_exit.clicked(event.pos):
                    self.running = False
                elif self.state == "menu" and self.button_rank.clicked(event.pos):
                    self.state = "rank"

                if self.state == "game_over" and self.button_retry.clicked(event.pos):
                    self.reset_game()
                    self.state = "play"
                elif self.state == "game_over" and self.button_menu.clicked(event.pos):
                    self.state = "menu"
                elif self.state == "game_over" and self.button_exit.clicked(event.pos):
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
                    self.state = "game_over"
                    save_score(self.score)

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
                self.state = "game_over"
                save_score(self.score)

    def reset_game(self):
        self.birds = [Bird(230, 350)]
        self.ground = Ground(self.GROUND_Y)
        self.pipes = [Pipe(700)]
        self.score = 0

    # final
    def quit_game(self):
        self.running = False
        pygame.quit()
        quit()
