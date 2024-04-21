import socket
import pickle

from ClientConnectionThread import ClientConnectionThread
from ServerGameHandler import ServerGameHandler


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = []
        self.games = []


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


    def client_message(self, clientThread, message):
        print(message)
        if message["id"] == "HOST GAME":
            print(clientThread.client_address, "jestem hostem")
            newHandler = ServerGameHandler(message["mapName"],2)
            newHandler.players.append(clientThread)
            self.games.append([newHandler,clientThread])
        elif message["id"] == "JOIN GAME":
            print(clientThread.client_address, "joinuje")
            #narazie tylko dla 2 ma działać także no
            self.games[0].append([clientThread])
            self.games[0][0].players.append(clientThread)
            self.games[0][0].start_game()
        elif message == "Hi":
            clientThread.client_socket.send(pickle.dumps("Hi!"))

    def broadcast_data(self, data):
        for client in self.clients:
            client.send(data)




if __name__ == "__main__":
    server = Server("localhost", 8888)
    server.start()