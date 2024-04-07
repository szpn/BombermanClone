import pygame

from util.SpriteLoader import SpriteLoader


class Bomber:

    def __init__(self, position, lives=3):
        self.lives = lives
        self.x = position[0]
        self.y = position[1]
        self.rect = pygame.Rect(position[0]*64,position[1]*64,64,64)
        self.sprite = SpriteLoader.loadSprite("./resources/sprites/bomber.png")
        self.lastMoveTick=0
        self.bombLimit = 1
        self.bombCounter = 0
        self.bombPower = 1
    def move(self,direction,board):
        #TODO tu trzeba będize jakiś validator dowalić ale kolizji póki co nie ogarniam i no bez mapy też cięzko
        dir_x = direction.value[0]
        dir_y = direction.value[1]
        print(board.getObjectAt(dir_x+self.x,dir_y+self.y).isEmpty())
        if board.getObjectAt(dir_x+self.x,dir_y+self.y).isEmpty():
            self.x += dir_x
            self.y += dir_y
            self.rect.move_ip(dir_x*64, dir_y*64)
        return '@'

    def printHi(self):
        print("im working")

        