import pygame
from Settings import *
import Tile

class MapManagement:
    def __init__(self, levelMap):
        self.levelMap = levelMap

        self.tileList = []

        wallImage = pygame.image.load("Tiles/wallV2.png")
        wallImage = pygame.transform.scale(wallImage, (tileSize, tileSize))
        self.wallTile = Tile.Tile("wall", wallImage, True, tileSize)
        self.tileList.append(self.wallTile)

        floorImage = pygame.image.load("Tiles/floor.png")
        floorImage = pygame.transform.scale(floorImage, (tileSize, tileSize))
        self.floorTile = Tile.Tile("floor", floorImage, False, tileSize)
        self.tileList.append(self.floorTile)

        keyImage = pygame.image.load("Tiles/key.png")
        keyImage = pygame.transform.scale(keyImage, (tileSize, tileSize))
        self.keyTile = Tile.Tile("key", keyImage,False, tileSize)
        self.tileList.append(self.keyTile)

        doorImage = pygame.image.load("Tiles/door.png")
        doorImage = pygame.transform.scale(doorImage, (tileSize, tileSize))
        self.doorTile = Tile.Tile("door", doorImage,True, tileSize)
        self.tileList.append(self.doorTile)

    # def testPrint(self):
    #     print("MAP:\n")
    #     print(self.levelMap)



