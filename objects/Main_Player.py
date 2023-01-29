import pygame
from pygame.sprite import Sprite
from .constants import *
from game.objects.cutter import cutter


class MainPlayer(Sprite):
    images = {'jump': pygame.image.load('images/Sprites/Jump.png'),
             'run': pygame.image.load('images/Sprites/Run.png'),
             'profile': pygame.image.load('images/Sprites/Run.png'),
             'attack_1': pygame.image.load('images/Sprites/Attack1.png'),
             'attack_2': pygame.image.load('images/Sprites/Attack2.png'),
             'attack_3': pygame.image.load('images/Sprites/Attack3.png'),
             'fall': pygame.image.load('images/Sprites/Fall.png'),
             'take_hit': pygame.image.load('images/Sprites/Take Hit.png'),
             'death': pygame.image.load('images/Sprites/Death.png'),
             'idle': pygame.image.load('images/Sprites/Idle.png')}

    def __init__(self, screen, i, pole):
        super(MainPlayer, self).__init__()
        self.pole = pole
        self.vector = 'stay'
        self.image = self.images[i]
        self.image.set_colorkey((255, 255, 255))
        # self.image = pygame.transform.scale(self.image, (32, 32))
        self.list_of_sprites = dict()
        for key, value in self.images.items():
            self.list_of_sprites[key] = cutter(self.images[key], key)
        self.mask = pygame.mask.from_surface(self.list_of_sprites['idle'][0])
        if type == 'magik':
            self.k = K_MAGIK
            self.k2 = K_MAGIK_2
        else:


            self.k = K_WARRIOR
            self.k2 = K_WARRIOR_2
        self.image = self.list_of_sprites['idle'][0]
        self.health_point = BASIC_HEALTH * self.k2
        self.mana = BASIC_MANA * self.k
        self.defence = BASIC_DEFENCE * self.k2
        self.damage = BASIC_DAMAGE * 1.5
        self.rect = self.image.get_rect()
        self.speed = BASIC_SPEED * self.k
        self.screen_rect = screen.get_rect()
        self.screen = screen
        self.rect.centerx = 300
        self.rect.centery = 60
        self.absy = self.rect.bottom - BLOCK_WIDTH
        self.absx = self.rect.left - 51
        self.move_left = False
        self.move_right = False
        self.jump = False
        self.on_floor = False
        self.t = 0
        self.jump_counter = 15
        self.jump_strenght = BASIC_JUMP
        self.stay = True
        self.inventory = list()
        self.max_size = 10
        self.inv_open = 0
        self.i = 0
        self.dt = 0
        self.flag = 0

    def output(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        x = self.absx // BLOCK_WIDTH
        y = self.absy // BLOCK_HEIGHT
        if self.jump and (self.on_floor or self.flag):
            if self.jump_counter == 15:
                self.on_floor = False
                self.flag = 1

            self.rect.centery += self.jump_strenght
            self.absy += self.jump_strenght
            # if self.absy < 0:
            #     self.jump = False
            #     self.on_floor = False
            #     return
            self.jump_counter -= 1
            if self.jump_counter == 0:
                self.jump_counter = 15
                self.on_floor = False
                self.jump = False
                self.flag = 1
            self.vector = 'up'
            self.t = 0
        if self.on_block():
            self.rect.centery -= self.jump_strenght
            self.absy -= self.jump_strenght
            self.vector = 'down'
            self.t += 1
        else:
            self.on_floor = True
            self.vector = 'stay'
            self.t = 0
        if self.move_right:
            if y < 0 or x + 1 < 0:
                return
            if self.pole[y][x + 1] == 0:
                self.rect.centerx += self.speed
                self.absx += self.speed
                self.vector = 'right'
        if self.move_left:
            if y < 0 or x - 1 < 0:
                return
            if self.pole[y][x - 1] == 0:
                self.rect.centerx -= self.speed
                self.absx -= self.speed
                self.vector = 'left'
        # if self.stay:
        #     self.vector = 'stay'
        self.anime(self.vector)

    def open_inventory(self):
        if self.inv_open:
            pass # Open
        else:
            pass # Close

    def on_block(self):
        y = self.absy
        x = self.absx
        i = x // BLOCK_HEIGHT
        j = y // BLOCK_WIDTH + 1
        if i < 0 or j < 0:
            return False
        # print(self.pole[j][i], j, i, x, y)
        if self.jump:
            return False
        if self.pole[j][i] == 0:
            return True
        else:
            pass
            # print(self.pole[j][i], x, y)
        return False

    def anime(self, vector):
        if self.jump:
            anim = self.list_of_sprites['jump']
            sh = 2
        elif not self.on_floor:
            anim = self.list_of_sprites['fall']
            sh = 2
        else:
            if self.vector in ['left', 'right'] and (self.move_right or self.move_left):
                anim = self.list_of_sprites['run']
                sh = 8
            else:
                anim = self.list_of_sprites['idle']
                sh = 8
        if self.dt == 6:
            if self.stay:
                # potok = [anim[3][-1], *anim[4][:-1]]
                self.image = anim[self.i % sh]
            if not self.stay:
                # potok = anim[0]
                self.image = anim[self.i % sh]
            if self.vector == 'left':
                self.image = pygame.transform.flip(self.image, True, False)
            self.dt = 0
        else:
            self.dt += 1
        self.i += 1

    def attack(self):
        if self.move_left:
            y = self.rect.centery
            x = self.rect.left
        else:
            pass

d = {'stay': 0,
     'down': 0,
     'down-right': 1,
     'right': 2,
     'up-right': 3,
     'up': 4,
     'up-left': 5,
     'left': 6,
     'down-left': 7}

