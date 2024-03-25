import pygame

class Bomber:
    def __init__(self, position, lives, bomberApparence):
        print(position[1])
        self.lives = lives
        self.position = position
        self.body = pygame.Rect((position[0],position[1],10,10))
        self.bomberApparence = bomberApparence
    def move(self,direction):
        #TODO tu trzeba będize jakiś validator dowalić ale kolizji póki co nie ogarniam i no bez mapy też cięzko
        self.body.move_ip(direction.value)
        return '@'

    def printHi(self):
        print("im working")

        