import pygame

class GameRender:
    def __init__(self, screen, game=None):
        self.screen = screen
        self.game = game
        self.scale_factor = 1.0

    def drawGame(self):
        self.cleanWindow()
        self.drawMap(self.game.map)
        self.drawBombers(self.game.bombers)
        self.drawPowerUps(self.game.powerups)
        self.drawBombs(self.game.bombs)
        self.drawFires(self.game.fires)
        pygame.display.update()

    def cleanWindow(self):
        self.screen.fill((68, 85, 90))

    def scaleImageAndRect(self, image, rect):
        scaled_image = pygame.transform.scale(image, (int(64 * self.scale_factor), int(64 * self.scale_factor)))
        scaled_rect = scaled_image.get_rect(topleft=(rect.x * self.scale_factor, rect.y * self.scale_factor))
        return scaled_image, scaled_rect

    def drawMap(self, map):
        for i in range(map.size):
            for j in range(map.size):
                tile = map.map[i][j]
                scaled_image, scaled_rect = self.scaleImageAndRect(tile.sprite.image, tile.rect)
                self.screen.blit(scaled_image, scaled_rect)

    def drawBombers(self, bombers):
        for bomber in bombers:
            scaled_image, scaled_rect = self.scaleImageAndRect(bomber.sprite.image, bomber.rect)
            self.screen.blit(scaled_image, scaled_rect)

    def drawBombs(self, bombs):
        for bomb in bombs:
            scaled_image, scaled_rect = self.scaleImageAndRect(bomb.sprite.image, bomb.rect)
            self.screen.blit(scaled_image, scaled_rect)

    def drawFires(self, fires):
        for fire in fires:
            scaled_image, scaled_rect = self.scaleImageAndRect(fire.sprite.image, fire.rect)
            self.screen.blit(scaled_image, scaled_rect)

    def drawPowerUps(self, powerups):
        for powerup in powerups:
            scaled_image, scaled_rect = self.scaleImageAndRect(powerup.sprite.image, powerup.rect)
            self.screen.blit(scaled_image, scaled_rect)

    def setGameToRender(self, game):
        self.game = game
        self.calculateScaleFactor()

    def calculateScaleFactor(self):
        self.scale_factor = self.screen.get_width() / (64 * self.game.map.size)
