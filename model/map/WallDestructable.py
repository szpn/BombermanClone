from BombermanClone.model.map.MapTile import MapTile
from BombermanClone.util.SpriteLoader import SpriteLoader
from BombermanClone.model.map.MapElement import MapElement

class WallDestructable(MapTile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.sprite = SpriteLoader.loadSprite('wall_destructable')


    def isEmpty(self):
        return False

    def whoImMap(self):
        return MapElement.WallDestructable