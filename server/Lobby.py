class Lobby:
    def __init__(self, lobbyID, hostClient):
        self.lobbyID = lobbyID
        self.host = hostClient
        self.players = [hostClient]
        self.lobbyState = "WAITING"

    def addPlayer(self, player):
        self.broadcastData("INFO:PLAYER_JOINED")
        self.players.append(player)

    def removePlayer(self, player):
        self.broadcastData("INFO:PLAYER_LEFT")
        self.players.remove(player)

    def broadcastData(self, data):
        for player in self.players:
            player.sendData(data)

    def serialize(self):
        return {
            "lobbyID": self.lobbyID,
            "lobbyState": self.lobbyState,
            "players": len(self.players)
        }