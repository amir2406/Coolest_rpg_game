import pygame
from pygame.sprite import Sprite, Group
from .constants import *


class Board:
    def __init__(self, screen, level, walls, floors, all_spr):
        self.screen = screen
        self.level = list()
        self.pole = list()
        for i, line in enumerate(level):
            pl = line.split(';')
            l = list()
            p = list()
            for j, x in enumerate(pl):
                n, oz, _ = eval(x)
                l.append(oz)
                if oz == 1:
                    object = Wall(screen, n, i, j)
                    walls.add(object)
                else:
                    object = Floor(screen, n, i, j)
                    floors.add(object)
                all_spr.add(object)
                p.append(object)
            self.pole.append(l)
            self.level.append(p)

    def out_pole(self):
        return self.pole

    def output(self):
        for i, line in enumerate(self.level):
            for j, object in enumerate(line):
                object.output()

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def get_cell(self, pos):
        x, y = pos
        i = y // BLOCK_HEIGHT
        j = x // BLOCK_WIDTH
        return i, j

    def on_click(self, cell):
        pass


class Wall(Sprite):
    images = {1: pygame.image.load('images/maybe/derevo.png')}

    def __init__(self, screen, type, i, j):
        super(Wall, self).__init__()
        self.image = self.images[type]
        self.image.set_colorkey((255, 255, 255))
        self.image = pygame.transform.scale(self.image, (BLOCK_WIDTH, BLOCK_HEIGHT))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.screen = screen
        self.rect.x = j * BLOCK_HEIGHT
        self.rect.y = i * BLOCK_WIDTH

    def output(self):
        self.screen.blit(self.image, self.rect)


class Floor(Sprite):
    images = {0: pygame.image.load('images/Environment/Grass1.png')}

    def __init__(self, screen, type, i, j):
        super(Floor, self).__init__()
        self.image = self.images[type]
        self.image.set_colorkey((255, 255, 255))
        self.image = pygame.transform.scale(self.image, (BLOCK_WIDTH, BLOCK_HEIGHT))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.screen = screen
        self.rect.x = j * BLOCK_HEIGHT
        self.rect.y = i * BLOCK_WIDTH

    def output(self):
        self.screen.blit(self.image, self.rect)
