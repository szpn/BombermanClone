import pygame
from model.Directions import Directions


class KeyAction:
    def __init__(self, gameTohandle, isLocal):
        self.isLocal = isLocal
        self.gameTohandle = gameTohandle

    def handle(self, key):
        # nie ma switch case w pythonie XDDDDD jest tylko match ale to dla 3.10 wiec nie bedziemy wymuszać
        if key[pygame.K_a]:
            self.gameTohandle.bomberman1.move(Directions.LEFT)
        if key[pygame.K_d]:
            self.gameTohandle.bomberman1.move(Directions.RIGHT)
        if key[pygame.K_w]:
            self.gameTohandle.bomberman1.move(Directions.UP)
        if key[pygame.K_s]:
            self.gameTohandle.bomberman1.move(Directions.DOWN)
        if key[pygame.K_ESCAPE]:
            self.gameTohandle.run = False