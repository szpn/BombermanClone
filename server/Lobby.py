from threading import Thread
from server.GameHandlerThread import GameHandlerThread

class Lobby:
    def __init__(self, lobbyID, hostClient):
        self.lobbyID = lobbyID
        self.host = hostClient
        self.players = []
        self.lobbyState = "WAITING"
        self.gameHandlerThread = None


    def startGame(self):
        self.lobbyState = "IN_GAME"
        self.gameHandlerThread = GameHandlerThread(self)
        self.gameHandlerThread.start()


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
        print(f"[LOBBY {self.lobbyID}] {message}")

        if client_thread == self.host:
            self.handleHostMessage(message)

    def handleHostMessage(self, message):
        if message == "START_GAME":
            self.startGame()

    def serialize(self):
        return {
            "lobbyID": self.lobbyID,
            "lobbyState": self.lobbyState,
            "players": len(self.players)
        }