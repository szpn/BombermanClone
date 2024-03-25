from model.map.MapTile import MapTile
from model.map.Wall import Wall


class MapLoader():
    @staticmethod
    def loadMap(mapPath):
        with open(mapPath, 'r') as f:
            lines = f.readlines()

        size = int(lines[0])
        map = [[None for _ in range(size)] for _ in range(size)]
        spawn_points = []

        map_tiles = [line.split() for line in lines[1:]]
        for i in range(size):
            for j in range(size):
                tile_type = map_tiles[i][j]
                if tile_type == 'S':
                    map[i][j] = MapTile(i, j)
                    spawn_points.append((i,j))
                elif tile_type == 'T':
                    map[i][j] = MapTile(i, j)
                elif tile_type == 'W':
                    map[i][j] = Wall(i,j)
                else:
                    raise ValueError(f"Invalid tile type '{tile_type}' at position ({i}, {j})")