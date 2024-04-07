from model.map.MapTile import MapTile
from util.SpriteLoader import SpriteLoader


class Wall(MapTile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.sprite = SpriteLoader.loadSprite('./resources/sprites/wall.png')


    def isEmpty(self):
        return False