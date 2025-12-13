from random import seed, choice
from abc import ABC
from socket import gethostname
from src.map.Map import Map
from src.map.terrain_tile.StoneTile import StoneTile
from src.map.terrain_tile.SandTile import SandTile
from src.map.terrain_tile.WaterTile import WaterTile
from src.map.terrain_tile.GrassTile import GrassTile
import noise

class MapGenerator(ABC):

    @staticmethod
    def getSeed():
        host = gethostname()
        s = 1
        for c in host:
            s *= ord(c)
        return s
    
    @staticmethod
    def perlinGeneration():
        mapSeed = MapGenerator.getSeed()
        seed(mapSeed)
        scale = 50
        octaves = 6
        persistence = 0.25
        lacunarity = 1.5
        map = Map()

        invalid = True
        while invalid:
            try:
                for x in range(Map.SIZE[0]):
                    for y in range(Map.SIZE[1]):
                        #pnoise = noise.pnoise2(x/scale, y/scale, octaves=octaves, persistence=persistence, lacunarity=lacunarity, repeatx=Map.SIZE[0], repeaty=Map.SIZE[1], base=0)
                        pnoise = noise.pnoise2(x/scale, y/scale, octaves=octaves, persistence=persistence, lacunarity=lacunarity, repeatx=Map.SIZE[0], repeaty=Map.SIZE[1], base=mapSeed%10_402_211)
                        noiseValue = abs(pnoise)
                        if noiseValue < 0.06:
                            map.grid[(x, y)]["terrain"] = WaterTile((x, y), map.terrainGroup)
                        elif noiseValue < 0.08:
                            map.grid[(x, y)]["terrain"] = SandTile((x, y), map.terrainGroup)
                        elif noiseValue < 0.11:
                            map.grid[(x, y)]["terrain"] = GrassTile((x, y), map.terrainGroup)
                        else:
                            map.grid[(x, y)]["terrain"] = StoneTile((x, y), map.terrainGroup)
                invalid = False
        return map


    @staticmethod
    def generateBlank():
        map = Map()
        for x in range(Map.SIZE[0]):
            for y in range(Map.SIZE[1]):
                map.grid[(x, y)]["terrain"] = StoneTile((x, y), map.terrainGroup)
        return map

    @staticmethod
    def generateNoiseMap():
        scale = 50
        octaves = 6
        persistence = 0.25
        lacunarity = 1.5
        noiseMap: list[list[float]] = []
        outstr = ""
        for i in range(Map.SIZE[1]):
            noiseMap.append([])
            for j in range(Map.SIZE[0]):
                noiseMap[-1].append(
                    noise.pnoise2(j/scale, i/scale, octaves=octaves, persistence=persistence, lacunarity=lacunarity, repeatx=Map.SIZE[0], repeaty=Map.SIZE[1], base=0)
                )
                outstr += str(noiseMap[-1][-1]) + " "
            outstr += "\n"
        with open("noise", "w") as f:
            f.write(outstr)


#MapGenerator.generateNoiseMap()