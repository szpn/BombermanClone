from threading import Thread
from time import sleep
from BombermanClone.model.game.GameCreator import GameCreator


class GameHandlerThread(Thread):
    def __init__(self, lobby, mapName='map1'):
        super().__init__()
        self.lobby = lobby
        self.mapName = mapName
        self.game = GameCreator.createGameUsingMapFile(mapName, len(lobby.players))
        self.TPS = 20

    def serializeBombers(self,game):
        data = []
        for i in range(len(game.bombers)):
            data.append([game.bombers[i].x,game.bombers[i].y])
        return data

    def serializePowerups(self,game):
        data = []
        for i in range(len(game.powerups)):
            data.append([game.powerups[i].x , game.powerups[i].y , game.powerups[i].whoImServer()])
        return data

    def run(self):
        while True:
            dupa1= self.serializeBombers(self.game)
            dupa2 = self.serializePowerups(self.game)
            sleep(1/self.TPS)
            self.game.tick()
            self.lobby.broadcastData({"map": self.game.tileCord, "bombs": self.game.bombCord, "bombers": dupa1, "fires": self.game.firesCord, "powerups": dupa2})

