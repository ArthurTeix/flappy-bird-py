from game.settings import IMG_BACKGROUND_GAME, IMG_BACKGROUND_RANK, FONT_SCORE, FONT_RANK, SCREEN_WIDTH
import pygame

def draw_game(screen, birds, pipes, ground, score):
    screen.blit(IMG_BACKGROUND_GAME, (0, 0))

    for bird in birds:
        bird.draw(screen)
    
    for pipe in pipes:
        pipe.draw(screen)

    text = FONT_SCORE.render(f"Score: {score}", 1, (255, 255, 0))
    screen.blit(text, (SCREEN_WIDTH - 10 - text.get_width(), 10))

    ground.draw(screen)

    pygame.display.update()


def draw_rank(screen, top5):
    screen.blit(IMG_BACKGROUND_RANK, (0, 0))

    text = FONT_SCORE.render("RECORDS - TOP 5", 1, (255, 255, 0))
    rect_texto = text.get_rect(center=(SCREEN_WIDTH // 2, 310))
    screen.blit(text, rect_texto)

    axios_y = 320
    gap = 50

    for ranked, score in enumerate(top5, start=1):
        rank = FONT_RANK.render(f"{ranked}º - {score}", 1, (0, 0, 0))
        rect_rank_text = rank.get_rect(center=(SCREEN_WIDTH // 2, (axios_y + (gap * ranked))))
        screen.blit(rank, rect_rank_text)
