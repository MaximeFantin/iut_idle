from random import choice
from src.map.TerrainTile import TerrainTile

class SandTile(TerrainTile):

    SPRITES = ["assets/sprites/terrain/sand-floor1.png", "assets/sprites/terrain/sand-floor2.png", "assets/sprites/terrain/sand-floor3.png"]

    def __init__(self, pos, *groups):
        self.spriteURL = choice(SandTile.SPRITES)
        super().__init__(pos, self.spriteURL, *groups)