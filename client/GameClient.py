import socket
import pickle
from threading import Thread

class GameClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.lastMessage = []

    def connect(self):
        self.client_socket.connect((self.host, self.port))
        print(f"Connected to server at {self.host}:{self.port}")

        receive_thread = Thread(target=self.receive_messages)
        receive_thread.start()

    def receive_messages(self):
        while True:
            try:
                data = self.client_socket.recv(1024)
                if not data:
                    break

                message = pickle.loads(data)
                print(f"Received message: {message}")
                self.lastMessage.append(message)
            except Exception as e:
                print(f"Error: {e}")
                break

    def send_message(self, message):
        try:
            self.client_socket.sendall(pickle.dumps(message))
        except Exception as e:
            print(f"Error: {e}")

# Example usage:
if __name__ == "__main__":
    client = GameClient("localhost", 8888)
    client.connect()

    while True:
        message = input("Enter message: ")
        client.send_message(message)