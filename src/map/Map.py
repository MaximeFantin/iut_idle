import pygame

class Map:
    SIZE = 68, 45

    def __init__(self):
        self.terrainGroup = pygame.sprite.Group()
        self.grid = {}
        for x in range(Map.SIZE[0]):
            for y in range(Map.SIZE[1]):
                self.grid[(x, y)] = {"terrain": None, "building": None, "buildingSource": None}
