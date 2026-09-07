import pygame

class Botao:
    def __init__(self, caminho_imagem, centro):
        self.imagem = pygame.image.load(caminho_imagem).convert_alpha()
        self.rect = self.imagem.get_rect(center=centro)

    def desenhar(self, tela):
        tela.blit(self.imagem, self.rect)

    def foi_clicado(self, pos_clique):
        return self.rect.collidepoint(pos_clique)