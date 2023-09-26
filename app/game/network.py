import socket
import threading
import json

class Network:
    def __init__(self, host='localhost', port=12345):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
        self.clients = []

    def start_server(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)  # allow up to 5 pending connections
        threading.Thread(target=self.accept_connections).start()

    def connect_to_server(self):
        self.socket.connect((self.host, self.port))
        self.conn = self.socket

    def send(self, data):
        message = json.dumps(data)
        self.conn.sendall(message.encode())

    def receive(self):
        data = self.conn.recv(1024).decode()
        return json.loads(data)

    def close(self):
        for client in self.clients:
            client.close()
        self.server_socket.close()

    def accept_connections(self):
        while True:
            conn, addr = self.server_socket.accept()
            self.clients.append(conn)
            threading.Thread(target=self.handle_client, args=(conn,)).start()

    def handle_client(self, conn):
        try:
            while True:
                data = conn.recv(1024).decode()
                if not data:
                    break
                print("Received data:", data)
                # Placeholder for game logic
                # game_state = self.process_game_logic(data)
                conn.sendall(data.encode())  # echo back for now
        except Exception as err:
            print(f"Error handling client: {err}")
        finally:
            conn.close()
            self.clients.remove(conn)

    # Placeholder methods for game interfacing
    def process_game_logic(self, data):
        # Process the game logic based on received data and return the game state
        # This is where you'd integrate with the Connect4 and Board classes
        pass

    def send_move(self, move):
        # Send a move to the game
        # This is where you'd integrate with the Connect4 and Board classes
        pass

    def get_game_state(self):
        # Get the current game state
        # This is where you'd integrate with the Connect4 and Board classes
        pass
