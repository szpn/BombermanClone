import pygame

from BombermanClone.model.powerup.PowerUp import PowerUp
from BombermanClone.util.SpriteLoader import SpriteLoader


class PowerUpHealth(PowerUp):
    def __init__(self, position):
        super().__init__(position)

        self.sprite = SpriteLoader.loadSprite("poweruphealth")

    def picked_up(self, bomber):
        bomber.lives +=1

    def whoImServer(self):
        return "poweruphealth"