import pygame

from BombermanClone.util.SpriteLoader import SpriteLoader

class DisplayTile:
    def __init__(self,position,sprite):
        self.x = position[0]
        self.y = position[1]
        self.rect = pygame.Rect(position[0] * 64, position[1] * 64, 64, 64)
        self.sprite = SpriteLoader.loadSprite(sprite)


