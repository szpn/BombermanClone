import pygame

from BombermanClone.model.powerup.PowerUp import PowerUp
from BombermanClone.util.SpriteLoader import SpriteLoader


class PowerUpBombCount(PowerUp):
    def __init__(self, position):
        super().__init__(position)

        self.sprite = SpriteLoader.loadSprite("powerupbombcount")

    def picked_up(self, bomber):
        bomber.bombLimit +=1

    def whoImServer(self):
        return "powerupbombcount"