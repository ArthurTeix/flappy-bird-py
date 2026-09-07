import pygame
from classBtn import Botao

pygame.init()
tela = pygame.display.set_mode((500, 800))

botao_start = Botao('./imgs/button/start_btn.png', (250, 250))
botao_exit = Botao('./imgs/button/exit_btn.png', (250, 550))

estado = "menu"  # pode ser "menu" ou "jogo"

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            if estado == "menu" and botao_start.foi_clicado(evento.pos):
                estado = "jogo"  # troca de tela

            elif estado == "menu" and botao_exit.foi_clicado(evento.pos):
                rodando = False

    # agora o desenho depende do estado
    if estado == "menu":
        tela.fill((50, 150, 200))
        botao_start.desenhar(tela)
        botao_exit.desenhar(tela)
    else:
        tela.fill((0, 0, 0))  # só pra ver que mudou - depois vira o jogo de verdade

    pygame.display.update()

pygame.quit()
