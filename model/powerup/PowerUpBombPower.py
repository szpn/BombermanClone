import pygame

from model.powerup.PowerUp import PowerUp
from util.SpriteLoader import SpriteLoader


class PowerUpBombPower(PowerUp):
    def __init__(self, position):
        super().__init__(position)

        self.sprite = SpriteLoader.loadSprite("powerupbombpower")

    def picked_up(self, bomber):
        bomber.bombPower +=1