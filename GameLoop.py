import pygame

from model.game.Game import Game
from model.KeyAction import KeyAction
from model.game.GameRender import GameRender
from util.MapLoader import MapLoader


class GameLoop:
    def __init__(self, screen, game=None):
        self.game = game
        self.keyHandler = KeyAction(self.game, True)
        self.render = GameRender(screen)

    def setGame(self, game):
        self.game = game
        self.keyHandler.setGameToHandle(game)
        self.render.setGameToRender(game)

    def tick(self):
        if self.game is None:
            raise RuntimeError("GameLoop tried to process a non-exisitng game!")
        self.game.tick()

        self.render.drawGame()
        self.keyHandler.handle(pygame.key.get_pressed())

