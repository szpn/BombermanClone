from BombermanClone.clientGameDisplay.GameDisplay import GameDisplay
from BombermanClone.util.MapLoader import MapLoader


class GameDisplayCreator:
    def __init__(self):
        pass

    @staticmethod
    def createGameUsingMapFile(mapName):
        gameMap = MapLoader.fromFile(mapName)
        game = GameDisplay(gameMap)
        return game