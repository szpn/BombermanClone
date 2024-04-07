from random import choice

from model.powerup.PowerUpHealth import PowerUpHealth


class PowerUpCreator:
    available_powerups = [PowerUpHealth]


    @staticmethod
    def create_random_powerup(position):
        return choice(PowerUpCreator.available_powerups)(position)
