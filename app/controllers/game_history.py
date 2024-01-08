"""game_history.py

Manages the history of games played in a Connect 4 application.

This module contains the GameHistory class, which is responsible for tracking,
storing, and retrieving the history of games played. It includes
functionalities to add game records, filter games, save and load game history
to and from files, and manage the game history data.
"""

import datetime
import json
import os

class GameHistory:
    """
    Represents and manages the history of games played.

    This class provides methods to add game records to the history, retrieve
    games, filter games based on winners, and handle the persistence of game
    history through saving to and loading from files.

    Attributes:
        games (list): A list of dictionaries, each representing a game's
        details.
    """

    def __init__(self):
        """
        Initializes the GameHistory instance, setting up an empty game history
        list.
        """
        self.games = []

    def __str__(self):
        """
        Returns a string representation of the GameHistory instance.

        Returns:
            str: A summary string indicating the total number of games recorded.
        """
        return f"Total games recorded: {self.get_game_count()}"

    def __repr__(self):
        """
        Returns a formal string representation of the GameHistory object.

        Returns:
            str: A formal representation of the GameHistory object.
        """
        return f"GameHistory(games={self.games})"

    def add_game(self, start_time, end_time, winner, moves):
        """
        Adds a record of a game to the game history.

        Args:
            start_time (datetime.datetime): The start time of the game.
            end_time (datetime.datetime): The end time of the game.
            winner (str): The name of the winning player.
            moves (list): A list of moves made during the game.
        """
        game = {
            'start_time': start_time.isoformat(),
            'end_time': end_time.isoformat(),
            'winner': winner,
            'moves': moves
        }
        self.games.append(game)

    def get_games(self):
        """
        Retrieves all recorded games from the game history.

        Returns:
            list: A list of dictionaries, each representing a game's details.
        """
        return self.games

    def get_game_count(self):
        """
        Returns the number of games stored in the history.

        Returns:
            int: The total number of games recorded.
        """
        return len(self.games)

    def filter_games_by_winner(self, winner_name):
        """
        Filters and returns games won by a specified player.

        Args:
            winner_name (str): The name of the winner to filter games by.

        Returns:
            list: A list of games won by the specified player.
        """
        return [game for game in self.games if game['winner'] == winner_name]

    def save_to_file(self, filename):
        """
        Saves the game history to the specified file.

        Args:
            filename (str): the name of the file to save to
        """
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(self.games, file)
        except FileNotFoundError:
            print(f"Error: File {filename} not found.")
        except IOError as err:
            print(f"IO Error saving to file: {err}")

    def load_from_file(self, filename):
        """
        Loads game history from a specified file.

        Args:
            filename (str): The filename or path to load the game history from.
        """
        if not os.path.exists(filename):
            print(f"Error: {filename} does not exist.")
            return

        try:
            with open(filename, 'r', encoding='utf-8') as file:
                self.games = json.load(file)
        except FileNotFoundError:
            print(f"Error: File {filename} not found.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from {filename}.")
        except IOError as err:
            print(f"IO Error loading from file: {err}")

    def clear_history(self):
        """
        Clears all stored game history, resetting the history to an empty state.
        """
        self.games = []
