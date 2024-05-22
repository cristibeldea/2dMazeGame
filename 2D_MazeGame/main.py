import threading

import pygame, sys

import PositionManagement
import MapManagement
import Player
from Settings import *

class Game:
    def __init__(self):
        pygame.init()
        self.running = True
        self.screen = pygame.display.set_mode((screenWidth, screenHeight))
        self.clock = pygame.time.Clock()

        self.levelMap = []
        with open("map.txt", "r") as mapFile:
            self.map = mapFile.read()
        self.map = self.map.split("\n")

        for row in self.map:
            mapRow = []
            for digit in row:
                digit = int(digit)
                mapRow.append(digit)
            self.levelMap.append(mapRow)

        # self.mapWidth = len(mapRow)
        # self.mapHeight = len(self.levelMap)
        #self.mapManage.testPrint()
        self.mapManage = MapManagement.MapManagement(self.levelMap)
        self.posManage = PositionManagement.PositionManagement(self.mapManage, self.levelMap)
        self.player = Player.Player()

        self.wonGame = False

    def checkKeyTaken(self):
        if self.posManage.player_position[0] == keyPosition[0] and self.posManage.player_position[1] == keyPosition[1]:
            self.player.keyTaken = True
            self.levelMap[keyPosition[1]][keyPosition[0]] = 0

    def checkOpenedDoor(self):
        if self.posManage.player_position[0] == doorPosition[0] and self.posManage.player_position[1] == doorPosition[1] + 1:
            if(self.player.keyTaken):
                self.mapManage.doorTile.isSolid = False

    def checkExitMaze(self):
        if self.posManage.player_position[0] == doorPosition[0] and self.posManage.player_position[1] == doorPosition[1]:
            if(self.player.keyTaken):
                self.levelMap[doorPosition[1]][doorPosition[0]] = 0

    def checkWinnedGame(self):
        if self.posManage.player_position[1] < doorPosition[1] - 1:
            self.wonGame = True

    # def resetGame(self):
    #     if __name__ == "__main__":
    #         gameManagement = Game()
    #         gameManagement.run()
    def checkPlayerHasQuitted(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):

        self.keyPressed = pygame.key.get_pressed()
        self.posManage.move(self.keyPressed)


        self.posManage.checkAndChangePosition()
        self.checkKeyTaken()
        self.checkOpenedDoor()
        self.checkExitMaze()
        self.checkWinnedGame()
        threading.Thread(target = self.drawScreen())

        pygame.display.update()
        self.clock.tick(FPS)


    def run(self):
        while self.running:
            self.checkPlayerHasQuitted()
            if(not self.wonGame):
                self.update()
            else:
                pygame.time.wait(3000)
                exit()


    def drawMap(self):
        for i in range(0, heightTiles+1):
            for j in range(0, widthTiles+1):
                #currentTileToDraw = self.mapManage.getTile(i+1, j+1)
                currentTileToDraw = self.posManage.getTile(i, j)
                self.screen.blit(currentTileToDraw.image, (j*tileSize - self.posManage.insideTileX, i*tileSize - self.posManage.insideTileY) )
            #print("\n")

    def drawPlayer(self):
        # position_toDraw = self.posManage.getDetailedPosition()
        # self.screen.blit(self.player.playerTile.image, (position_toDraw[0] * tileSize, position_toDraw[1] * tileSize) )
        if (self.keyPressed[pygame.K_s]):
            if (self.posManage.front < self.posManage.changeRate):
                self.player.changePlayerImage("frontRightFoot")

            elif (self.posManage.front >= self.posManage.changeRate):
                self.player.changePlayerImage("frontLeftFoot")

            self.posManage.front += 1
            if (self.posManage.front == 2* self.posManage.changeRate):
                self.posManage.front = 0

        elif self.keyPressed[pygame.K_a]:
            if self.posManage.left < self.posManage.changeRate:
                self.player.changePlayerImage("left1")

            elif self.posManage.left >= self.posManage.changeRate:
                self.player.changePlayerImage("left2")

            self.posManage.left += 1
            if (self.posManage.left == 2* self.posManage.changeRate):
                self.posManage.left = 0

        elif self.keyPressed[pygame.K_w]:
            if self.posManage.back < self.posManage.changeRate:
                self.player.changePlayerImage("backRightFoot")

            elif self.posManage.back >= self.posManage.changeRate:
                self.player.changePlayerImage("backLeftFoot")

            self.posManage.back += 1
            if (self.posManage.back == 2 * self.posManage.changeRate):
                self.posManage.back = 0

        elif self.keyPressed[pygame.K_d]:
            if self.posManage.right < self.posManage.changeRate:
                self.player.changePlayerImage("right1")

            elif self.posManage.right >= self.posManage.changeRate:
                self.player.changePlayerImage("right2")

            self.posManage.right += 1
            if (self.posManage.right == 2 * self.posManage.changeRate):
                self.posManage.right = 0

        else:
            self.player.changePlayerImage("standing")
        self.screen.blit(self.player.playerTile.image, screenCenter)

    def drawWinScreen(self):
        winImage = pygame.image.load("Tiles/win.png")
        winImage = pygame.transform.scale(winImage, (4 * tileSize, 2 * tileSize))
        self.screen.fill((0,0,0))
        self.screen.blit(winImage,
                         ((screenWidth - 4*tileSize) / 2, (screenHeight - 2*tileSize) / 2))


    def drawScreen(self):
        self.screen.fill((0, 0, 0))
        #draw map
        self.drawMap()
        self.drawPlayer()

        if self.wonGame:
            self.drawWinScreen()
        #draw player


        #draw movable objects

if __name__ == "__main__":
    gameManagement = Game()
    gameManagement.run()
