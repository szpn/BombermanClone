from random import choice

from model.powerup.PowerUpBombCount import PowerUpBombCount
from model.powerup.PowerUpHealth import PowerUpHealth


class PowerUpCreator:
    available_powerups = [PowerUpHealth, PowerUpBombCount]


    @staticmethod
    def create_random_powerup(position):
        return choice(PowerUpCreator.available_powerups)(position)
