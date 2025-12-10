from random import seed, choice
from abc import ABC, abstractmethod
from socket import gethostname
from src.map.Map import Map
from src.map.terrain_tile.StoneTile import StoneTile
import noise_display

class MapGenerator(ABC):

    @staticmethod
    def getSeed():
        return gethostname

    @staticmethod
    def generate():
        seed(gethostname())
        map = Map()
        for x in range(Map.SIZE[0]):
            for y in range(Map.SIZE[1]):
                map.grid[(x, y)]["terrain"] = StoneTile((x, y), map.terrainGroup)
        return map

    @staticmethod
    def generateNoiseMap():
        scale = 100
        octaves = 6
        persistence = 0.5
        lacunarity = 2.0
        noiseMap = []
        outstr = ""
        for i in range(Map.SIZE[1]):
            noiseMap.append([])
            for j in range(Map.SIZE[0]):
                noiseMap[-1].append(
                    noise_display.pnoise2(j/scale, i/scale, octaves=octaves, persistence=persistence, lacunarity=lacunarity, repeatx=Map.SIZE[0], repeaty=Map.SIZE[1], base=0)
                )
                outstr += str(noiseMap[-1][-1]) + " "
            outstr += "\n"
        with open("noise", "w") as f:
            f.write(outstr)


MapGenerator.generateNoiseMap()