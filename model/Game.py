from model.Bomber import Bomber


class Game:
    def __init__(self, map):
        self.map = map
        self.bombers = []

    def addBombers(self, count):
        for i in range(count):
            self.bombers.append(Bomber([30, 30], 3))