from model.map.MapTile import MapTile
from util.SpriteLoader import SpriteLoader


class WallDestructable(MapTile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.sprite = SpriteLoader.loadSprite('./resources/sprites/wall_destructable.png')


    def isEmpty(self):
        return False