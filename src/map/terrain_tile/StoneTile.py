from random import choice
from src.map.TerrainTile import TerrainTile

class StoneTile(TerrainTile):

    SPRITES = ["assets/sprites/terrain/stone1.png", "assets/sprites/terrain/stone2.png", "assets/sprites/terrain/stone3.png"]

    def __init__(self, pos, *groups):
        self.spriteURL = choice(StoneTile.SPRITES)
        super().__init__(pos, self.spriteURL, *groups)