from Sprite import Sprite
import pygame

class Terrain(Sprite):

    TERRAIN_SPRITES = pygame.sprite.Group()

    def __init__(self, pos, tileSprite, *groups):
        super().__init__((pos[0] * 16, pos[1] * 16), 16, 16, Terrain.TERRAIN_SPRITES, *groups)
        self.image.blit(pygame.image.load(tileSprite), pos)