import pygame

from model.powerup.PowerUp import PowerUp
from util.SpriteLoader import SpriteLoader


class PowerUpBombCount(PowerUp):
    def __init__(self, position):
        super().__init__(position)

        self.sprite = SpriteLoader.loadSprite("./resources/sprites/powerupbombcount.png")

    def picked_up(self, bomber):
        bomber.bombLimit +=1