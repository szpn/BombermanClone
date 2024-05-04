import pygame

from BombermanClone.util.SpriteLoader import SpriteLoader

class Bomb:
    def __init__(self,position,power,bomber):
        self.x = position[0]
        self.y = position[1]
        self.power = power
        self.fuse = 250
        self.rect = pygame.Rect(position[0] * 64, position[1] * 64, 64, 64)
        self.sprite = SpriteLoader.loadSprite("bomb")
        self.bomber = bomber

