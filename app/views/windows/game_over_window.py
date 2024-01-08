"""game_over_window.py

A PyQt6 window for displaying the outcome of a Connect 4 game.

The GameOverWindow class creates a graphical user interface to display the
result of a game and offers options for replaying or exiting to the main menu.
The window displays a message indicating whether a player has won or if the
game ended in a draw. This class is an essential part of the user experience in
the game, providing closure to each game session and guiding the player to
their next action.
"""

from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import pyqtSignal

class GameOverWindow(QDialog):
    """
    A window that displays the result of a Connect 4 game and offers post-game
    options.

    This class extends QWidget and provides a user interface for showing the
    game's outcome. It includes options for replaying the game or returning to
    the main menu, allowing players to easily continue interacting with the
    application.

    Args:
        QWidget (QWidget): Inherits from QWidget, a base class for all UI
        objects in PyQt.
    """
    play_again_signal = pyqtSignal()

    def __init__(self, winner, parent=None):
        """
        Initializes the GameOverWindow with the game's result.

        Args:
            winner (str or None): The name of the winning player or None if
              it's a draw.
            parent (QWidget, optional): The parent widget of this window.
        """
        super().__init__(parent)
        self.setWindowTitle("Game Over")
        self.setModal(True)  # Set the window as modal

        layout = QVBoxLayout(self)

        # Display the game result
        result_label = QLabel(f"{winner} won!" if winner else "It's a draw!")
        layout.addWidget(result_label)

        # Play Again Button
        play_again_button = QPushButton("Play Again")
        play_again_button.clicked.connect(self.play_again)
        layout.addWidget(play_again_button)

        # Return to Main Menu Button
        main_menu_button = QPushButton("Return to Main Menu")
        main_menu_button.clicked.connect(self.main_menu)
        layout.addWidget(main_menu_button)

    def play_again(self):
        """
        Triggers the action to start a new game.
        """
        # Logic for playing again
        self.accept()  # Closes the dialog and returns QDialog.Accepted

    def main_menu(self):
        # Logic for returning to the main menu
        self.reject()  # Closes the dialog and returns QDialog.Rejected
