import pygame

from BombermanClone.util.SpriteLoader import SpriteLoader

class DisplayMap:
    def __init__(self,size,map):
        self.map = map
        self.size = size

