"""save_load.py

Provides functionality to save and load game states for a Connect 4 game.

This module contains the SaveLoad class, which handles the saving and loading
of game states to and from files. It uses Python's pickle module for
serialization and deserialization. Additional functionalities include checking
for existing saves, listing all saves in a directory, and deleting save files.
"""

import os
import pickle

class SaveLoad:
    """
    Manages saving and loading of game states for a Connect 4 game.

    This class provides methods to save the current game state to a file, load
    a game state from a file, list all saved games in a directory, check for
    the existence of a save file, and delete save files.

    Methods:
        save_game: Saves the current game state to a file.
        load_game: Loads a game state from a file.
        save_exists: Checks if a save file exists.
        list_saves: Lists all save files in a directory.
        delete_save: Deletes a specified save file.
    """

    def __init__(self):
        """
        Initializes the SaveLoad instance.
        """
        pass

    def save_game(self, game_state, filename):
        """
        Saves the given game state to the specified file using pickle serialization.

        Args:
            game_state (object): The game state to be saved.
            filename (str): The filename or path where the game state will be saved.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(game_state, file)
            print(f"Game saved to {filename}")
        except IOError as err:
            print(f"IO Error saving game: {err}")
        except pickle.PicklingError:
            print("Error pickling the game state.")

    def load_game(self, filename):
        """
        Loads the game state from the specified file using pickle
        deserialization.

        Args:
            filename (str): The filename or path from which the game state will
            be loaded.

        Returns:
            object: The loaded game state, or None if loading fails.
        """
        if not self.save_exists(filename):
            print(f"Error: Save file {filename} does not exist.")
            return None

        try:
            with open(filename, 'rb') as file:
                game_state = pickle.load(file)
            return game_state
        except IOError as err:
            print(f"IO Error loading game: {err}")
            return None
        except pickle.UnpicklingError:
            print("Error unpickling the game state.")
            return None

    def save_exists(self, filename):
        """
        Checks if the specified save file exists.

        Args:
            filename (str): The filename or path to check.

        Returns:
            bool: True if the save file exists, False otherwise.
        """
        return os.path.exists(filename)

    def list_saves(self, directory='.'):
        """
        Lists all save files (with .pkl extension) in the specified directory.

        Args:
            directory (str, optional): The directory to search for save files.
            Defaults to the current directory.

        Returns:
            list: A list of filenames of the save files in the specified
            directory.
        """
        return [file for file in os.listdir(directory) if file.endswith('.pkl')]

    def delete_save(self, filename):
        """
        Deletes the specified save file.

        Args:
            filename (str): The filename or path of the save file to delete.
        """
        if self.save_exists(filename):
            try:
                os.remove(filename)
                print(f"Deleted save file: {filename}")
            except OSError as err:
                print(f"Error deleting save file: {err}")
        else:
            print(f"Save file {filename} does not exist.")
