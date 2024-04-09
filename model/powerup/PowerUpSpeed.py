import pygame

from model.powerup.PowerUp import PowerUp
from util.SpriteLoader import SpriteLoader


class PowerUpSpeed(PowerUp):
    def __init__(self, position):
        super().__init__(position)

        self.sprite = SpriteLoader.loadSprite("./resources/sprites/powerupspeed.png")

    def picked_up(self, bomber):
        bomber.ticksNeededToMove -= 1