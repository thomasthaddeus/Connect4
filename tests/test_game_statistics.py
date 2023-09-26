import pytest
from game_statistics import GameStatistics
import os

def test_initial_values():
    stats = GameStatistics()
    assert stats.get_total_games() == 0
    assert stats.get_average_moves() == 0
    assert stats.get_player_wins() == {}

def test_game_played():
    stats = GameStatistics()
    stats.game_played("Alice", ["move1", "move2", "move3"])
    assert stats.get_total_games() == 1
    assert stats.get_average_moves() == 3
    assert stats.get_player_wins() == {"Alice": 1}

def test_multiple_games():
    stats = GameStatistics()
    stats.game_played("Alice", ["move1", "move2", "move3"])
    stats.game_played("Bob", ["move1", "move2"])
    stats.game_played(None, ["move1"])
    assert stats.get_total_games() == 3
    assert stats.get_average_moves() == 2
    assert stats.get_player_wins() == {"Alice": 1, "Bob": 1}

def test_save_load():
    stats1 = GameStatistics()
    stats1.game_played("Alice", ["move1", "move2", "move3"])
    stats1.game_played("Bob", ["move1", "move2"])
    filename = "test_stats.json"
    stats1.save_to_file(filename)

    stats2 = GameStatistics()
    stats2.load_from_file(filename)

    assert stats2.get_total_games() == stats1.get_total_games()
    assert stats2.get_average_moves() == stats1.get_average_moves()
    assert stats2.get_player_wins() == stats1.get_player_wins()

    os.remove(filename)  # Clean up the saved file after test
