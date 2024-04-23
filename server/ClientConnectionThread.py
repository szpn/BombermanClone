from threading import Thread
import pickle


class ClientConnectionThread(Thread):
    def __init__(self, client_socket, client_address, server):
        super().__init__()
        self.client_socket = client_socket
        self.client_address = client_address
        self.server = server

    def run(self):
        while True:
            try:
                self.recieveData()

            except Exception as e:
                print(f"Error: {e}")
                break

    def recieveData(self):
        data = self.client_socket.recv(1024)

        message = pickle.loads(data)
        self.server.handleClientMessage(self, message)

    def sendData(self, data):
        try:
            message = pickle.dumps(data)
            self.client_socket.sendall(message)
        except Exception as e:
            print(f"Error: {e}")