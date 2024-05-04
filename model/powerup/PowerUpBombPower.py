import pygame

from BombermanClone.model.powerup.PowerUp import PowerUp
from BombermanClone.util.SpriteLoader import SpriteLoader


class PowerUpBombPower(PowerUp):
    def __init__(self, position):
        super().__init__(position)

        self.sprite = SpriteLoader.loadSprite("powerupbombpower")

    def picked_up(self, bomber):
        bomber.bombPower +=1

    def whoImServer(self):
        return "powerupbombpower"