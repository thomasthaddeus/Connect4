import pytest
from player import Player  # Assuming the Player class is in a file named player.py

def test_player_initialization():
    player = Player("Alice", 1)
    assert player.get_name() == "Alice"
    assert player.get_id() == 1
    assert not player.is_ai_player()

def test_ai_player():
    ai_player = Player("AI_Player", 2, is_ai=True)
    assert ai_player.is_ai_player()

def test_score_increment():
    player = Player("Bob", 2)
    player.increment_score()
    assert player.get_score() == 1

    player.increment_score()
    player.increment_score()
    assert player.get_score() == 3

def test_score_reset():
    player = Player("Charlie", 1)
    player.increment_score()
    player.increment_score()
    player.reset_score()
    assert player.get_score() == 0

def test_string_representation():
    player = Player("David", 2)
    assert str(player) == "Player David (ID: 2)"
    assert repr(player) == "Player(name=David, number=2, is_ai=False)"
