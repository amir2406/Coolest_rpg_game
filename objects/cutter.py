import pygame



def cutter(filename, key):
    mega_image = filename
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
    for x in range(len_of_sprite):
        image = mega_image.subsurface(x * 160, 0, 160, 111)
        image = pygame.transform.scale(image.subsurface(pygame.Rect((64, 30), (50, 81))), (150, 243))
        list_of_sprites.append(image)
    return list_of_sprites
