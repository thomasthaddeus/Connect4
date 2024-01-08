"""game_history_window.py

A PyQt6 window for displaying the history of games played in a Connect 4 application.

The GameHistoryWindow class provides a user interface to view a list of past
games. Each game in the list can be selected to view more detailed information.
The window includes functionality to view the details of a selected game and a
button to return to the main menu. It's designed to integrate with the game's
data structure, assuming each game has identifiable attributes like 'id' and
'name'.
"""

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QListWidget, QListWidgetItem, QApplication
from widgets import ReturnToMainMenuWidget
from game_statistics_window import GameStatisticsWindow


class GameHistoryWindow(QWidget):
    """
    A window to display the history of games played in the Connect 4
    application.

    This class extends QWidget and is responsible for showing a list of past
    games. It allows users to view more detailed information about each game.

    Args:
        QWidget (QWidget): Inherits from QWidget, a base class for all UI objects in PyQt.
    """
    def __init__(self, games):
        """
        Initializes the GameHistoryWindow with a list of past games.

        Args:
            games (list): A list of dictionaries, each representing a game's
            details.
        """
        super().__init__()
        self.setWindowTitle("Game History")
        self.return_widget = ReturnToMainMenuWidget(self)
        self.games_list = QListWidget(self)
        self.games = games
        self.game_statistics = GameStatisticsWindow(self)

        layout = QVBoxLayout(self)

        # List of Past Games
        for game in games:
            item = QListWidgetItem(game['name'])
            item.setData(256, game['id'])
            self.games_list.addItem(item)
        layout.addWidget(self.games_list)

        # View Details Button
        view_details_btn = QPushButton("View Details")
        view_details_btn.clicked.connect(self.view_details)
        layout.addWidget(view_details_btn)

        # Return to Main Menu Button
        main_menu_btn = QPushButton("Return to Main Menu")
        main_menu_btn.clicked.connect(self.return_to_main)
        layout.addWidget(main_menu_btn)

        # Return to Main Menu Widget
        layout.addWidget(self.return_widget)


    def view_details(self):
        """
        Handles the action to view details of the selected game.

        This method is triggered when the 'View Details' button is clicked. It
        retrieves the selected game's information and displays its details.
        """
        # Logic to view game details
        selected_items = self.games_list.selectedItems()
        if selected_items:
            selected_game_id = selected_items[0].data(256)
            # Find the selected game from self.games and show its details
            # For instance, you might show a new window or a dialog here
            self.game_statistics

    def return_to_main(self):
        """
        Handles the action to return to the main menu.

        This method is triggered when the 'Return to Main Menu' button is clicked.
        It should close the current window and return to the main menu.
        """
        self.return_widget
        self.close()

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
