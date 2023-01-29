import pygame


class Block:
    image = pygame.image.load('images/magic.png')

    def __init__(self, screen, i):
        super(Block, self).__init__()
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.screen = screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def output(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        pass