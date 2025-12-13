from src.map.TerrainTile import TerrainTile

class WaterTile(TerrainTile):

    SPRITES = ["assets/sprites/terrain/shallow-water.png"]

    def __init__(self, pos, *groups):
        self.spriteURL = WaterTile.SPRITES[0]
        super().__init__(pos, self.spriteURL, *groups)