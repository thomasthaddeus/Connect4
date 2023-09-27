""" game_over_widget.py

The GameOverWidget is a PyQt6 widget that displays the result of a game.

It provides options for the user to either play the game again or return to the
main menu. The widget is designed to be flexible, allowing for the display of a
winner or indicating a draw.
"""

import sys
from PyQt6.QtWidgets import (
    QLabel,
    QWidget,
    QComboBox,
    QLineEdit,
    QPushButton,
    QGridLayout,
    QHBoxLayout,
    QListWidget,
    QMessageBox,
    QVBoxLayout,
    QApplication,
    QListWidgetItem,
    QMainWindow,
    QTextBrowser,
)
from PyQt6.QtGui import QColor


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


class ReturnToMainMenuWidget(QWidget):
    """return_to_main_menu_widget.py

    This widget provides a button that allows users to return to the main menu.
    When clicked, it opens the main menu window and closes the current window.

    # TODO: Add additional methods or logic as needed for the ReturnToMainMenuWidget.
    """

    def __init__(self, parent=None):
        """
        Initialize the ReturnToMainMenuWidget.

        Parameters:
        - parent: The parent widget (optional).
        """
        super().__init__(parent)

        # Set up the layout for the widget
        self.layout = QVBoxLayout(self)

        # Button to return to the main menu
        self.main_menu = MainMenuWindow()
        self.main_menu_button = QPushButton("Return to Main Menu")
        self.main_menu_button.clicked.connect(self.return_to_main)
        self.layout.addWidget(self.main_menu_button)

    def return_to_main(self):
        """
        Open the main menu window and close the current window.

        This method creates an instance of the MainMenuWindow, displays it,
        and then closes the current window (which is the game over window).
        """
        self.main_menu.show()
        self.close()


class PlayerSetupWindow(QWidget):
    def __init__(self):
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
        if text == "AI":
            self.p2_name_entry.setEnabled(False)
            self.p2_name_entry.clear()
        else:
            self.p2_name_entry.setEnabled(True)

    def start_game(self):
        # Logic to start the game
        pass


class NetworkSetupWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Network Setup")

        layout = QVBoxLayout(self)

        # Note: In a real-world scenario, you would use a library to get the local machine's IP.
        # Host Game
        self.host_ip_label = QLabel("Host IP: <Dynamically Set IP>")
        layout.addWidget(self.host_ip_label)
        self.host_port = QLineEdit(self)
        self.host_port.setPlaceholderText("Host Port (e.g., 8080)")
        layout.addWidget(self.host_port)

        # Join Game
        join_layout = QHBoxLayout()
        self.join_ip = QLineEdit(self)
        self.join_ip.setPlaceholderText("Enter IP")
        self.join_port = QLineEdit(self)
        self.join_port.setPlaceholderText("Enter Port")
        join_layout.addWidget(self.join_ip)
        join_layout.addWidget(self.join_port)
        layout.addLayout(join_layout)

        # Start/Connect Button
        start_connect_btn = QPushButton("Start/Connect")
        start_connect_btn.clicked.connect(self.start_or_connect)
        layout.addWidget(start_connect_btn)

    def start_or_connect(self):
        # Check if the user wants to host or join a game
        if self.host_port.text():
            # Logic to start a game as host
            # Here you'd set up your game server on the specified port
            QMessageBox.information(
                self, "Hosting Game", f"Started hosting on port {self.host_port.text()}"
            )

        elif self.join_ip.text() and self.join_port.text():
            # Logic to join a game
            # Here you'd attempt to connect to the provided IP and port
            QMessageBox.information(
                self,
                "Joining Game",
                "Attempting to connect to"
                f"{self.join_ip.text()}:{self.join_port.text()}",
            )

        else:
            QMessageBox.warning(
                self, "Error", "Please provide valid hosting or joining details."
            )


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


class GameWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialize the QTextBrowser
        self.text_browser = QTextBrowser(self)
        # Set up the layout and central widget
        layout = QVBoxLayout()
        layout.addWidget(self.text_browser)

        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Sample data
        self.display_game_stats(
            True
        )  # True means the user won, False means the user lost
        self.setWindowTitle("Connect 4 Game")

        layout = QVBoxLayout(self)

        # Display Board
        board_layout = QGridLayout()
        self.board_buttons = [[QPushButton() for _ in range(7)] for _ in range(6)]
        for i in range(6):
            for j in range(7):
                self.board_buttons[i][j].setFixedSize(50, 50)
                self.board_buttons[i][j].clicked.connect(
                    lambda i=i, j=j: self.drop_piece(i, j)
                )
                board_layout.addWidget(self.board_buttons[i][j], i, j)
        layout.addLayout(board_layout)

        # Whose Turn
        self.turn_label = QLabel("Turn: Player 1")
        layout.addWidget(self.turn_label)

        # End Game and Save Game Option
        end_game_btn = QPushButton("End Game")
        end_game_btn.clicked.connect(self.end_game)
        layout.addWidget(end_game_btn)

        # Score Display
        self.score_label = QLabel("Score - Player 1: 0 | Player 2: 0")
        layout.addWidget(self.score_label)

    def drop_piece(self, row, col):
        # Logic to handle dropping a piece onto the board
        pass

    def end_game(self):
        # Logic to handle ending the game
        # Proceed to game over window
        # This should be called when the user clicks the "End Game" button
        # This should also be called when the game is over (i.e. someone wins or the board is full)
        pass

    def display_game_stats(self, user_won: bool):
        # Update the QTextBrowser with game stats
        if user_won:
            self.text_browser.setHtml(
                "<h1>You Won!</h1><p>Congratulations on your victory!</p>"
            )
            self.change_window_color(QColor(0, 255, 0))  # Green color for victory
        else:
            self.text_browser.setHtml("<h1>You Lost!</h1><p>Better luck next time.</p>")
            self.change_window_color(QColor(255, 0, 0))  # Red color for defeat

    def change_window_color(self, color: QColor):
        # Change the window color
        self.setStyleSheet(f"background-color: {color.name()}")


class GameHistoryWindow(QWidget):
    def __init__(self, games):
        super().__init__()
        self.setWindowTitle("Game History")
        self.games = games

        layout = QVBoxLayout(self)

        # List of Past Games
        self.games_list = QListWidget(self)
        for game in games:
            # Assuming each game has a unique 'id' and 'name'
            item = QListWidgetItem(game["name"])
            item.setData(256, game["id"])  # 256 (Qt.UserRole) is arbitrary
            self.games_list.addItem(item)
        layout.addWidget(self.games_list)

        # Option to view details of each game
        view_details_btn = QPushButton("View Details")
        view_details_btn.clicked.connect(self.view_details)
        layout.addWidget(view_details_btn)
        # Return to Main Menu Widget
        self.return_widget = ReturnToMainMenuWidget(self)
        layout.addWidget(self.return_widget)

        # Return to main menu button
        main_menu_btn = QPushButton("Return to Main Menu")
        main_menu_btn.clicked.connect(self.return_widget.return_to_main)
        layout.addWidget(main_menu_btn)


    def view_details(self):
        # Logic to view game details
        selected_items = self.games_list.selectedItems()
        if selected_items:
            selected_game_id = selected_items[0].data(256)
            # Find the selected game from self.games and show its details
            # For instance, you might show a new window or a dialog here
            pass

    def main_menu(self):
        # Logic to return to the main menu or close this window
        self.return_widget.return_to_main()
        self.close()

class GameStatisticsWindow(QWidget):
    def __init__(self, stats, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Game Statistics")

        layout = QVBoxLayout(self)

        # Overall win/loss/draw statistics
        overall_label = QLabel(
            f"Wins: {stats['wins']}, Losses: {stats['losses']}, Draws: {stats['draws']}"
        )
        layout.addWidget(overall_label)

        # Individual player statistics (assuming stats holds data for two players)
        player1_label = QLabel(
            f"Player 1 - Wins:   {stats['player1']['wins']},"
            f"           Losses: {stats['player1']['losses']}"
        )
        layout.addWidget(player1_label)

        player2_label = QLabel(
            f"Player 2 - Wins:   {stats['player2']['wins']},"
            f"           Losses: {stats['player2']['losses']}"
        )
        layout.addWidget(player2_label)

        # Return to Main Menu Button
        main_menu_button = QPushButton("Return to Main Menu")
        main_menu_button.clicked.connect(self.main_menu)
        layout.addWidget(main_menu_button)

    def main_menu(self):
        # Logic to return to the main menu or close this window
        pass


class GameOverWindow(QWidget):
    def __init__(self, winner, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Game Over")

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

    def play_again(self):
        # Logic to reset the game or signal main window to start a new game
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # For Game History Window with sample data
    sample_games = [
        {"id": 1, "name": "Game 1", "moves": [], "winner": "Player 1"},
        {"id": 2, "name": "Game 2", "moves": [], "winner": "Player 2"},
    ]

    # For Player Setup Window
    window1 = PlayerSetupWindow()
    window2 = GameHistoryWindow(sample_games)
    window3 = GameWindow()  # For Game Window
    window4 = MainMenuWindow()
    window5 = NetworkSetupWindow()  # Test this window directly if needed
    window6 = ReturnToMainMenuWidget()
    window7 = NetworkSetupWindow()  # For Network Setup Window

    window1.show()
    window2.show()
    window3.show()
    window4.show()
    window5.show()
    window6.show()
    window7.show()
    app.exec()

    sys.exit(app.exec())
