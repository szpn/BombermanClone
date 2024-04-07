import pygame

class GameRender:
    def __init__(self, screen, game=None):
        self.screen = screen
        self.game = game
        self.scale_factor = 2  # Define the scale factor

    def drawGame(self):
        self.cleanWindow()
        self.drawMap(self.game.map)
        self.drawBombers(self.game.bombers)
        self.drawPowerUps(self.game.powerups)
        pygame.display.update()

    def cleanWindow(self):
        self.screen.fill((68, 85, 90))

    def drawMap(self, map):
        for i in range(map.size):
            for j in range(map.size):
                tile = map.map[i][j]
                scaled_image = pygame.transform.scale(tile.sprite.image, (tile.sprite.image.get_width() * self.scale_factor, tile.sprite.image.get_height() * self.scale_factor))
                self.screen.blit(scaled_image, (tile.rect.x * self.scale_factor, tile.rect.y * self.scale_factor))

    def drawBombers(self, bombers):
        for bomber in bombers:
            scaled_image = pygame.transform.scale(bomber.sprite.image, (bomber.sprite.image.get_width() * self.scale_factor, bomber.sprite.image.get_height() * self.scale_factor))
            self.screen.blit(scaled_image, (bomber.rect.x * self.scale_factor, bomber.rect.y * self.scale_factor))

    def drawPowerUps(self, powerups):
        for powerup in powerups:
            scaled_image = pygame.transform.scale(powerup.sprite.image, (powerup.sprite.image.get_width() * self.scale_factor, powerup.sprite.image.get_height() * self.scale_factor))
            self.screen.blit(scaled_image, (powerup.rect.x * self.scale_factor, powerup.rect.y * self.scale_factor))

    def setGameToRender(self, game):
        self.game = game
