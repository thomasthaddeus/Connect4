"""save_load.py
_summary_

_extended_summary_

Returns:
    _type_: _description_
"""

import os
import pickle

class SaveLoad:
    def __init__(self):
        pass

    def save_game(self, game_state, filename):
        """Saves the game state to the specified file."""
        try:
            with open(filename, 'wb') as file:
                pickle.dump(game_state, file)
            print(f"Game saved to {filename}")
        except IOError as err:
            print(f"IO Error saving game: {err}")
        except pickle.PicklingError:
            print("Error pickling the game state.")

    def load_game(self, filename):
        """Loads the game state from the specified file."""
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
        """Checks if a save file exists."""
        return os.path.exists(filename)

    def list_saves(self, directory='.'):
        """Lists all saved game files in the specified directory."""
        return [file for file in os.listdir(directory) if file.endswith('.pkl')]

    def delete_save(self, filename):
        """Deletes the specified save file."""
        if self.save_exists(filename):
            try:
                os.remove(filename)
                print(f"Deleted save file: {filename}")
            except OSError as err:
                print(f"Error deleting save file: {err}")
        else:
            print(f"Save file {filename} does not exist.")
