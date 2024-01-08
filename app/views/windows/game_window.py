"""game_window.py

Defines the main game interface for a Connect 4 game using PyQt6.

This module contains the GameWindow class, which creates a graphical user
interface for the Connect 4 game. The window includes a grid layout
representing the game board, labels to display whose turn it is and the current
score, and a button to end the game. The class handles player interactions such
as dropping pieces onto the board and ending the game.
"""

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QGridLayout, QApplication
from widgets import GameOverWidget


class GameWindow(QWidget):
    """
    A window representing the Connect 4 game interface.

    This class extends QWidget and creates a user interface for playing Connect
    4. It includes a grid of buttons representing the game board, labels for
    turn and score, and an end game button.

    Args:
        QWidget (QWidget): Inherits from QWidget, a base class for all UI
        objects in PyQt.
    """

    def __init__(self):
        """
        Initializes the GameWindow with UI components for playing Connect 4.
        """
        super().__init__()
        self.setWindowTitle("Connect 4 Game")

        layout = QVBoxLayout(self)

        # Display Board
        board_layout = QGridLayout()
        self.board_buttons = [[QPushButton() for _ in range(7)] for _ in range(6)]
        for i in range(6):
            for j in range(7):
                self.board_buttons[i][j].setFixedSize(50, 50)
                self.board_buttons[i][j].clicked.connect(lambda i=i, j=j: self.drop_piece(i, j))
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
        """
        Handles the logic for dropping a piece onto the board.

        This method is triggered when a board button is clicked. It updates the game state based
        on the player's move and refreshes the board display.

        Args:
            row (int): The row index of the clicked button on the board.
            col (int): The column index of the clicked button on the board.
        """
        # Assuming a `Game` class instance manages the game state
        game_state = Game.get_instance()
        player = game_state.current_player
        move_success = game_state.make_move(player, col)

        if move_success:
            self.update_board_display()
            if game_state.check_winner():
                self.end_game(winner=player)
            else:
                game_state.switch_player()
                self.turn_label.setText(f"Turn: Player {game_state.current_player}")
        else:
            # Handle invalid move (e.g., column is full)
            pass

    def end_game(self, winner=None):
        """
        Handles the logic for ending the game.

        This method is triggered when the 'End Game' button is clicked or when the game is over.
        It terminates the current game session and displays the game over screen or returns to the
        main menu.

        Args:
            winner (str, optional): The winner of the game, if applicable. Defaults to None.
        """
        # Assuming `GameOverWidget` is a widget to display the game over screen
        if winner:
            message = f"Player {winner} wins!"
        else:
            message = "Game over!"

        game_over_widget = GameOverWidget(message)
        game_over_widget.show()
        self.close()  # Close the current game window

if __name__ == '__main__':
    app = QApplication([])

    # For Network Setup Window
    # window = NetworkSetupWindow()

    # For Game Window
    window = GameWindow()

    window.show()
    app.exec()
