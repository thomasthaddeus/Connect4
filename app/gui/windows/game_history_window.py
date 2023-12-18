"""game_history_window.py
_summary_

_extended_summary_
"""

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QListWidget, QListWidgetItem, QApplication
from return_to_main_menu_widget import ReturnToMainMenuWidget

class GameHistoryWindow(QWidget):
    """
    GameHistoryWindow _summary_

    _extended_summary_

    Args:
        QWidget (_type_): _description_
    """
    def __init__(self, games):
        """
        __init__ _summary_

        _extended_summary_

        Args:
            games (_type_): _description_
        """
        super().__init__()
        self.setWindowTitle("Game History")
        self.games = games

        layout = QVBoxLayout(self)

        # List of Past Games
        self.games_list = QListWidget(self)
        for game in games:
            # Assuming each game has a unique 'id' and 'name'
            item = QListWidgetItem(game['name'])
            item.setData(256, game['id'])  # 256 (Qt.UserRole) is arbitrary
            self.games_list.addItem(item)
        layout.addWidget(self.games_list)

        # Option to view details of each game
        view_details_btn = QPushButton("View Details")
        view_details_btn.clicked.connect(self.view_details)
        layout.addWidget(view_details_btn)

        # Return to main menu button
        main_menu_btn = QPushButton("Return to Main Menu")
        main_menu_btn.clicked.connect(self.return_to_main)
        layout.addWidget(main_menu_btn)

        # Return to Main Menu Widget
        self.return_widget = ReturnToMainMenuWidget(self)
        layout.addWidget(self.return_widget)


    def view_details(self):
        """
        view_details _summary_

        _extended_summary_
        """
        # Logic to view game details
        selected_items = self.games_list.selectedItems()
        if selected_items:
            selected_game_id = selected_items[0].data(256)
            # Find the selected game from self.games and show its details
            # For instance, you might show a new window or a dialog here
            pass

if __name__ == '__main__':
    app = QApplication([])

    # For Player Setup Window
    # window = PlayerSetupWindow()

    # For Game History Window with sample data
    sample_games = [
        {'id': 1, 'name': 'Game 1', 'moves': [], 'winner': 'Player 1'},
        {'id': 2, 'name': 'Game 2', 'moves': [], 'winner': 'Player 2'},
    ]
    window = GameHistoryWindow(sample_games)

    window.show()
    app.exec()
