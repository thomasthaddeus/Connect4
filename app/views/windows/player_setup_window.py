"""player_setup_window.py

Defines a GUI window for setting up players in a Connect 4 game using PyQt6.

This module contains the PlayerSetupWindow class, which creates a graphical
user interface for users to enter names for Player 1 and Player 2 or choose to
play against an AI. The class allows for dynamic switching between entering a
name for Player 2 or selecting an AI opponent. It also includes a button to
start the game once the players are set up.
"""

from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QComboBox,
)
from widgets import return_to_main_menu_widget


class PlayerSetupWindow(QWidget):
    """
    A window for setting up players in a Connect 4 game.

    This class extends QWidget and creates a user interface with input fields
    for player names and an option to select an AI opponent. It also includes a
    'Start Game' button.

    Args:
        QWidget (QWidget): Inherits from QWidget, a base class for all UI objects in PyQt.
    """

    def __init__(self):
        """
        Initializes the PlayerSetupWindow with UI components for player setup.
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
        Toggles the input method for Player 2 between a QLineEdit and selecting
        AI.

        When 'AI' is selected, the QLineEdit for Player 2's name is disabled
        and cleared. Otherwise, it is enabled for name input.

        Args:
            text (str): The current text of the combo box, used to determine
            the toggle state.
        """
        if text == "AI":
            self.p2_name_entry.setEnabled(False)
            self.p2_name_entry.clear()
        else:
            self.p2_name_entry.setEnabled(True)

    def start_game(self):
        """
        Placeholder method for starting the game.

        This method should be implemented to initiate the game with the provided player details once the 'Start Game' button is clicked.
        """
        # Logic to start the game
        pass


if __name__ == '__main__':
    from PyQt6.QtWidgets import QApplication
    app = QApplication([])
    window = PlayerSetupWindow()
    window.show()
    app.exec()
