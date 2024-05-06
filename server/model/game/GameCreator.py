from server.model.game.Game import Game
from util.MapLoader import MapLoader


class GameCreator:
    def __init__(self):
        pass

    @staticmethod
    def createGameUsingMapFile(mapName, bomberCount):
        gameMap = MapLoader.fromFile(mapName)
        game = Game(gameMap)
        game.addBombers(bomberCount)
        return game