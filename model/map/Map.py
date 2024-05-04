from BombermanClone.model.Bomber import Bomber


class Map:
    def __init__(self, mapData):
        self.size = mapData['size']
        self.map = mapData['map']
        self.spawnPoints = mapData['spawnPoints']


    def getObjectAt(self, x, y):
        return self.map[x][y]
