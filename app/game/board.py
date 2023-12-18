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
    """
    Represents a Connect 4 board.

    This class encapsulates the state and behavior of a Connect 4 board. It provides methods to initialize the board, make moves, check the game status (win, draw, or ongoing), and manage player turns.

    Attributes:
        rows (int): Number of rows in the board. Default is 6.
        columns (int): Number of columns in the board. Default is 7.
        board (list): A 2D list representing the board state.
        current_player (str): The current player ('X' or 'O').
    """

    def __init__(self, rows=6, columns=7):
        """
        Initializes a new board for Connect 4.

        Args:
            rows (int, optional): The number of rows in the board. Defaults to 6.
            columns (int, optional): The number of columns in the board. Defaults to 7.
        """
        self.rows = rows
        self.columns = columns
        self.board = [[None for _ in range(rows)] for _ in range(columns)]
        self.current_player = "X"

    def __repr__(self):
        """
        Provides a string representation of the board for debugging and display.

        Returns:
            str: A string representing the current state of the board.
        """
        board_representation = ""
        for row in range(
            self.rows - 1, -1, -1
        ):  # Start from the last row for correct visualization
            row_data = [str(self.board[col][row] or ".") for col in range(self.columns)]
            board_representation += " | ".join(row_data) + "\n"
        return board_representation

    def is_valid_move(self, column):
        """
        is_valid_move _summary_

        _extended_summary_

        Args:
            column (_type_): _description_

        Returns:
            _type_: _description_
        """
        return len(self.board[column]) < self.rows

    def available_moves(self):
        """
        available_moves _summary_

        _extended_summary_

        Returns:
            _type_: _description_
        """
        return [
            col
            for col, column_data in enumerate(self.board)
            if len(column_data) < self.rows
        ]

    def make_move(self, player, column):
        """
        make_move _summary_

        _extended_summary_

        Args:
            player (_type_): _description_
            column (_type_): _description_

        Returns:
            _type_: _description_
        """
        for row in range(self.rows):
            if self.board[column][row] is None:
                self.board[column][row] = player
                return True
        return False

    def is_full(self):
        """
        is_full _summary_

        _extended_summary_

        Returns:
            _type_: _description_
        """
        return all(cell is not None for col in self.board for cell in col)

    def is_draw(self):
        """
        is_draw _summary_

        _extended_summary_

        Returns:
            _type_: _description_
        """
        return self.is_full() and not self.get_winner()

    def get_column_state(self, column):
        """
        get_column_state _summary_

        _extended_summary_

        Args:
            column (_type_): _description_

        Returns:
            _type_: _description_
        """
        return self.board[column]

    def switch_player(self):
        """
        switch_player _summary_

        _extended_summary_
        """
        self.current_player = "O" if self.current_player == "X" else "X"

    def get_winner(self):
        """
        get_winner _summary_

        _extended_summary_

        Returns:
            _type_: _description_
        """
        for col in range(self.columns):
            for row in range(self.rows):
                player = self.board[col][row]
                if not player:
                    continue
                # Check right
                if col + 3 < self.columns and all(
                    self.board[c][row] == player for c in range(col, col + 4)
                ):
                    return player
                # Check down
                if row + 3 < self.rows and all(
                    self.board[col][r] == player for r in range(row, row + 4)
                ):
                    return player
                # Check diagonal right-down
                if (
                    col + 3 < self.columns
                    and row + 3 < self.rows
                    and all(self.board[col + i][row + i] == player for i in range(4))
                ):
                    return player
                # Check diagonal left-down
                if (
                    col - 3 >= 0
                    and row + 3 < self.rows
                    and all(self.board[col - i][row + i] == player for i in range(4))
                ):
                    return player
        return None  # No winner found

    def check_winner(self):
        """
        check_winner _summary_

        _extended_summary_

        Returns:
            _type_: _description_
        """
        for row in range(6):
            for col in range(7):
                try:
                    if (
                        self.board[row][col] == self.current_player
                        and self.board[row + 1][col + 1] == self.current_player
                        and self.board[row + 2][col + 2] == self.current_player
                        and self.board[row + 3][col + 3] == self.current_player
                    ):
                        return True
                except IndexError:
                    pass

                try:
                    if (
                        self.board[row][col] == self.current_player
                        and self.board[row + 1][col] == self.current_player
                        and self.board[row + 2][col] == self.current_player
                        and self.board[row + 3][col] == self.current_player
                    ):
                        return True
                except IndexError:
                    pass

                if (
                    col < 4
                    and self.board[row][col] == self.current_player
                    and self.board[row][col + 1] == self.current_player
                    and self.board[row][col + 2] == self.current_player
                    and self.board[row][col + 3] == self.current_player
                ):
                    return True

                if (
                    row < 3
                    and self.board[row][col] == self.current_player
                    and self.board[row + 1][col] == self.current_player
                    and self.board[row + 2][col] == self.current_player
                    and self.board[row + 3][col] == self.current_player
                ):
                    return True

        return False

    def reset(self):
        """
        reset _summary_

        _extended_summary_
        """
        self.board = [[None for _ in range(self.rows)] for _ in range(self.columns)]


class Connect4:
    """
    Manages the overall game logic for a Connect 4 game.

    This class uses a Board object to maintain the game state and provides
    methods for drawing the board, handling player turns, and managing the game
    flow.

    Attributes:
        board (Board): An instance of the Board class representing the game
        board.
    """

    def __init__(self):
        """
        __init__ _summary_

        _extended_summary_
        """
        self.board = Board()

    def draw_board(self):
        """
        draw_board _summary_

        _extended_summary_
        """
        print("\n".join([" ".join(row) for row in self.board[::-1]]))
        print(" ".join(map(str, range(1, 8))))

    def play_turn(self, col):
        """
        play_turn _summary_

        _extended_summary_

        Args:
            col (_type_): _description_

        Returns:
            _type_: _description_
        """
        if self.board.make_move(self.board.current_player, col):
            if self.board.get_winner():
                print(f"Player {self.board.current_player} wins!")
                self.draw_board()
                return True
            self.board.switch_player()
        else:
            print("This column is full, try a different one!")
        return False
