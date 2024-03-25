from model.map.MapTile import MapTile


class Wall(MapTile):
    def __init__(self, x, y):
        super().__init__(x, y)