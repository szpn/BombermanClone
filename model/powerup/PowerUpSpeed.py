import pygame

from BombermanClone.model.powerup.PowerUp import PowerUp
from BombermanClone.util.SpriteLoader import SpriteLoader


class PowerUpSpeed(PowerUp):
    def __init__(self, position):
        super().__init__(position)

        self.sprite = SpriteLoader.loadSprite("powerupspeed")

    def picked_up(self, bomber):
        bomber.ticksNeededToMove -= 1

    def whoImServer(self):
        return "powerupspeed"