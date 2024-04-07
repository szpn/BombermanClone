from model.map.MapTile import MapTile
from util.SpriteLoader import SpriteLoader
from model.map.MapElement import MapElement

class WallDestructable(MapTile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.sprite = SpriteLoader.loadSprite('./resources/sprites/wall_destructable.png')


    def isEmpty(self):
        return False

    def whoImMap(self):
        return MapElement.WallDestructable