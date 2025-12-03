from random import choice
from ..Terrain import Terrain

class StoneTile(Terrain):

    SPRITES = ["assets/sprites/terrain/stone1.png", "assets/sprites/terrain/stone2.png", "assets/sprites/terrain/stone3.png"]

    def __init__(self, pos, *groups):
        super().__init__(pos, choice(StoneTile.SPRITES), *groups)