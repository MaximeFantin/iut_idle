from random import choice
from src.map.TerrainTile import TerrainTile

class GrassTile(TerrainTile):

    SPRITES = ["assets/sprites/terrain/grass1.png", "assets/sprites/terrain/grass2.png", "assets/sprites/terrain/grass3.png"]

    def __init__(self, pos, *groups):
        self.spriteURL = choice(GrassTile.SPRITES)
        super().__init__(pos, self.spriteURL, *groups)