import pygame

class Render:
    def __init__(self, game, windowSize):
        self.game = game
        self.SCREEN_WIDTH = windowSize
        self.SCREEN_HEIGHT = windowSize
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_WIDTH))

    def drawGame(self):
        self.cleanWindow()
        self.drawMap(self.game.map)
        self.drawBombers(self.game.bombers)
        pygame.display.update()

    def cleanWindow(self):
        self.screen.fill((68, 85, 90))

    def drawMap(self, map):
        for i in range(map.size):
            for j in range(map.size):
                tile = map.map[i][j]
                self.screen.blit(tile.sprite.image, tile.rect)

    def drawBombers(self, bombers):
        for bomber in bombers:
            self.screen.blit(bomber.sprite.image, bomber.rect)
