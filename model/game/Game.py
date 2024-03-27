from model.Bomber import Bomber


class Game:
    def __init__(self, map):
        self.map = map
        self.bombers = []
        self.bomb = []

    def addBombers(self, count):
        for i in range(count):
            self.bombers.append(Bomber([0, 0]))


    def tick(self):
        self.tickBombs()
        self.pickupPowerUps()


    def tickBombs(self):
        pass

    def pickupPowerUps(self):
        pass

    def moveBomber(self, bomber, direction):
        if bomber not in self.bombers:
            raise ValueError("The provided bomber is not in the game!")
        bomber.move(direction)
        #TODO: finish this

    def placeBomb(self):
        pass

    def spawnPowerUp(self):
        pass