import pygame

from model.Bomber import Bomber
from model.Game import Game
from model.KeyAction import KeyAction
from model.Render import Render
from model.map.Map import Map
from util.MapLoader import MapLoader


class Gameloop:
    def __init__(self, windowSize):
        self.map = MapLoader.fromFile("./resources/map1.txt")
        self.game = Game(self.map)
        self.render = Render(self.game, windowSize)
        self.run = True
        self.keyHandler = KeyAction(self,True)

        self.game.addBombers(1)

    def start(self):
        while self.run:
            self.render.drawGame()


            self.keyHandler.handle(pygame.key.get_pressed())
            self.handleEvents()
            pygame.display.update()
        pygame.quit()

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False