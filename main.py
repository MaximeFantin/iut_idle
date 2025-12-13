import pygame
from src.Sprite import *
from src.map.Map import *

pygame.init()
screen = pygame.display.set_mode((1088, 720))
clock = pygame.time.Clock()
running = True

from src.map.MapGenerator import MapGenerator
map: Map = MapGenerator.perlinGeneration()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(pygame.Color(65, 60, 70))


    map.terrainGroup.draw(screen)


    pygame.display.flip()
    clock.tick(30)

pygame.quit()