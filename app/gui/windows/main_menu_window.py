"""main_menu_window.py
_summary_

_extended_summary_
"""


import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from .game_history_window import GameHistoryWindow
from .game_statistics_window import GameStatisticsWindow
from .network_setup_window import NetworkSetupWindow
from .player_setup_window import PlayerSetupWindow



class MainMenuWindow(QWidget):
    def __init__(self):
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
        self.player_setup_window = PlayerSetupWindow()
        self.player_setup_window.show()

    def multiplayer(self):
        self.network_setup_window = NetworkSetupWindow()
        self.network_setup_window.show()

    def view_game_stats(self):
        # For simplicity, I'm assuming empty data.
        # Replace with your actual data.
        self.game_statistics_window = GameStatisticsWindow([])
        self.game_statistics_window.show()

    def view_game_history(self):
        # For simplicity, I'm assuming empty data.
        # Replace with your actual data.
        self.game_history_window = GameHistoryWindow([])
        self.game_history_window.show()

if __name__ == '__main__':
    app = QApplication([])
    window = MainMenuWindow()
    window.show()
    app.exec()
