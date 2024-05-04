from random import choice

from BombermanClone.model.powerup.PowerUpSpeed import PowerUpSpeed
from BombermanClone.model.powerup.PowerUpBombCount import PowerUpBombCount
from BombermanClone.model.powerup.PowerUpBombPower import PowerUpBombPower
from BombermanClone.model.powerup.PowerUpHealth import PowerUpHealth


class PowerUpCreator:
    available_powerups = [PowerUpHealth, PowerUpBombCount, PowerUpBombPower, PowerUpSpeed]


    @staticmethod
    def create_random_powerup(position):
        return choice(PowerUpCreator.available_powerups)(position)
