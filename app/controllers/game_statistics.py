"""game_statistics.py

Manages and tracks statistics for games played in a Connect 4 application.

This module contains the GameStatistics class, which is responsible for
tracking various statistics of games played, such as total games, wins per
player, and total moves. It includes functionality to update statistics,
retrieve them, and save/load them from a file.
"""

import json

class GameStatistics:
    """
    Represents and manages game-related statistics.

    This class provides methods for tracking and retrieving game statistics
    like the total number of games played, individual player wins, and the
    average number of moves per game. It also includes functionality to save
    and load these statistics to and from a file.

    Attributes:
        total_games (int): The total number of games played.
        player_wins (dict): A dictionary mapping players to their win counts.
        total_moves (int): The total number of moves made in all games.
    """

    def __init__(self):
        """
        Initializes the GameStatistics instance, setting up the initial
        statistics.
        """
        self.total_games = 0
        self.player_wins = {}
        self.total_moves = 0

    def game_played(self, winner, moves):
        """
        Updates the statistics based on a completed game.

        Args:
            winner (str): The name of the winning player.
            moves (list): A list of moves made during the game.
        """
        self.total_games += 1
        self.total_moves += len(moves)
        if winner is not None:
            self.player_wins[winner] = self.player_wins.get(winner, 0) + 1

    def get_total_games(self):
        """
        Retrieves the total number of games played.

        Returns:
            int: The total number of games played.
        """
        return self.total_games

    def get_player_wins(self):
        """
        Retrieves the win count for each player.

        Returns:
            dict: A dictionary mapping players to their win counts.
        """
        return self.player_wins

    def get_average_moves(self):
        """
        Calculates the average number of moves per game.

        Returns:
            float: The average number of moves per game. Returns 0 if no games have been played.
        """
        if self.total_games == 0:
            return 0
        else:
            return self.total_moves / self.total_games

    def save_to_file(self, filename):
        """
        Saves the current game statistics to a file.

        Args:
            filename (str): The filename or path to save the statistics to.
        """
        data = {
            'total_games': self.total_games,
            'player_wins': self.player_wins,
            'total_moves': self.total_moves,
        }
        with open(filename, mode='w', encoding='utf-8') as f:
            json.dump(data, f)

    def load_from_file(self, filename):
        """
        Loads game statistics from a specified file.

        Args:
            filename (str): The filename or path to load the statistics from.
        """
        with open(filename, mode='r', encoding='utf-8') as f:
            data = json.load(f)
            self.total_games = data['total_games']
            self.player_wins = data['player_wins']
            self.total_moves = data['total_moves']
