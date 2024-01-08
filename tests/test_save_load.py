import os
from pathlib import Path
from typing import Any
import pytest
from ..app.controllers.save_load import SaveLoad

# Setup for the tests
@pytest.fixture
def sl():
    return SaveLoad()

@pytest.fixture
def sample_game_state():
    return {"player1": "Alice", "player2": "Bob", "board": [[0]*7 for _ in range(6)]}

def test_save_load_game(
    sl: Any, sample_game_state: dict[str, Any], tmp_path: Path
):
    # Use a temporary path for saving the game state
    file_path = tmp_path / "game.pkl"

    # Save the game state
    sl.save_game(sample_game_state, file_path)

    # Ensure file exists
    assert file_path.exists()

    # Load the game state
    loaded_game = sl.load_game(file_path)

    assert loaded_game == sample_game_state

def test_save_exists(sl: Any, tmp_path: Path):
    # Use a temporary path for saving the game state
    file_path = tmp_path / "game.pkl"

    # Assert that the save doesn't exist yet
    assert not sl.save_exists(file_path)

    # Create a dummy file
    with open(file_path, "wb") as f:
        f.write(b'')

    # Assert that the save exists now
    assert sl.save_exists(file_path)

def test_list_saves(sl: Any, tmp_path: Path):
    # Create some dummy save files
    for i in range(3):
        with open(tmp_path / f"game_{i}.pkl", "wb") as f:
            f.write(b'')

    saves = sl.list_saves(tmp_path)
    assert len(saves) == 3

def test_delete_save(sl: Any, tmp_path: Path):
    # Use a temporary path for saving the game state
    file_path = tmp_path / "game.pkl"

    # Create a dummy file
    with open(file_path, "wb") as f:
        f.write(b'')

    assert file_path.exists()

    # Delete the save
    sl.delete_save(file_path)

    # Ensure the file no longer exists
    assert not file_path.exists()
