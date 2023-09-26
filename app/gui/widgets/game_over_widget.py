""" game_over_widget.py
_summary_

_extended_summary_
"""

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from widgets.return_to_main_menu_widget import ReturnToMainMenuWidget


class GameOverWidget(QWidget):
    def __init__(self, winner, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)

        # Display the result
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
        main_menu_button = QPushButton("Return to Main Menu")
        main_menu_button.clicked.connect(self.main_menu)
        layout.addWidget(main_menu_button)

        # Logic to return to the main menu or close this window
        self.return_widget = ReturnToMainMenuWidget(self)
        layout.addWidget(self.return_widget)

    def play_again(self):
        # Logic to reset the game or signal main window to start a new game
        pass
