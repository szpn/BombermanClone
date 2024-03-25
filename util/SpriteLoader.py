import pygame


class SpriteLoader(object):
    loadedSprites = {}
    @classmethod
    def loadSprite(cls, path):
        if path in cls.loadedSprites:
            return cls.loadedSprites[path]

        img = pygame.image.load(path)
        sprite = pygame.sprite.Sprite()
        sprite.image = img
        cls.loadedSprites[path] = sprite
        return sprite