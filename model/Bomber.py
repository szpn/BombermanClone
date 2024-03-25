import pygame

from util.SpriteLoader import SpriteLoader


class Bomber:
    def __init__(self, position, lives):
        print(position[1])
        self.lives = lives
        self.position = position
        self.rect = pygame.Rect((position[0],position[1],64,64))
        self.sprite = SpriteLoader.loadSprite("./resources/sprites/bomber.png")
    def move(self,direction):
        #TODO tu trzeba będize jakiś validator dowalić ale kolizji póki co nie ogarniam i no bez mapy też cięzko
        self.rect.move_ip(direction.value)
        return '@'

    def printHi(self):
        print("im working")

        