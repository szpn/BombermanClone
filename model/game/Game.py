from model.Bomber import Bomber
from model.powerup.PowerUpCreator import PowerUpCreator
from util.RandomEmptyPosition import RandomEmptyPosition


class Game:
    def __init__(self, map):
        self.map = map
        self.bombers = []
        self.bomb = []
        self.powerups = []
        self.spawnPowerUp()
        self.currentTick = 0



    def tick(self):
        self.tickBombs()
        self.pickupPowerUps()
        self.currentTick += 1

    def tickBombs(self):
        pass

    def pickupPowerUps(self):
        pass

    def moveBomber(self, bomber, direction):
        if bomber not in self.bombers:
            raise ValueError("The provided bomber is not in the game!")
        if self.currentTick - bomber.lastMoveTick > 25:
            bomber.move(direction)
            bomber.lastMoveTick = self.currentTick

        #TODO: finish this


    def addBombers(self, count):
        for i in range(count):
            if i == 0:
                self.bombers.append(Bomber([0, 0]))
            elif i == 1:
                self.bombers.append(Bomber([self.map.size-1,self.map.size-1]))
    def placeBomb(self):
        pass

    def spawnPowerUp(self):
        powerUpPosition = RandomEmptyPosition.generate(self)
        powerUp = PowerUpCreator.create_random_powerup(powerUpPosition)
        self.powerups.append(powerUp)
