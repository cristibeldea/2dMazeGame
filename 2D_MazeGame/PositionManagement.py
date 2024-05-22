import pygame
from Settings import *


class PositionManagement:
    def __init__(self, mapManage, levelMap):
        self.mapManage = mapManage
        self.levelMap = levelMap

        self.insideTileX = tileSize
        self.insideTileY = tileSize
        self.player_position = [mapSize // 2, mapSize // 2]

        self.front = 0
        self.back = 0
        self.right = 0
        self.left = 0

        self.changeRate = 17

    def getTile(self, i, j):
        currentTile = self.levelMap[i + self.player_position[1] - heightTiles//2][j + self.player_position[0] - widthTiles//2]
        #print (currentTile,end=" ")

        if (currentTile == 1):
            return self.mapManage.wallTile
        elif (currentTile == 0):
            return self.mapManage.floorTile
        elif (currentTile == 2):
            return self.mapManage.keyTile
        elif (currentTile == 3):
            return self.mapManage.doorTile

    def translateIntoTile(self, x, y):
        if self.levelMap[y][x] == 0:
            return self.mapManage.floorTile
        elif self.levelMap[y][x] == 1:
            return self.mapManage.wallTile
        elif self.levelMap[y][x] == 2:
            return self.mapManage.keyTile
        elif self.levelMap[y][x] == 3:
            return self.mapManage.doorTile

    def canMove(self, keyPressed):
        if keyPressed[pygame.K_w]:
            upperTile = self.translateIntoTile(self.player_position[0], self.player_position[1] - 1)
            print(self.player_position)
            if upperTile.isSolid and self.insideTileY < tileSize/3:
                return False
            else:
                return True

        elif keyPressed[pygame.K_a]:
            leftTile = self.translateIntoTile(self.player_position[0] - 1, self.player_position[1])
            if leftTile.isSolid and self.insideTileX < tileSize/2:
                return False
            else:
                return True

        elif keyPressed[pygame.K_s]:
            lowerTile = self.translateIntoTile(self.player_position[0], self.player_position[1] + 1)
            if lowerTile.isSolid and self.insideTileY > tileSize/3:
                return False
            else:
                return True

        elif keyPressed[pygame.K_d]:
            rightTile = self.translateIntoTile(self.player_position[0] + 1, self.player_position[1])
            if rightTile.isSolid and self.insideTileX > tileSize/2:
                return False
            else:
                return True

    def move(self, keyPressed):
        if keyPressed[pygame.K_w] and self.canMove(keyPressed):
            self.insideTileY -= step
        elif keyPressed[pygame.K_a] and self.canMove(keyPressed):
            self.insideTileX -= step
        elif keyPressed[pygame.K_s] and self.canMove(keyPressed):
            self.insideTileY += step
        elif keyPressed[pygame.K_d] and self.canMove(keyPressed):
            self.insideTileX += step

    # def playerNotOutOfMap(self):
    #     if(self.player_position[0] < widthTiles and self.player_position[0] > 0):
    #         if(self.player_position[1] < heightTiles and self.player_position[1] > 0):
    #             return True
    #         else:
    #             return False

    def changePosition(self, xIncrement, yIncrement):
        self.player_position[0] += xIncrement
        self.player_position[1] += yIncrement

    def checkAndChangePosition(self):
        xIncrement = 0
        yIncrement = 0
        if self.insideTileX < 0:
            self.insideTileX = tileSize
            xIncrement = -1
        elif self.insideTileX > tileSize:
            self.insideTileX = 0
            xIncrement = 1

        if self.insideTileY < 0:
            self.insideTileY = tileSize
            yIncrement = -1
        elif self.insideTileY > tileSize:
            self.insideTileY = 0
            yIncrement = 1

        self.changePosition(xIncrement, yIncrement)

    def getDetailedPosition(self):
        position = [self.player_position[0] + self.insideTileX / tileSize,
                    self.player_position[1] + self.insideTileY / tileSize]

        return position
