from threading import Thread
from time import sleep
from model.game.GameCreator import GameCreator


class GameHandlerThread(Thread):
    def __init__(self, lobby, mapName='map1'):
        super().__init__()
        self.lobby = lobby
        self.mapName = mapName
        self.game = GameCreator.createGameUsingMapFile(mapName, len(lobby.players))
        self.TPS = 60


    def run(self):
        while True:
            sleep(1/self.TPS)
            self.game.tick()
            self.lobby.broadcastData("game ticked!")

