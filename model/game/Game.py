from model.Bomber import Bomber
from model.Bomb import Bomb
from model.powerup.PowerUpCreator import PowerUpCreator
from util.RandomEmptyPosition import RandomEmptyPosition
from model.map.MapElement import MapElement
from model.map.MapTile import MapTile
from model.Fire import Fire


class Game:
    def __init__(self, map):
        self.map = map
        self.bombers = []
        self.bombs = []
        self.powerups = []
        self.fires = []
        self.firesCord = [[0 for _ in range(map.size)] for _ in range(map.size)]
        self.bombCord = [[0 for _ in range(map.size)] for _ in range(map.size)]
        self.spawnPowerUp()
        self.currentTick = 0

    def tick(self):
        self.tickBombs()
        self.pickupPowerUps()
        self.tickFire()
        self.currentTick += 1

    def tickBombs(self):
        for bomb in self.bombs:
            bomb.fuse -= 1
            if bomb.fuse == 0:
                self.bombBOOM(bomb)

    def tickFire(self):
        for fire in self.fires:
            fire.burn -= 1
            if fire.burn == 0:
                self.firesCord[fire.x][fire.y] -= 1
                self.fires.remove(fire)

    def pickupPowerUps(self):
        #TODO: rewrite this
        for bomber in self.bombers:
            for powerup in self.powerups:
                if bomber.x == powerup.x and bomber.y == powerup.y:
                    powerup.picked_up(bomber)
                    self.powerups.remove(powerup)


    def moveBomber(self, bomber, direction):
        if bomber not in self.bombers:
            raise ValueError("The provided bomber is not in the game!")

        if bomber.moveAvailable(self.currentTick):
            bomber.move(direction, self.map, self.firesCord)
            bomber.lastMoveTick = self.currentTick

    def addBombers(self, count):
        for i in range(count):
            if i == 0:
                self.bombers.append(Bomber(self.map.spawnPoints[0]))
            elif i == 1:
                self.bombers.append(Bomber(self.map.spawnPoints[1]))

    def placeBomb(self, bomber):
        if bomber.bombCounter < bomber.bombLimit and self.bombCord[bomber.x][bomber.y] == 0:
            self.bombCord[bomber.x][bomber.y] = 1
            self.bombs.append(Bomb([bomber.x, bomber.y], bomber.bombPower, bomber))
            bomber.bombCounter += 1
            #print("bomb has been planted")

    def spawnPowerUp(self):
        powerUpPosition = RandomEmptyPosition.generate(self)
        powerUp = PowerUpCreator.create_random_powerup(powerUpPosition)
        self.powerups.append(powerUp)

    def bombBOOM(self, bomb):
        bomb.bomber.bombCounter -= 1
        gora, dol, lewo, prawo = True, True, True, True
        self.bombCord[bomb.x][bomb.y] = 0

        for i in range(0, bomb.power + 1):
            if i == 0:
                self.bombDestroyOrNot(self.map.getObjectAt(bomb.x, bomb.y).whoImMap(), bomb.x, bomb.y)
                continue
            if gora:
                gora = self.bombDestroyOrNot(self.map.getObjectAt(bomb.x, bomb.y + i).whoImMap(), bomb.x, bomb.y + i)
            if dol:
                dol = self.bombDestroyOrNot(self.map.getObjectAt(bomb.x, bomb.y - i).whoImMap(), bomb.x, bomb.y - i)
            if lewo:
                lewo = self.bombDestroyOrNot(self.map.getObjectAt(bomb.x - i, bomb.y).whoImMap(), bomb.x - i, bomb.y)
            if prawo:
                prawo = self.bombDestroyOrNot(self.map.getObjectAt(bomb.x + i, bomb.y).whoImMap(), bomb.x + i, bomb.y)

        self.bombs.remove(bomb)

    def bombDestroyOrNot(self, mapElem, x, y):
        if mapElem == MapElement.WallDestructable:
            self.map.map[x][y] = MapTile(x, y)
            self.fires.append(Fire((x, y)))
            self.firesCord[x][y] += 1
            return False

        elif mapElem == MapElement.Maptile:
            self.fires.append(Fire((x, y)))
            self.firesCord[x][y] += 1
            for bomber in self.bombers:
                if bomber.x == x and bomber.y == y:
                    bomber.bomberDmg()
            return True

        return False
