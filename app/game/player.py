"""player.py
_summary_

_extended_summary_

Returns:
    _type_: _description_
"""

import random

class Player:
    def __init__(self, name, number, is_ai=False):
        self.name = name
        self.number = number  # This might be used to determine the color of the player's pieces (e.g., 1 for red, 2 for yellow)
        self.is_ai = is_ai  # Whether this player is an AI or a human
        self.score = 0  # Tracks the score or wins of the player in multiple rounds

    def get_name(self):
        return self.name

    def get_id(self):
        return self.number

    def is_ai_player(self):
        """Returns True if the player is an AI, else returns False."""
        return self.is_ai

    def increment_score(self):
        """Increments the player's score by 1."""
        self.score += 1

    def get_score(self):
        """Returns the player's score."""
        return self.score

    def reset_score(self):
        """Resets the player's score to 0."""
        self.score = 0

    def make_move(self, board):
        """
        If the player is AI, calculate and make a move on the given board.
        For human players, this method might be overridden by GUI interactions.
        """
        if self.is_ai:
            # Basic AI logic: make a random move
            available_moves = [i for i, cell in enumerate(board) if cell is None]
            if available_moves:
                return random.choice(available_moves)
            # Note: In a real-world scenario, you'd want a more sophisticated AI algorithm.


    def __str__(self):
        return f"Player {self.name} (ID: {self.number})"

    def __repr__(self):
        return f"Player(name={self.name}, number={self.number}, is_ai={self.is_ai})"
