from random import choice

from model.powerup.PowerUpSpeed import PowerUpSpeed
from model.powerup.PowerUpBombCount import PowerUpBombCount
from model.powerup.PowerUpBombPower import PowerUpBombPower
from model.powerup.PowerUpHealth import PowerUpHealth


class PowerUpCreator:
    available_powerups = [PowerUpHealth, PowerUpBombCount, PowerUpBombPower, PowerUpSpeed]


    @staticmethod
    def create_random_powerup(position):
        return choice(PowerUpCreator.available_powerups)(position)
