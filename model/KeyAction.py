import pygame
from model.Directions import Directions


class KeyAction:
    def __init__(self, gameTohandle, isLocal):
        self.isLocal = isLocal
        self.gameTohandle = gameTohandle

    def handle(self, key):
        # nie ma switch case w pythonie XDDDDD jest tylko match ale to dla 3.10 wiec nie bedziemy wymuszać
        if key[pygame.K_a]:
            self.gameTohandle.bombers[0].move(Directions.LEFT)
        elif key[pygame.K_d]:
            self.gameTohandle.bombers[0].move(Directions.RIGHT)
        elif key[pygame.K_w]:
            self.gameTohandle.bombers[0].move(Directions.UP)
        elif key[pygame.K_s]:
            self.gameTohandle.bombers[0].move(Directions.DOWN)
        if key[pygame.K_ESCAPE]:
            self.gameTohandle.run = False