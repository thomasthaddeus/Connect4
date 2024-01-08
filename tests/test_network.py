import socket
import threading
from app.models.network import Network  # replace 'your_module' with the name of the module containing the Network class
import pytest

HOST, PORT = 'localhost', 12345

@pytest.fixture
def server():
    network = Network(host=HOST, port=PORT)
    threading.Thread(target=network.start_server, daemon=True).start()
    yield network
    network.close()

def test_server_starts_and_accepts_connections(server: Network):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    client_socket.close()

def test_send_and_receive(server: Network):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    test_message = "Hello, server!"
    client_socket.sendall(test_message.encode())

    received = client_socket.recv(1024).decode()
    assert received == test_message, f"Expected {test_message}, but got {received}"

    client_socket.close()
