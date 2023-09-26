""" return_to_main_menu_widget.py

This widget provides a button that allows users to return to the main menu.
When clicked, it opens the main menu window and closes the current window.

# TODO: Add additional methods or logic as needed for the ReturnToMainMenuWidget.
"""

from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QApplication
from main_menu_window import MainMenuWindow

class ReturnToMainMenuWidget(QWidget):
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
        self.main_menu_button = QPushButton("Return to Main Menu")
        self.main_menu_button.clicked.connect(self.return_to_main)
        self.layout.addWidget(self.main_menu_button)


    def return_to_main(self):
        """
        Open the main menu window and close the current window.

        This method creates an instance of the MainMenuWindow, displays it,
        and then closes the current window (which is the game over window).
        """
        self.main_menu = MainMenuWindow()
        self.main_menu.show()
        self.close()


# Test this widget directly if needed
# Test the ReturnToMainMenuWidget directly
# This allows for quick testing of this widget without needing to run the entire application.
if __name__ == '__main__':
    app = QApplication([])
    window = ReturnToMainMenuWidget()
    window.show()
    app.exec()
