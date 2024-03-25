import pygame

from model.Bomber import Bomber
from model.KeyAction import KeyAction


class Gameloop:
    def __init__(self, mapSize):
        self.mapSize = mapSize
        self.SCREEN_WIDTH = self.mapSize
        self.SCREEN_HEIGHT = self.mapSize
        self.bomberman1 = Bomber([30, 30], 3, (255,0,0))
        self.bomberman2 = Bomber([self.mapSize, self.mapSize], 3,(128,0,0))
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_WIDTH))
        self.run = True
        self.keyHandler = KeyAction(self,True)

    def start(self):
        while self.run:
            self.screen.fill((68,85,90))
            pygame.draw.rect(self.screen,self.bomberman1.bomberApparence,self.bomberman1.body)
            # pygame.draw.rect(self.screen,self.bomberman2.body,self.bomberman2.bomberApparence)
            key = pygame.key.get_pressed()
            self.keyHandler.handle(key)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

            pygame.display.update()
        pygame.quit()