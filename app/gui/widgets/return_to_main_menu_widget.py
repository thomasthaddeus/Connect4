""" return_to_main_menu_widget.py

This widget provides a button that allows users to return to the main menu.

The ReturnToMainMenuWidget is part of a PyQt6 application and offers a simple
interface for returning to the main menu. When clicked, it opens the
MainMenuWindow and closes the current window. This widget can be used in
different parts of the application where a return to the main menu
functionality is needed.

TODO: Add additional methods or logic as needed for the ReturnToMainMenuWidget.
"""

from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QApplication
from windows.main_menu_window import MainMenuWindow

class ReturnToMainMenuWidget(QWidget):
    """
    A widget providing a button to return to the main menu of the application.

    This widget contains a single button. When clicked, it opens the main menu
    window and closes the current window, facilitating easy navigation back to
    the main menu.

    Args:
        QWidget (QWidget): Inherits from QWidget, a base class for all UI objects in PyQt.
    """

    def __init__(self, parent=None):
        """
        Initializes the ReturnToMainMenuWidget.

        Args:
            parent (QWidget, optional): The parent widget of this widget.
        """
        super().__init__(parent)

        self.layout = QVBoxLayout(self)

        # Button to return to the main menu
        self.main_menu_button = QPushButton("Return to Main Menu")
        self.main_menu_button.clicked.connect(self.return_to_main)
        self.layout.addWidget(self.main_menu_button)

    def return_to_main(self):
        """
        Handles the action to return to the main menu.

        This method creates an instance of the MainMenuWindow, shows it, and
        closes the current window (which is typically a game over or game
        window).
        """
        self.main_menu = MainMenuWindow()
        self.main_menu.show()
        self.close()

# TODO: Test the ReturnToMainMenuWidget directly
# This allows for quick testing of this widget without needing to run the entire application.
if __name__ == '__main__':
    app = QApplication([])
    window = ReturnToMainMenuWidget()
    window.show()
    app.exec()
