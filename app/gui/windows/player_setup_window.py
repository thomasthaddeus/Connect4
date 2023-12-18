"""player_setup_window.py
_summary_

_extended_summary_
"""

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox

class PlayerSetupWindow(QWidget):
    """
    PlayerSetupWindow _summary_

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
        self.setWindowTitle("Player Setup")

        layout = QVBoxLayout(self)

        # Enter Player 1 Name
        p1_layout = QHBoxLayout()
        p1_label = QLabel("Player 1 name:")
        self.p1_name = QLineEdit(self)
        p1_layout.addWidget(p1_label)
        p1_layout.addWidget(self.p1_name)
        layout.addLayout(p1_layout)

        # Enter Player 2 Name or Select AI
        p2_layout = QHBoxLayout()
        p2_label = QLabel("Player 2 name or select AI:")
        self.p2_name_or_ai = QComboBox(self)
        self.p2_name_or_ai.addItems(["AI", "Player 2"])
        self.p2_name_entry = QLineEdit(self)
        p2_layout.addWidget(p2_label)
        p2_layout.addWidget(self.p2_name_or_ai)
        p2_layout.addWidget(self.p2_name_entry)
        layout.addLayout(p2_layout)

        # Logic to toggle between AI and Player 2 name entry
        self.p2_name_or_ai.currentTextChanged.connect(self.toggle_player2_input)
        self.toggle_player2_input(self.p2_name_or_ai.currentText())

        # Start Game Button
        start_game_btn = QPushButton("Start Game")
        start_game_btn.clicked.connect(self.start_game)
        layout.addWidget(start_game_btn)

    def toggle_player2_input(self, text):
        """
        toggle_player2_input _summary_

        _extended_summary_

        Args:
            text (_type_): _description_
        """
        if text == "AI":
            self.p2_name_entry.setEnabled(False)
            self.p2_name_entry.clear()
        else:
            self.p2_name_entry.setEnabled(True)

    def start_game(self):
        """
        start_game _summary_

        _extended_summary_
        """
        # Logic to start the game
        pass
