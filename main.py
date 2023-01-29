import pygame
from pygame.sprite import Group
from Coolest_rpg_game import control
from Coolest_rpg_game.objects.Main_Player import MainPlayer
from Coolest_rpg_game.objects.board import Board
from Coolest_rpg_game.objects.camera import Camera
from Coolest_rpg_game.condition.started import *


FPS = 50


def run():
    pygame.init()
    clock = pygame.time.Clock()
    size = 800, 800
    screen = pygame.display.set_mode(size)  # , pygame.FULLSCREEN)
    with open('levels/level_one.txt') as lvl:
        level = lvl.readlines()
    running = True
    bg_color = (255, 255, 255)
    pygame.display.set_caption('Coolest RPG_game')
    enemies = Group() # Все враги
    npc = Group() # Все НПС
    walls = Group()
    floors = Group
    all_sprites = Group()
    camera = Camera()
    bullets = Group() # Группа всех снарядов маг., физ.
    board = Board(screen, level, walls, floors, all_sprites)
    player = MainPlayer(screen, 'idle', board.out_pole())  # Главный герой
    all_sprites.add(player)
    while running:
        control.controls(screen, player, board) # отслеживание событий
        control.update(screen, bg_color, player, board, walls) # обновление всех кто на экране
        control.animated(screen, player, enemies)
        clock.tick(FPS) #
        camera.update(player)
        # обновляем положение всех спрайтов
        for sprite in all_sprites:
            camera.apply(sprite)



if __name__ == '__main__':
    if start:
        run()
        start = 0
    else:
        control.load()
    input()