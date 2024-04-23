import socket
import pickle

from server.ClientConnectionThread import ClientConnectionThread
from server.LobbyManager import LobbyManager


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.lobby_manager = LobbyManager()
        self.clients = []

    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()
        print(f"Server is listening on {self.host}:{self.port}")

        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"Connection from {client_address}")
            client_thread = ClientConnectionThread(client_socket, client_address, self)
            client_thread.start()
            self.clients.append(client_thread)

    def handleClientMessage(self, client_thread, message):
        print(message)
        if message.startswith("HOST_LOBBY"):
            self.lobby_manager.createLobby(client_thread)

        if message.startswith("JOIN_LOBBY"):
            lobby_id = int(message.split(":")[1])
            self.lobby_manager.joinLobby(lobby_id, client_thread)

        if message.startswith("LIST_LOBBY"):
            lobbies = self.lobby_manager.getLobbies()
            client_thread.sendData({"LOBBIES": lobbies})



    def broadcast_data(self, data):
        for client in self.clients:
            client.sendData(data)

if __name__ == "__main__":
    server = Server("localhost", 8888)
    server.start()