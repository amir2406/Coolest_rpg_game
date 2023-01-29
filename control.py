import pygame, sys
from .objects.bullet import Bullet
from pygame.sprite import spritecollide, groupcollide

pygame.init()


def controls(screen, all_sprites, player, board, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)
            bullet = Bullet(screen, player)
            bullets.add(bullet)
            all_sprites.add(bullet)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.move_left = True
                player.stay = False
            elif event.key == pygame.K_d:
                player.move_right = True
                player.stay = False
            # elif event.key == pygame.K_w:
            #     player.move_up = True
            #     player.stay = False
            elif event.key == pygame.K_s:
                player.move_down = True
                player.stay = False
                # player.jump_counter =
            elif event.key == pygame.K_i:
                if player.inv_open:
                    player.inv_open = 0
                else:
                    player.inv_open = 1
                player.open_inventory()
            elif event.key == pygame.K_SPACE:
                player.jump = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player.move_left = False
                player.stay = True
            elif event.key == pygame.K_d:
                player.move_right = False
                player.stay = True
            elif event.key == pygame.K_w:
                player.move_up = False
                player.stay = True
            elif event.key == pygame.K_s:
                player.move_down = False
                player.stay = True


def update(screen, bg_color, player, board, walls, bullets):
    screen.fill(bg_color)
    board.output()
    # if spritecollideany(player, walls):
    #     if player.vector == 'up':
    #         player.rect.top += player.speed
    #     elif player.vector == 'down':
    #         player.rect.bottom -= player.speed
    #     elif player.vector == 'right':
    #         player.rect.right -= player.speed
    #     elif player.vector == 'left':
    #         player.rect.left += player.speed
    #     # player.speed = 0
    # else:
    #     player.speed = BASIC_SPEED
    for bullet in groupcollide(bullets, walls, True, False):
        bullet.remove()
        bullet.kill()
    for object in bullets:
        object.update()
        object.output()
    player.update()
    player.output()
    pygame.display.flip()


def animated(screen, player, enemies):
    pass


def save():
    pass


# anti = {'up': 'down',
#         'right': 'left',
#         'left': 'right',
#         'down': 'up'}