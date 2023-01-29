import pygame


def cutter(mega_image, key):
    list_of_sprites = list()
    len_of_sprite = {'jump': 2,
                     'fall': 2,
                     'idle': 8,
                     'attack_1': 4,
                     'attack_2': 4,
                     'attack_3': 4,
                     'death': 6,
                     'run': 8,
                     'take_hit': 4,
                     'profile': 8}[key]
    for x in range(8):
        p = list(0)
        for y in range(28):
            image = mega_image.subsurface(y * 32, x * 32, 32, 32)
            # image = pygame.transform.scale(image.subsurface(pygame.Rect((60, 30), (50, 81))), (150, 243))
            p.append(image)
        list_of_sprites.append(p)
    return list_of_sprites
