"""network.py

_summary_

_extended_summary_

Returns:
    _type_: _description_
"""


import socket
import threading
import json

class Network:
    """
    Manages network interactions for a Connect 4 game.

    This class encapsulates the functionality for setting up a server and client connections,
    handling data transfer, and managing client connections for a multiplayer Connect 4 game.

    Attributes:
        host (str): Host address for the server. Defaults to 'localhost'.
        port (int): Port number for the server. Defaults to 12345.
        clients (list): A list of connected client sockets.
    """

    def __init__(self, host='localhost', port=12345):
        """
        Initializes the Network class with server and client socket configurations.

        Args:
            host (str, optional): The host address to bind the server. Defaults to 'localhost'.
            port (int, optional): The port number to bind the server. Defaults to 12345.
        """
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
        self.clients = []

    def start_server(self):
        """
        Starts the server and begins listening for incoming connections.

        It binds the server to the specified host and port, and starts a new thread to accept
        connections. The server listens for up to 5 pending connections.
        """
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        threading.Thread(target=self.accept_connections).start()

    def connect_to_server(self):
        """
        Establishes a connection to the server from a client.

        This method is used by clients to connect to the server. It sets up the connection
        and maintains it for sending and receiving data.
        """
        self.socket.connect((self.host, self.port))
        self.conn = self.socket

    def send(self, data):
        """
        Sends data to the connected server or client.

        Args:
            data (dict): The data to be sent, which is serialized into JSON format.
        """
        message = json.dumps(data)
        self.conn.sendall(message.encode())

    def receive(self):
        """
        Receives data from the connected server or client.

        Returns:
            dict: The data received, deserialized from JSON format.
        """
        data = self.conn.recv(1024).decode()
        return json.loads(data)

    def close(self):
        """
        Closes all client connections and the server socket.

        This method is called to safely close all active connections and the server socket,
        typically when shutting down the server.
        """
        for client in self.clients:
            client.close()
        self.server_socket.close()

    def accept_connections(self):
        """
        Continuously accepts incoming client connections.

        This method runs in a separate thread and is responsible for accepting new client
        connections, adding them to the client list, and starting a new thread to handle
        each client.
        """
        while True:
            conn, addr = self.server_socket.accept()
            self.clients.append(conn)
            threading.Thread(target=self.handle_client, args=(conn,)).start()

    def handle_client(self, conn):
        """
        Handles the communication with a connected client.

        Args:
            conn (socket.socket): The socket object representing the client connection.

        This method is responsible for receiving data from a client, processing it (e.g., game logic),
        and sending responses back. It runs in a separate thread for each client.
        """
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
        """
        Processes the game logic based on received data.

        Args:
            data (dict): The data received from a client, typically
              representing a game move.

        This method should be implemented to integrate with the Connect4 and
        Board classes, processing the game logic and updating the game state
        accordingly.
        """
        pass

    def send_move(self, move):
        """
        Sends a move to the game.

        Args:
            move (dict): The move to be sent to the game.

        This method should be implemented to integrate with the Connect4 and
        Board classes, sending a move to the game logic for processing.
        """
        pass

    def get_game_state(self):
        """
        Retrieves the current state of the game.

        This method should be implemented to integrate with the Connect4 and
        Board classes, returning the current state of the game.
        """
        pass
