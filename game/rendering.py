from game.settings import IMG_BACKGROUND, FONT_SCORE, SCREEN_WIDTH
import pygame

def draw_game(screen, birds, pipes, ground, score):
    screen.blit(IMG_BACKGROUND, (0, 0))

    for bird in birds:
        bird.draw(screen)
    
    for pipe in pipes:
        pipe.draw(screen)

    text = FONT_SCORE.render(f"Score: {score}", 1, (255, 255, 0))
    screen.blit(text, (SCREEN_WIDTH - 10 - text.get_width(), 10))

    ground.draw(screen)

    pygame.display.update()


def draw_rank(screen, text, top5):
    pass