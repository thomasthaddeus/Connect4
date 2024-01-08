""" game_statistics_window.py
_summary_

_extended_summary_
"""

from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton

class GameStatisticsWindow(QDialog):
    """
    GameStatisticsWindow _summary_

    _extended_summary_

    Args:
        QWidget (_type_): _description_
    """
    def __init__(self, stats, parent=None):
        """
        __init__ _summary_

        _extended_summary_

        Args:
            stats (_type_): _description_
            parent (_type_, optional): _description_. Defaults to None.
        """
        super().__init__(parent)
        self.setWindowTitle("Game Statistics")

        layout = QVBoxLayout(self)

        # Overall win/loss/draw statistics
        overall_label = QLabel(f"Wins: {stats['wins']}, Losses: {stats['losses']}, Draws: {stats['draws']}")
        layout.addWidget(overall_label)

        # Individual player statistics (assuming stats holds data for two players)
        player1_label = QLabel(f"Player 1 - Wins: {stats['player1']['wins']}, Losses: {stats['player1']['losses']}")
        layout.addWidget(player1_label)

        player2_label = QLabel(f"Player 2 - Wins: {stats['player2']['wins']}, Losses: {stats['player2']['losses']}")
        layout.addWidget(player2_label)

        # Return to Main Menu Button
        main_menu_button = QPushButton("Return to Main Menu")
        main_menu_button.clicked.connect(self.main_menu)
        layout.addWidget(main_menu_button)


    def main_menu(self):
        # Logic for returning to the main menu
        self.reject()  # Closes the dialog and returns QDialog.Rejected
