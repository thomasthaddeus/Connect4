"""board.py

Summary:
    Class to represent a Connect 4 board.

Extended Summary:
    This class manages the state of the Connect 4 board, allows players to make moves,
    checks if the board is full, determines the winner, and can reset itself to the initial state.

Returns:
    bool: Whether the action (like making a move) was successful.
"""

class Board:
    def __init__(self, rows=6, columns=7):
        self.rows = rows
        self.columns = columns
        self.board = [[None for _ in range(rows)] for _ in range(columns)]
        self.current_player = 'X'

    def __repr__(self):
        board_representation = ""
        for row in range(self.rows - 1, -1, -1):  # Start from the last row for correct visualization
            row_data = [str(self.board[col][row] or ".") for col in range(self.columns)]
            board_representation += " | ".join(row_data) + "\n"
        return board_representation

    def is_valid_move(self, column):
        return len(self.board[column]) < self.rows

    def available_moves(self):
        return [col for col, column_data in enumerate(self.board) if len(column_data) < self.rows]

    def make_move(self, player, column):
        for row in range(self.rows):
            if self.board[column][row] is None:
                self.board[column][row] = player
                return True
        return False

    def is_full(self):
        return all(cell is not None for col in self.board for cell in col)

    def is_draw(self):
        return self.is_full() and not self.get_winner()

    def get_column_state(self, column):
        return self.board[column]

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def get_winner(self):
        for col in range(self.columns):
            for row in range(self.rows):
                player = self.board[col][row]
                if not player:
                    continue
                # Check right
                if col + 3 < self.columns and all(self.board[c][row] == player for c in range(col, col + 4)):
                    return player
                # Check down
                if row + 3 < self.rows and all(self.board[col][r] == player for r in range(row, row + 4)):
                    return player
                # Check diagonal right-down
                if col + 3 < self.columns and row + 3 < self.rows and all(self.board[col + i][row + i] == player for i in range(4)):
                    return player
                # Check diagonal left-down
                if col - 3 >= 0 and row + 3 < self.rows and all(self.board[col - i][row + i] == player for i in range(4)):
                    return player
        return None  # No winner found

    def check_winner(self):
        for row in range(6):
            for col in range(7):
                try:
                    if self.board[row][col] == self.current_player and \
                        self.board[row+1][col+1] == self.current_player and \
                        self.board[row+2][col+2] == self.current_player and \
                        self.board[row+3][col+3] == self.current_player:
                        return True
                except IndexError:
                    pass

                try:
                    if self.board[row][col] == self.current_player and \
                        self.board[row+1][col] == self.current_player and \
                        self.board[row+2][col] == self.current_player and \
                        self.board[row+3][col] == self.current_player:
                        return True
                except IndexError:
                    pass

                if col < 4 and \
                    self.board[row][col] == self.current_player and \
                    self.board[row][col+1] == self.current_player and \
                    self.board[row][col+2] == self.current_player and \
                    self.board[row][col+3] == self.current_player:
                    return True

                if row < 3 and \
                    self.board[row][col] == self.current_player and \
                    self.board[row+1][col] == self.current_player and \
                    self.board[row+2][col] == self.current_player and \
                    self.board[row+3][col] == self.current_player:
                    return True

        return False

    def reset(self):
        self.board = [[None for _ in range(self.rows)] for _ in range(self.columns)]

class Connect4:
    def __init__(self):
        self.board = Board()

    def draw_board(self):
        print('\n'.join([' '.join(row) for row in self.board[::-1]]))
        print(' '.join(map(str, range(1, 8))))

    def play_turn(self, col):
        if self.board.make_move(self.board.current_player, col):
            if self.board.get_winner():
                print(f"Player {self.board.current_player} wins!")
                self.draw_board()
                return True
            self.board.switch_player()
        else:
            print("This column is full, try a different one!")
        return False
