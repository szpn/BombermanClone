import pygame

from model.game.Game import Game
from model.KeyAction import KeyAction
from model.game.GameRender import GameRender
from clientGameDisplay.DisplayTile import DisplayTile
from clientGameDisplay.DisplayMap import DisplayMap

from util.MapLoader import MapLoader


class GameLoop:
    def __init__(self, screen,connection, game=None,):
        self.game = game
        self.keyHandler = KeyAction(self.game, True,connection)
        self.render = GameRender(screen)
        self.connection = connection

    def setGame(self, game):
        self.game = game
        self.keyHandler.setGameToHandle(game)
        self.render.setGameToRender(game)

    def updateGame(self, info , game):
        if type(info) is dict:
            self.updateMap(info["map"],game)
            self.updateFires(info["fires"],game)
            self.updateBombs(info["bombs"],game)
            self.updateBombers(info["bombers"],game)
            self.updatePowerups(info["powerups"],game)

    def updateMap(self,mapArr,game):
        mapToEnter = [[0 for _ in range(game.map.size)] for _ in range(game.map.size)]
        for i in range(len(mapArr)):
            for j in range(len(mapArr)):
                mapToEnter[i][j] = (DisplayTile((i,j),mapArr[i][j]))
        game.map = DisplayMap(len(mapToEnter),mapToEnter)
    def updateFires(self,mapArr,game):
        game.fires.clear()
        for i in range(len(mapArr)):
            for j in range(len(mapArr)):
                if mapArr[i][j] == 1:
                    game.fires.append(DisplayTile((i,j),"fire"))
    def updateBombs(self,mapArr,game):
        game.bombs.clear()
        for i in range(len(mapArr)):
            for j in range(len(mapArr)):
                if mapArr[i][j] == 1:
                    game.bombs.append(DisplayTile((i,j),"bomb"))
    def updateBombers(self,mapArr,game):
        game.bombers.clear()
        for i in range(len(mapArr)):
                game.bombers.append(DisplayTile((mapArr[i][0],mapArr[i][1]),"bomber"))
    def updatePowerups(self,mapArr,game):
        game.powerups.clear()
        for i in range(len(mapArr)):
                game.powerups.append(DisplayTile((mapArr[i][0],mapArr[i][1]),mapArr[i][2]))


    def tick(self):
        if self.game is None:
            raise RuntimeError("GameLoop tried to process a non-exisitng game!")

        self.render.drawGame()
        self.keyHandler.handle(pygame.key.get_pressed())
        self.updateGame(self.connection.lastMessage, self.game)
