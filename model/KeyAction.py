import pygame
import pickle
from BombermanClone.model.Directions import Directions


class KeyAction:
    def __init__(self, gameTohandle, isLocal,connection):
        self.isLocal = isLocal
        self.gameTohandle = gameTohandle
        self.connection =connection

    def setGameToHandle(self, game):
        self.gameTohandle = game

    def handle(self, key):
        # nie ma switch case w pythonie XDDDDD jest tylko match ale to dla 3.10 wiec nie bedziemy wymuszać
        if key[pygame.K_a]:
            self.connection.send_message(("LEFT"))
        if key[pygame.K_d]:
            self.connection.send_message(("RIGHT"))
        if key[pygame.K_w]:
            self.connection.send_message(("UP"))
        if key[pygame.K_s]:
            self.connection.send_message(("DOWN"))
        if key[pygame.K_e]:
            self.connection.send_message(("BOMB"))

        # if key[pygame.K_LEFT]:
        #     self.gameTohandle.moveBomber(self.gameTohandle.bombers[1], Directions.LEFT)
        # if key[pygame.K_RIGHT]:
        #     self.gameTohandle.moveBomber(self.gameTohandle.bombers[1], Directions.RIGHT)
        # if key[pygame.K_UP]:
        #     self.gameTohandle.moveBomber(self.gameTohandle.bombers[1], Directions.UP)
        # if key[pygame.K_DOWN]:
        #     self.gameTohandle.moveBomber(self.gameTohandle.bombers[1], Directions.DOWN)
        # if key[pygame.K_SLASH]:
        #     self.gameTohandle.placeBomb(self.gameTohandle.bombers[1])
        #
        # if key[pygame.K_p]:
        #     self.gameTohandle.spawnPowerUp()
        #
        # if key[pygame.K_ESCAPE]:
        #     self.gameTohandle.run = False
