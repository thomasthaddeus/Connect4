import pytest
from datetime import datetime
from game_history import GameHistory
import os

def test_add_game():
    gh = GameHistory()
    gh.add_game(datetime.now(), datetime.now(), "Player 1", ["Move 1", "Move 2"])
    assert gh.get_game_count() == 1

def test_filter_games_by_winner():
    gh = GameHistory()
    gh.add_game(datetime.now(), datetime.now(), "Player 1", ["Move 1", "Move 2"])
    gh.add_game(datetime.now(), datetime.now(), "Player 2", ["Move 3", "Move 4"])
    filtered_games = gh.filter_games_by_winner("Player 1")
    assert len(filtered_games) == 1
    assert filtered_games[0]['winner'] == "Player 1"

def test_save_and_load_from_file():
    gh = GameHistory()
    gh.add_game(datetime.now(), datetime.now(), "Player 1", ["Move 1", "Move 2"])
    filename = "test_game_history.json"
    gh.save_to_file(filename)

    # Ensure the file exists
    assert os.path.exists(filename)

    gh2 = GameHistory()
    gh2.load_from_file(filename)
    assert gh2.get_game_count() == 1
    assert gh2.get_games()[0]['winner'] == "Player 1"

    # Cleanup the test file
    os.remove(filename)

def test_clear_history():
    gh = GameHistory()
    gh.add_game(datetime.now(), datetime.now(), "Player 1", ["Move 1", "Move 2"])
    assert gh.get_game_count() == 1
    gh.clear_history()
    assert gh.get_game_count() == 0
