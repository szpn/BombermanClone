import pygame

from model.Bomber import Bomber
from model.Game import Game
from model.KeyAction import KeyAction
from model.Render import Render
from model.map.Map import Map
from util.MapLoader import MapLoader


class Gameloop:
    def __init__(self, windowSize):
        self.run = True

        self.map = MapLoader.fromFile("./resources/map2.txt")
        self.game = Game(self.map)
        self.keyHandler = KeyAction(self.game, True)
        self.render = Render(self.game, windowSize)

        self.game.addBombers(1)

    def start(self):
        clock = pygame.time.Clock()
        while self.run:
            self.render.drawGame()

            self.keyHandler.handle(pygame.key.get_pressed())
            self.handleEvents()
            pygame.display.update()
            clock.tick(15)
        pygame.quit()

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False