"""player.py

Defines the Player class for a Connect 4 game.

This module contains the Player class, which represents a player in a Connect 4
game. It includes attributes and methods for managing player details, such as
name, player number, AI status, score, and making moves. The class supports
both human and AI players.
"""

import random

class Player:
    """
    Represents a player in the Connect 4 game.

    This class encapsulates the details and actions of a player, including the
    ability to make moves, track scores, and determine if the player is an AI
    or a human.

    Attributes:
        name (str): The name of the player.
        number (int): An identifier for the player, often used to distinguish
          players in the game.
        is_ai (bool): Indicates whether the player is controlled by AI. Default
          is False for human players.
        score (int): The player's current score in the game.
    """

    def __init__(self, name, number, is_ai=False):
        """
        Initializes a new Player instance.

        Args:
            name (str): The name of the player.
            number (int): An identifier for the player.
            is_ai (bool, optional): Indicates if the player is an AI. Defaults
              to False.
        """
        self.name = name
        self.number = number  # Player's identifier (e.g., 1 for red, 2 for yellow)
        self.is_ai = is_ai  # Flag for AI player
        self.score = 0  # Tracks the player's score

    def get_name(self):
        """
        Returns the player's name.

        Returns:
            str: The name of the player.
        """
        return self.name

    def get_id(self):
        """
        Returns the player's identifier.

        Returns:
            int: The identifier of the player.
        """
        return self.number

    def is_ai_player(self):
        """
        Determines if the player is an AI.

        Returns:
            bool: True if the player is an AI, False otherwise.
        """
        return self.is_ai

    def increment_score(self):
        """
        Increments the player's score by 1.
        """
        self.score += 1

    def get_score(self):
        """
        Retrieves the player's current score.

        Returns:
            int: The current score of the player.
        """
        return self.score

    def reset_score(self):
        """
        Resets the player's score to 0.
        """
        self.score = 0

    def make_move(self, board):
        """
        If the player is an AI, calculates and makes a move on the given board.

        Args:
            board (list): The current state of the game board.

        Returns:
            int: The column index where the AI decides to make a move. None if
            no move is made.
        """
        if self.is_ai:
            # Basic AI logic: make a random move
            available_moves = [i for i, cell in enumerate(board) if cell is None]
            if available_moves:
                return random.choice(available_moves)
            # Note: In a real-world scenario, you'd want a more sophisticated AI algorithm.

    def __str__(self):
        """
        Returns a string representation of the player.

        Returns:
            str: A string describing the player.
        """
        return f"Player {self.name} (ID: {self.number})"

    def __repr__(self):
        """
        Returns a formal string representation of the Player object.

        Returns:
            str: A formal representation of the Player object.
        """
        return f"Player(name={self.name}, number={self.number}, is_ai={self.is_ai})"
