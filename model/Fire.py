import pygame

from util.SpriteLoader import SpriteLoader

class Fire:
    def __init__(self,position,game):
        self.game = game
        self.x = position[0]
        self.y = position[1]
        self.burn = 50
        self.rect = pygame.Rect(position[0] * 64, position[1] * 64, 64, 64)
        self.sprite = SpriteLoader.loadSprite("./resources/sprites/fire.png")
