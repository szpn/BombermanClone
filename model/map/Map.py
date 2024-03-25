from model.Bomber import Bomber


class Map:
    def __init__(self, mapData):
        self.size = mapData['size']
        self.map = mapData['map']
        self.spawnPoints = mapData['spawnPoints']


    def drawMap(self, screen):
        for i in range(self.size):
            for j in range(self.size):
                tile = self.map[i][j]
                screen.blit(tile.sprite.image, tile.rect)

        for bomberman in self.bombermans:
            screen.blit(bomberman.sprite.image, bomberman.rect)
