""" game_over_widget.py

The GameOverWidget is a PyQt6 widget that displays the result of a game.

This widget is part of a Connect 4 game application. It displays the game
result, either announcing the winner or indicating a draw. It also provides
buttons for the user to play again or return to the main menu. The widget can
be used at the end of a game to offer these post-game choices to the user.
"""

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from widgets import ReturnToMainMenuWidget


class GameOverWidget(QWidget):
    """
    A widget to display the game result and offer post-game options.

    This widget shows who won the game or if it ended in a draw. It provides
    buttons for playing again or returning to the main menu.

    Args:
        QWidget (QWidget): Inherits from QWidget, a base class for all UI objects in PyQt.
    """

    def __init__(self, winner, parent=None):
        """
        Initializes the GameOverWidget with the game result.

        Args:
            winner (str or None): The name of the winner. If None, it indicates a draw.
            parent (QWidget, optional): The parent widget.
        """
        super().__init__(parent)

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

        # Incorporate ReturnToMainMenuWidget
        self.return_widget = ReturnToMainMenuWidget(self)
        layout.addWidget(self.return_widget)

    def play_again(self):
        """
        Signals to start a new game.

        This method should be connected to the game logic to reset the game state or emit a signal to the main window to start a new game.
        """
        self.parent().restart_game()

    def main_menu(self):
        """
        Handle the logic to return to the main menu.

        This method can be connected to the main window or game logic
        to switch the view back to the main menu or close the current game view.
        """
        self.parent().show_main_menu()

#TODO: Add additional methods or logic as needed for the GameOverWidget.
