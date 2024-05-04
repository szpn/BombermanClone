from threading import Thread
from GameHandlerThread import GameHandlerThread
from BombermanClone.model.Directions import Directions
class Lobby:
    def __init__(self, lobbyID, hostClient):
        self.lobbyID = lobbyID
        self.host = hostClient
        self.players = []
        self.lobbyState = "WAITING"
        self.gameHandlerThread = None
        self.gameTohandle = None


    def startGame(self):
        self.lobbyState = "IN_GAME"
        self.gameHandlerThread = GameHandlerThread(self)
        self.gameHandlerThread.start()
        self.gameTohandle = self.gameHandlerThread.game


    def addPlayer(self, player):
        self.broadcastData("INFO:PLAYER_JOINED")
        self.players.append(player)

        player.messageHandlingFunction = self.handleClientMessage

    def removePlayer(self, player):
        self.broadcastData("INFO:PLAYER_LEFT")
        self.players.remove(player)

    def broadcastData(self, data):
        for player in self.players:
            player.sendData(data)

    def handleClientMessage(self, client_thread, message):


        if self.lobbyState == "WAITING":
            print(f"[LOBBY {self.lobbyID}] {message}")
            if client_thread == self.host:
                self.handleHostMessage(message)
        #TODO Zmienic na hosta przy zabawie z gui

            self.handleStartTestMessage(message)
        elif self.lobbyState == "IN_GAME":

            actingPlayer = self.players.index(client_thread)
            print(f"[LOBBY {self.lobbyID}] {message} {actingPlayer}")
            self.handleClientGameMessages(message,actingPlayer)

    def handleHostMessage(self, message):
        if message == "START_GAME":
            self.startGame()


    #### Generalnie to prowizoryczny start bo Gui nie zrobione
    def handleStartTestMessage(self, message):
        if message == "START_GAME":
            self.startGame()

    ####

    def handleClientGameMessages(self, message,actingPlayer):
        if message == "LEFT":
            self.gameTohandle.moveBomber(self.gameTohandle.bombers[actingPlayer], Directions.LEFT)
        if message == "RIGHT":
            self.gameTohandle.moveBomber(self.gameTohandle.bombers[actingPlayer], Directions.RIGHT)
        elif message == "UP":
            self.gameTohandle.moveBomber(self.gameTohandle.bombers[actingPlayer], Directions.UP)
        if message == "DOWN":
            self.gameTohandle.moveBomber(self.gameTohandle.bombers[actingPlayer], Directions.DOWN)
        if message == "BOMB":
            self.gameTohandle.placeBomb(self.gameTohandle.bombers[actingPlayer])
    def serialize(self):
        return {
            "lobbyID": self.lobbyID,
            "lobbyState": self.lobbyState,
            "players": len(self.players)
        }