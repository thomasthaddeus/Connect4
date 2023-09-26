import pytest
from board import Board, Connect4

# ------ Board class tests ------

def test_board_initialization():
    b = Board()
    assert b.rows == 6
    assert b.columns == 7
    assert b.board == [[None for _ in range(6)] for _ in range(7)]
    assert b.current_player == 'X'

def test_make_move():
    b = Board()
    result = b.make_move('X', 3)
    assert result is True
    assert b.board[3][0] == 'X'

def test_full_column_move():
    b = Board()
    for i in range(6):
        b.make_move('X', 3)
    result = b.make_move('X', 3)
    assert result is False

def test_winner_check_horizontal():
    b = Board()
    for col in range(4):
        b.make_move('X', col)
    assert b.get_winner() == 'X'

def test_winner_check_vertical():
    b = Board()
    for _ in range(4):
        b.make_move('X', 0)
    assert b.get_winner() == 'X'

def test_winner_check_diagonal():
    b = Board()
    for i in range(4):
        for _ in range(i):
            b.make_move('O', i)
        b.make_move('X', i)
    assert b.get_winner() == 'X'

def test_board_is_full():
    b = Board()
    for col in range(7):
        for _ in range(6):
            b.make_move('X', col)
    assert b.is_full() is True

def test_board_reset():
    b = Board()
    for col in range(7):
        for _ in range(6):
            b.make_move('X', col)
    b.reset()
    assert b.board == [[None for _ in range(6)] for _ in range(7)]

# ------ Connect4 class tests ------

def test_connect4_initialization():
    c = Connect4()
    assert isinstance(c.board, Board)

def test_connect4_play_turn():
    c = Connect4()
    result = c.play_turn(3)
    assert result is False  # Because no one has won yet
    assert c.board.board[3][0] == 'X'

def test_connect4_column_full():
    c = Connect4()
    for i in range(6):
        c.play_turn(3)
    result = c.play_turn(3)
    assert result is False

def test_connect4_win():
    c = Connect4()
    for col in range(4):
        c.play_turn(col)  # Play as 'X'
        c.play_turn((col + 4) % 7)  # Play as 'O' in other columns
    assert c.play_turn(4) is True  # Player 'X' should win now
