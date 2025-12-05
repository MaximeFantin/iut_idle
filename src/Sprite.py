import pygame

class Sprite(pygame.sprite.Sprite):

    ALIVE_SPRITES = pygame.sprite.Group()

    def __init__(self, pos, width, height, *groups):
        super().__init__(Sprite.ALIVE_SPRITES, *groups)
        self.image = pygame.Surface((width, height))
        self.rect = pygame.Rect(pos[0], pos[1], width, height)