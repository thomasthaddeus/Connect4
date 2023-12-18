"""game_window.py
_summary_

_extended_summary_
"""
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QGridLayout, QApplication
from widgets.game_over_widget import GameOverWidget


class GameWindow(QWidget):
    """
    GameWindow _summary_

    _extended_summary_

    Args:
        QWidget (_type_): _description_
    """
    def __init__(self):
        """
        __init__ _summary_

        _extended_summary_
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
        drop_piece _summary_

        _extended_summary_

        Args:
            row (_type_): _description_
            col (_type_): _description_
        """
        # Logic to handle dropping a piece onto the board
        pass

    def end_game(self):
        """
        end_game _summary_

        _extended_summary_
        """
        # Logic to handle ending the game
        # Proceed to game over window
        # This should be called when the user clicks the "End Game" button
        # This should also be called when the game is over (i.e. someone wins or the board is full)

        pass

if __name__ == '__main__':
    app = QApplication([])

    # For Network Setup Window
    # window = NetworkSetupWindow()

    # For Game Window
    window = GameWindow()

    window.show()
    app.exec()
