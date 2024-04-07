from model.Bomber import Bomber
from model.Bomb import Bomb
from model.powerup.PowerUpCreator import PowerUpCreator
from util.RandomEmptyPosition import RandomEmptyPosition


class Game:
    def __init__(self, map):
        self.map = map
        self.bombers = []
        self.bombs = []
        self.powerups = []
        self.spawnPowerUp()
        self.currentTick = 0



    def tick(self):
        self.tickBombs()
        self.pickupPowerUps()
        self.currentTick += 1

    def tickBombs(self):
        for bomb in self.bombs:
            bomb.fuse-=1
            if bomb.fuse == 0:
                bomb.bombExplode()


    def pickupPowerUps(self):
        pass

    def moveBomber(self, bomber, direction):
        if bomber not in self.bombers:
            raise ValueError("The provided bomber is not in the game!")
        #tutaj możeesz zmienić jak szybko się ruszają
        if self.currentTick - bomber.lastMoveTick > 15:
            bomber.move(direction,self.map)
            bomber.lastMoveTick = self.currentTick


    def addBombers(self, count):
        for i in range(count):
            if i == 0:
                self.bombers.append(Bomber([1, 1]))
            elif i == 1:
                self.bombers.append(Bomber([self.map.size-2,self.map.size-2]))
    def placeBomb(self,bomber):
        if bomber.bombCounter < bomber.bombLimit:
            self.bombs.append(Bomb([bomber.x,bomber.y],bomber.bombPower,bomber,self))
            bomber.bombCounter +=1
            # print("bomb has been planted")

    def spawnPowerUp(self):
        powerUpPosition = RandomEmptyPosition.generate(self)
        powerUp = PowerUpCreator.create_random_powerup(powerUpPosition)
        self.powerups.append(powerUp)

    def bombBOOM(self,bomb):
        self.bombs.remove(bomb)
