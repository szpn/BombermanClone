import pygame
from model.Directions import Directions


class KeyAction:
    def __init__(self, gameTohandle, isLocal):
        self.isLocal = isLocal
        self.gameTohandle = gameTohandle

    def setGameToHandle(self, game):
        self.gameTohandle = game

    def handle(self, key):
        # nie ma switch case w pythonie XDDDDD jest tylko match ale to dla 3.10 wiec nie bedziemy wymuszać
        if key[pygame.K_a]:
            self.gameTohandle.moveBomber(self.gameTohandle.bombers[0], Directions.LEFT, )
        if key[pygame.K_d]:
            self.gameTohandle.moveBomber(self.gameTohandle.bombers[0], Directions.RIGHT)
        if key[pygame.K_w]:
            self.gameTohandle.moveBomber(self.gameTohandle.bombers[0], Directions.UP)
        if key[pygame.K_s]:
            self.gameTohandle.moveBomber(self.gameTohandle.bombers[0], Directions.DOWN)
        if key[pygame.K_e]:
            self.gameTohandle.placeBomb(self.gameTohandle.bombers[0])

        if key[pygame.K_LEFT]:
            self.gameTohandle.moveBomber(self.gameTohandle.bombers[1], Directions.LEFT)
        if key[pygame.K_RIGHT]:
            self.gameTohandle.moveBomber(self.gameTohandle.bombers[1], Directions.RIGHT)
        if key[pygame.K_UP]:
            self.gameTohandle.moveBomber(self.gameTohandle.bombers[1], Directions.UP)
        if key[pygame.K_DOWN]:
            self.gameTohandle.moveBomber(self.gameTohandle.bombers[1], Directions.DOWN)
        if key[pygame.K_SLASH]:
            self.gameTohandle.placeBomb(self.gameTohandle.bombers[1])

        if key[pygame.K_ESCAPE]:
            self.gameTohandle.run = False
