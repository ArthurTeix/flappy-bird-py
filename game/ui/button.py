import pygame

class Button:
    def __init__(self, img, cent):
        self.img = pygame.image.load(img).convert_alpha()
        self.rect = self.img.get_rect(center=cent)

    def draw(self, tela):
        tela.blit(self.img, self.rect)

    def clicked(self, pos_clique):
        return self.rect.collidepoint(pos_clique)
