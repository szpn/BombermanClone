import pygame
from GameLoop import GameLoop
from MenuLoop import MenuLoop
from client.SimpleClient import SimpleClient

STATE_MENU = 0
STATE_GAME = 1
STATE_END = 2
FPS = 60


class MainLoop:
    def __init__(self, screen):
        self.state = STATE_MENU
        self.screen = screen
        self.isRunning = True
        self.connection = SimpleClient("localhost", 8888)
        self.connection.listenForMessages(self.handleServerMessage)

        self.menuloop = MenuLoop(screen, self.connection)
        self.gameloop = GameLoop(screen, self.connection)
        self.menuloop.listenForMessages(self.handleUIMessage)

    def run(self):
        clock = pygame.time.Clock()

        self.connection.connect()

        while self.isRunning:

            time_delta = clock.tick(FPS) / 1000.0

            if self.state == STATE_MENU:
                self.menuloop.tick()
                self.menuloop.manager.update(time_delta)

            if self.state == STATE_GAME:
                self.gameloop.tick()

            self.handleEvents()
            pygame.display.update()

        pygame.quit()


    def handleServerMessage(self, message):
        print(message)
        if message["id"] == "BEFORE_LOBBY_STATE":
            self.menuloop.showLobbies(message["LOBBIES"])

        if message["id"] == "LOBBY_STATE":
            self.menuloop.setInLobby(message["data"])

        if message["id"] == "GAME_STARTED":

            self.state = STATE_GAME
            self.connection.listenForMessages(self.gameloop.handleServerMessage)



    def handleUIMessage(self, message):
        id = message["id"]
        if id == "HOST_LOBBY":
            self.connection.send_message(message)
        elif id == "SELECT_MAP":
            self.connection.send_message(message)
        elif id == "JOIN_LOBBY":
            self.connection.send_message(message)
        elif id == "LIST_LOBBY":
            self.connection.send_message(message)
        elif id == "START_GAME":
            self.connection.send_message(message)



    def handleEvents(self):
        for event in pygame.event.get():
            if self.state == STATE_MENU:
                self.menuloop.manager.process_events(event)
                self.menuloop.handleMenuEvents(event)

            if self.state == STATE_GAME:
                pass

            if event.type == pygame.QUIT:
                self.isRunning = False
