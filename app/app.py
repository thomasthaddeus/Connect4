# app.py

from PyQt6.QtWidgets import QApplication
from main_menu_window import MainMenuWindow
from game_window import GameWindow
from game_over_window import GameOverWindow
from game_statistics_window import GameStatisticsWindow
from game_history_window import GameHistoryWindow
from network_setup_window import NetworkSetupWindow
from player_setup_window import PlayerSetupWindow
from main import GameBackend
from game_statistics import GameStatistics
from save_load import SaveLoad
from game_history import GameHistory
from AI import AI
from board import Board, Connect4
from player import Player
from main import GameBackend

class App:
    def __init__(self):
        self.app = QApplication([])
        self.game_backend = GameBackend()

        # GUI Windows
        self.main_menu_window = MainMenuWindow()
        self.game_window = GameWindow()
        self.game_over_window = GameOverWindow(None)
        self.game_statistics_window = GameStatisticsWindow({})
        self.game_history_window = GameHistoryWindow([])
        self.network_setup_window = NetworkSetupWindow()
        self.player_setup_window = PlayerSetupWindow()

        # Connect signals/slots or events between GUI and backend
        # Example:
        # self.game_window.some_signal.connect(self.game_backend.some_method)

        # Data
        self.game_statistics = GameStatistics()
        self.save_load = SaveLoad()
        self.game_history = GameHistory()

        self.game_backend = GameBackend()
        self.database = Database()
        self.gui = GUI()

    def start(self):
        # Main loop to integrate the game, GUI, and database
        while not self.game_backend.board.is_full() and not self.game_backend.board.get_winner():
            current_player = self.game_backend.players[self.game_backend.board.current_player - 1]
            if current_player.is_ai_player():
                best_move = self.game_backend.ai.find_best_move(self.game_backend.board)
                self.game_backend.game.play_turn(best_move)
            else:
                move = self.gui.get_player_move()
                self.game_backend.game.play_turn(move)

            # Update the GUI with the current board state
            self.gui.update_board(self.game_backend.board)

            # Optionally save the game state to the database
            self.database.save_game_state(self.game_backend.board)

    def run(self):
        self.main_menu_window.show()
        self.app.exec()


    def start(self):
        # Start the main menu GUI
        # self.main_menu_window.show()

        # Connect GUI events to backend logic
        # For example:
        # self.game_window.move_made.connect(self.game_backend.make_move)
        # self.game_window.save_game.connect(self.save_load.save_game)
        # ...

        # Load game statistics and history
        self.game_statistics.load_from_file("statistics.json")
        self.game_history.load_from_file("history.json")

        # Main loop to integrate the game, GUI, and data
        # This will depend on your GUI framework
        # For example, in PyQt:
        # app = QApplication(sys.argv)
        # sys.exit(app.exec_())

class Database:
    def __init__(self):
        pass  # Initialize your database connection here

    def save_game_state(self, game_state):
        pass  # Logic to save game state to the database

    def load_game_state(self):
        pass  # Logic to load game state from the database

class GUI:
    def __init__(self):
        pass  # Initialize your GUI components here

    def update_board(self, board):
        pass  # Logic to update the board in the GUI

    def get_player_move(self):
        pass  # Logic to get the player's move from the GUI




if __name__ == "__main__":
    app_instance = App()
    app_instance.run()

if __name__ == "__main__":
    app = App()
    app.start()