import pygame

from util.SpriteLoader import SpriteLoader


class PowerUp:
    def __init__(self, position):
        self.x = position[0]
        self.y = position[1]

        self.rect = pygame.Rect(position[0]*64,position[1]*64,64,64)
        self.sprite = SpriteLoader.loadSprite("./resources/sprites/unknown.png")

    def picked_up(self, bomber):
        raise NotImplementedError(f"{self.__class__.__name__} does not implement picked_up()!")