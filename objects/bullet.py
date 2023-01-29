import pygame


class Bullet(pygame.sprite.Sprite):
    image = pygame.transform.scale(pygame.image.load('images/bullet.png'), (16, 16))

    def __init__(self, screen, player):
        super(Bullet, self).__init__()
        self.vector = player.vector
        self.rect = self.image.get_rect()
        self.speed = 5
        self.screen_rect = screen.get_rect()
        self.screen = screen
        self.speed_y = 0
        self.rect.centery = player.rect.centery
        if self.vector == 'left':
            self.rect.right = player.rect.left
            self.speed_x = -self.speed
        else:
            self.rect.left = player.rect.right
            self.speed_x = self.speed

    def output(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.rect.centerx += self.speed_x
        self.rect.centery += self.speed_y