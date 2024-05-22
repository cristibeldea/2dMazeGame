import pygame
import Tile
from Settings import *
class Player:
    def __init__(self):

        self.keyTaken = False

        self.playerImage = pygame.image.load("Tiles/player.png")
        self.playerImage = pygame.transform.scale(self.playerImage, (tileSize, tileSize))
        self.playerTile = Tile.Tile("player", self.playerImage, False, tileSize)

        self.frontRightWalkingImage = pygame.image.load("Tiles/walkingFrontRightFoot.png")
        self.frontRightWalkingImage = pygame.transform.scale(self.frontRightWalkingImage, (tileSize, tileSize))

        self.frontLeftWalkingImage = pygame.image.load("Tiles/walkingFrontLeftFoot.png")
        self.frontLeftWalkingImage = pygame.transform.scale(self.frontLeftWalkingImage, (tileSize, tileSize))

        self.leftStanding = pygame.image.load("Tiles/standingLeft (1).png")
        self.leftStanding = pygame.transform.scale(self.leftStanding, (tileSize, tileSize))

        self.leftWalking1 = pygame.image.load("Tiles/walkingLeft1.png")
        self.leftWalking1 = pygame.transform.scale(self.leftWalking1, (tileSize, tileSize))

        self.leftWalking2 = pygame.image.load("Tiles/walkingLeft2.png")
        self.leftWalking2 = pygame.transform.scale(self.leftWalking2, (tileSize, tileSize))

        self.backWalkingRightFoot = pygame.image.load("Tiles/walkingBackRightFoot.png")
        self.backWalkingRightFoot = pygame.transform.scale(self.backWalkingRightFoot, (tileSize, tileSize))

        self.backWalkingLeftFoot = pygame.image.load("Tiles/walkingBackLeftFoot.png")
        self.backWalkingLeftFoot = pygame.transform.scale(self.backWalkingLeftFoot, (tileSize, tileSize))

        self.rightWalking1 = pygame.image.load("Tiles/walkingRight1.png")
        self.rightWalking1 = pygame.transform.scale(self.rightWalking1,(tileSize, tileSize))

        self.rightWalking2 = pygame.image.load("Tiles/walkingRight2.png")
        self.rightWalking2 = pygame.transform.scale(self.rightWalking2, (tileSize, tileSize))


        #self.tileList.append(playerTile)

    def changePlayerImage(self, description):
        if description == "frontRightFoot":
            self.playerTile.image = self.frontRightWalkingImage

        if description == "standing":
            self.playerTile.image = self.playerImage

        if description == "frontLeftFoot":
            self.playerTile.image = self.frontLeftWalkingImage

        if description == "left1":
            self.playerTile.image = self.leftWalking1

        # if description == "leftStanding":
        #     self.playerTile.image = self.leftStanding

        if description == "left2":
            self.playerTile.image = self.leftWalking2

        if description == "backRightFoot":
            self.playerTile.image = self.backWalkingRightFoot

        if description == "backLeftFoot":
            self.playerTile.image = self.backWalkingLeftFoot

        if description == "right1":
            self.playerTile.image = self.rightWalking1

        if description == "right2":
            self.playerTile.image = self.rightWalking2





