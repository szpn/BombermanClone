from threading import Thread
from time import sleep

from server.model.Directions import Directions
from server.model.game.GameCreator import GameCreator


class GameHandlerThread(Thread):
    def __init__(self, lobby, mapName='map1'):
        super().__init__()
        self.lobby = lobby
        self.game = GameCreator.createGameUsingMapFile(mapName, 0)
        self.TPS = 60

        self.selectedMap = 'map1'


    def run(self):
        self.game = GameCreator.createGameUsingMapFile(self.selectedMap, len(self.lobby.players))
        self.lobby.broadcastData({"id": "GAME_STARTED"})
        while self.game.isGame:
            sleep(1/self.TPS)
            self.game.tick()
            self.lobby.broadcastData({"id": "GAME_STATE", "data": self.game.serialize()})
        self.lobby.broadcastData({"id":"END_STATE","data": self.game.bomberScore})


    def handleClientGameMessage(self, message, actingPlayer):
        if message['id'] == 'ACTION':
            action = message['action']
            if action == "LEFT":
                self.game.moveBomber(self.game.bombers[actingPlayer], Directions.LEFT)
            if action == "RIGHT":
                self.game.moveBomber(self.game.bombers[actingPlayer], Directions.RIGHT)
            if action == "UP":
                self.game.moveBomber(self.game.bombers[actingPlayer], Directions.UP)
            if action == "DOWN":
                self.game.moveBomber(self.game.bombers[actingPlayer], Directions.DOWN)
            if action == "BOMB":
                self.game.placeBomb(self.game.bombers[actingPlayer])
