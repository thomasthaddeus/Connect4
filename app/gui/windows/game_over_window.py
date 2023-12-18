"""game_over_window.py

"""

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton

class GameOverWindow(QWidget):
    """
    GameOverWindow _summary_

    _extended_summary_

    Args:
        QWidget (_type_): _description_
    """
    def __init__(self, winner, parent=None):
        """
        __init__ _summary_

        _extended_summary_

        Args:
            winner (_type_): _description_
            parent (_type_, optional): _description_. Defaults to None.
        """
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
        """
        play_again _summary_

        _extended_summary_
        """
        # Logic to reset the game or signal main window to start a new game
        pass

    def main_menu(self):
        """
        main_menu _summary_

        _extended_summary_
        """
        # Logic to return to the main menu or close this window
        pass
