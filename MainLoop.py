import pygame
from GameLoop import GameLoop
from MenuLoop import MenuLoop
from model.game.GameCreator import GameCreator

STATE_MENU = 0
STATE_GAME = 1
FPS = 60

class MainLoop:
    def __init__(self, screen):
        self.state = STATE_MENU
        self.screen = screen
        self.menuloop = MenuLoop(screen)
        self.menuloop.listenForMessages(self.handleMessage)
        self.gameloop = GameLoop(screen)
        self.isRunning = True


    def run(self):
        clock = pygame.time.Clock()
        while self.isRunning:
            time_delta = clock.tick(FPS)/1000.0
            if self.state == STATE_MENU:
                self.menuloop.tick()
                self.menuloop.manager.update(time_delta)

            if self.state == STATE_GAME:
                self.gameloop.tick()

            self.handleEvents()
            pygame.display.update()

        pygame.quit()

    #TODO :change the "ID" to be numbers not string
    def handleMessage(self, message):
        id = message["id"]
        if id == "HOST GAME":
            mapName = message["mapName"]
            game = GameCreator.createGameUsingMapFile(mapName, 1)
            self.startGame(game)




    def startGame(self, game):
        self.state = STATE_GAME
        self.gameloop.setGame(game)


    def handleEvents(self):
        for event in pygame.event.get():
            if self.state == STATE_MENU:
                self.menuloop.manager.process_events(event)
                self.menuloop.handleMenuEvents(event)

            if self.state == STATE_GAME:
                pass

            if event.type == pygame.QUIT:
                self.isRunning = False
