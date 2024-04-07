import pygame

from util.SpriteLoader import SpriteLoader


class MapTile:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x*64, y*64, 64, 64)
        self.sprite = SpriteLoader.loadSprite('./resources/sprites/tile.png')


    def isEmpty(self):
        return True