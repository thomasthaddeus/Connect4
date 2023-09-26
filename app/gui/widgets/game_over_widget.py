""" game_over_widget.py

The GameOverWidget is a PyQt6 widget that displays the result of a game.

It provides options for the user to either play the game again or return to the
main menu. The widget is designed to be flexible, allowing for the display of a
winner or indicating a draw.
"""

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from widgets.return_to_main_menu_widget import ReturnToMainMenuWidget


class GameOverWidget(QWidget):
    """
    GameOverWidget _summary_

    _extended_summary_

    Args:
        QWidget (_type_): _description_
    """
    def __init__(self, winner, parent=None):
        """
        Initialize the GameOverWidget.

        Parameters:
        - winner (str or None): The name of the winner. If None, it indicates a draw.
        - parent (QWidget, optional): The parent widget.
        """
        super().__init__(parent)

        # Set up the vertical layout for the widget
        layout = QVBoxLayout(self)

        # Display the result
        if winner:
            result_label = QLabel(f"{winner} won!")
        else:
            result_label = QLabel("It's a draw!")
        layout.addWidget(result_label)

        # Determine and display the game result based on the 'winner' parameter
        if winner:
            result_label = QLabel(f"{winner} won!")
        else:
            result_label = QLabel("It's a draw!")
        layout.addWidget(result_label)

        # Play Again Button
        play_again_button = QPushButton("Play Again")
        play_again_button.clicked.connect(self.play_again)
        layout.addWidget(play_again_button)

        # Return to Main Menu Button
        # Add a button that allows the user to return to the main menu
        main_menu_button = QPushButton("Return to Main Menu")
        main_menu_button.clicked.connect(self.main_menu)
        layout.addWidget(main_menu_button)

        # Logic to return to the main menu or close this window
        # Incorporate the ReturnToMainMenuWidget, which might contain
        # additional logic or UI elements related to returning to the main menu.
        self.return_widget = ReturnToMainMenuWidget(self)
        layout.addWidget(self.return_widget)


    def play_again(self):
        """
        Handle the logic to reset the game or signal the main window to start a
        new game.

        This method should be connected to the game logic to reset the game
        state or emit a signal to the main window to start a new game.
        """
        # TODO: Implement the logic to reset the game or signal the main window
        pass

    def main_menu(self):
        """
        Handle the logic to return to the main menu.

        This method can be connected to the main window or game logic
        to switch the view back to the main menu or close the current game view.
        """
        # TODO: Implement the logic to return to the main menu or close this widget
        pass

# TODO: Add additional methods or logic as needed for the GameOverWidget.
