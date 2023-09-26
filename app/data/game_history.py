""" game_history.py
_summary_

_extended_summary_

Returns:
    _type_: _description_
"""

import datetime
import json
import os

class GameHistory:
    def __init__(self):
        self.games = []

    def add_game(self, start_time, end_time, winner, moves):
        game = {
            'start_time': start_time.isoformat(),
            'end_time': end_time.isoformat(),
            'winner': winner,
            'moves': moves
        }
        self.games.append(game)

    def get_games(self):
        return self.games

    def get_game_count(self):
        """Returns the number of games stored."""
        return len(self.games)

    def filter_games_by_winner(self, winner_name):
        """Returns games won by the specified winner."""
        return [game for game in self.games if game['winner'] == winner_name]

    def save_to_file(self, filename):
        """
        saves the game history to the specified file.

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
        """Loads game history from the specified file."""
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
        """Clears all stored game history."""
        self.games = []

    def __str__(self):
        return f"Total games recorded: {self.get_game_count()}"

    def __repr__(self):
        return f"GameHistory(games={self.games})"
