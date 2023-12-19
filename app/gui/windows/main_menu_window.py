"""main_menu_window.py

Defines the main menu GUI for a Connect 4 game using PyQt6.

This module contains the MainMenuWindow class, which creates a graphical user
interface for the main menu of a Connect 4 game. The menu offers options to
play against AI, start a multiplayer game, view game statistics, view game
history, and exit the game. Each option is represented by a button that, when
clicked, opens the corresponding window or performs the associated action.
"""

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from windows.game_history_window import GameHistoryWindow
from windows.game_statistics_window import GameStatisticsWindow
from windows.network_setup_window import NetworkSetupWindow
from windows.player_setup_window import PlayerSetupWindow

class MainMenuWindow(QWidget):
    """
    A window representing the main menu of a Connect 4 game.

    This class extends QWidget and creates a user interface for the main menu
    of the game. It provides options to start different modes of the game, view
    statistics, view history, and exit the application.

    Args:
        QWidget (QWidget): Inherits from QWidget, a base class for all UI
        objects in PyQt.
    """

    def __init__(self):
        """
        Initializes the MainMenuWindow with UI components for the main menu.
        """
        super().__init__()
        self.setWindowTitle("Connect 4")

        layout = QVBoxLayout(self)

        # Title
        title_label = QLabel("Connect 4")
        layout.addWidget(title_label)

        # Play against AI Button
        ai_button = QPushButton("Play against AI")
        ai_button.clicked.connect(self.play_against_ai)
        layout.addWidget(ai_button)

        # Play Against AI
        ai_game_btn = QPushButton("Play Against AI")
        ai_game_btn.clicked.connect(self.play_against_ai)
        layout.addWidget(ai_game_btn)

        # Multiplayer Button
        multiplayer_button = QPushButton("Multiplayer (local or over network)")
        multiplayer_button.clicked.connect(self.multiplayer)
        layout.addWidget(multiplayer_button)

        # View Game Statistics
        game_stats_btn = QPushButton("View Game Statistics")
        game_stats_btn.clicked.connect(self.view_game_stats)
        layout.addWidget(game_stats_btn)

        # View Game History
        game_history_btn = QPushButton("View Game History")
        game_history_btn.clicked.connect(self.view_game_history)
        layout.addWidget(game_history_btn)

        # Exit Button
        exit_button = QPushButton("Exit")
        exit_button.clicked.connect(self.close)
        layout.addWidget(exit_button)

    def play_against_ai(self):
        """
        Opens the player setup window for a game against AI.

        This method is triggered when the 'Play against AI' button is clicked.
        It initializes and shows the PlayerSetupWindow for setting up a game
        against an AI opponent.
        """
        self.player_setup_window = PlayerSetupWindow()
        self.player_setup_window.show()

    def multiplayer(self):
        """
        Opens the network setup window for a multiplayer game.

        This method is triggered when the 'Multiplayer (local or over network)'
        button is clicked. It initializes and shows the NetworkSetupWindow for
        setting up a local or network multiplayer game.
        """
        self.network_setup_window = NetworkSetupWindow()
        self.network_setup_window.show()

    def view_game_stats(self):
        """
        Opens the game statistics window.

        This method is triggered when the 'View Game Statistics' button is
        clicked. It initializes and shows the GameStatisticsWindow for viewing
        game statistics.
        """
        # For simplicity, I'm assuming empty data.
        # Replace with your actual data.
        self.game_statistics_window = GameStatisticsWindow([])
        self.game_statistics_window.show()

    def view_game_history(self):
        """
        Opens the game history window.

        This method is triggered when the View Game History button is clicked.
        It initializes and shows the GameHistoryWindow for viewing the history
        of past games.
        """
        # For simplicity, I'm assuming empty data.
        # Replace with your actual data.
        self.game_history_window = GameHistoryWindow([])
        self.game_history_window.show()

if __name__ == '__main__':
    app = QApplication([])
    window = MainMenuWindow()
    window.show()
    app.exec()
