"""network_setup_window.py
_summary_

_extended_summary_
"""

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, QMessageBox


class NetworkSetupWindow(QWidget):
    """
    NetworkSetupWindow _summary_

    _extended_summary_

    Args:
        QWidget (_type_): _description_
    """
    def __init__(self):
        """
        __init__ _summary_

        _extended_summary_
        """
        super().__init__()
        self.setWindowTitle("Network Setup")

        layout = QVBoxLayout(self)

        # Note: In a real-world scenario, you would use a library to get the local machine's IP.
        # Host Game
        self.host_ip_label = QLabel("Host IP: <Dynamically Set IP>")
        layout.addWidget(self.host_ip_label)
        self.host_port = QLineEdit(self)
        self.host_port.setPlaceholderText("Host Port (e.g., 8080)")
        layout.addWidget(self.host_port)

        # Join Game
        join_layout = QHBoxLayout()
        self.join_ip = QLineEdit(self)
        self.join_ip.setPlaceholderText("Enter IP")
        self.join_port = QLineEdit(self)
        self.join_port.setPlaceholderText("Enter Port")
        join_layout.addWidget(self.join_ip)
        join_layout.addWidget(self.join_port)
        layout.addLayout(join_layout)

        # Start/Connect Button
        start_connect_btn = QPushButton("Start/Connect")
        start_connect_btn.clicked.connect(self.start_or_connect)
        layout.addWidget(start_connect_btn)

    def start_or_connect(self):
        """
        start_or_connect _summary_

        _extended_summary_
        """
        # Check if the user wants to host or join a game
        if self.host_port.text():
            # Logic to start a game as host
            # Here you'd set up your game server on the specified port
            QMessageBox.information(
                self,
                "Hosting Game",
                f"Started hosting on port {self.host_port.text()}"
            )

        elif self.join_ip.text() and self.join_port.text():
            # Logic to join a game
            # Here you'd attempt to connect to the provided IP and port
            QMessageBox.information(
                self,
                "Joining Game",
                "Attempting to connect to"
                f"{self.join_ip.text()}:{self.join_port.text()}"
            )

        else:
            QMessageBox.warning(
                self,
                "Error",
                "Please provide valid hosting or joining details."
            )


# Test this window directly if needed
if __name__ == '__main__':
    from PyQt6.QtWidgets import QApplication
    app = QApplication([])
    window = NetworkSetupWindow()
    window.show()
    app.exec()
