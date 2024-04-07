import pygame

from model.powerup.PowerUp import PowerUp
from util.SpriteLoader import SpriteLoader


class PowerUpHealth(PowerUp):
    def __init__(self, position):
        super().__init__(position)

        self.sprite = SpriteLoader.loadSprite("./resources/sprites/poweruphealth.png")

    def picked_up(self, bomber):
        bomber.lives +=1