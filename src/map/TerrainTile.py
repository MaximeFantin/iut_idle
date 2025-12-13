from src.Sprite import Sprite
import pygame

class TerrainTile(Sprite):

    TERRAIN_SPRITES = pygame.sprite.Group()

    def __init__(self, pos, tileSprite, *groups):
        super().__init__((pos[0] * 16, pos[1] * 16), 16, 16, TerrainTile.TERRAIN_SPRITES, *groups)
        img = pygame.image.load(tileSprite).convert_alpha()
        if img.get_size() != (16, 16):
            img = pygame.transform.scale(img, (16, 16))
        self.image.blit(img, (0, 0))