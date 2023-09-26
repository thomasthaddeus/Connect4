"""AI.py
This module provides an AI class for playing a board game.

The AI uses the minimax algorithm with alpha-beta pruning to evaluate board states and make decisions.

Returns:
    _type_: _description_
"""

import random
import math


class AI:
    """
    Represents an AI player for a board game.

    Attributes:
        plyr_num (int): The number representing the AI player on the board.
    """

    def __init__(self, plyr_num):
        """
        Initializes the AI with a player number.

        Args:
            plyr_num (int): The number representing the AI player on the board.
        """
        self.plyr_num = plyr_num

    def set_player_number(self, plyr_num):
        """
        Sets the player number for the AI.

        Args:
            plyr_num (int): The number representing the AI player on the board.
        """
        self.plyr_num = plyr_num

    def minimax(self, board, depth, alpha, beta, maximizing_player):
        """
        Implements the minimax algorithm with alpha-beta pruning to evaluate board states.

        Args:
            board (Board): The current state of the game board.
            depth (int): The depth of the game tree to explore.
            alpha (int): The best value that the maximizing player can guarantee.
            beta (int): The best value that the minimizing player can guarantee.
            maximizing_player (bool): True if the current player is maximizing, False otherwise.

        Returns:
            int: The evaluation score of the board.
        """
        if depth == 0 or board.get_winner() is not None:
            return self.evaluate_board(board)

        possible_moves = board.available_moves()

        if maximizing_player:
            max_eval = -math.inf
            for col in possible_moves:
                if board.make_move(self.plyr_num, col):
                    eval1 = self.minimax(board, depth - 1, alpha, beta, False)
                    board.board[col].pop()  # undo move
                    max_eval = max(max_eval, eval1)
                    alpha = max(alpha, eval1)
                    if beta <= alpha:
                        break
            return max_eval
        else:
            min_eval = math.inf
            for col in possible_moves:
                if board.make_move(3 - self.plyr_num, col):  # other player's number
                    eval1 = self.minimax(board, depth - 1, alpha, beta, True)
                    board.board[col].pop()  # undo move
                    min_eval = min(min_eval, eval1)
                    beta = min(beta, eval1)
                    if beta <= alpha:
                        break
            return min_eval

    def find_best_move(self, board):
        """
        Finds the best move for the AI based on the current board state.

        Args:
            board (Board): The current state of the game board.

        Returns:
            int: The column number of the best move.
        """
        best_eval = -math.inf
        possible_moves = board.available_moves()
        best_move = random.choice(possible_moves)  # random valid move

        for col in possible_moves:
            if board.make_move(self.plyr_num, col):
                eval = self.minimax(board, 3, -math.inf, math.inf, False)  # depth 3
                board.board[col].pop()  # undo move
                if eval > best_eval:
                    best_eval = eval
                    best_move = col

        return best_move

    @staticmethod
    def check_direction(
        board,
        plyr_num,
        leng,
        row_start,
        col_st,
        row_step,
        col_step
    ):
        """
        Checks sequences in a given direction on the board.

        Args:
            board (Board): The current state of the game board.
            plyr_num (int): The player number to check sequences for.
            leng (int): The length of the sequence to check.
            row_start (int): The starting row index.
            col_st (int): The starting column index.
            row_step (int): The row step for checking.
            col_step (int): The column step for checking.

        Returns:
            int: The count of sequences found in the given direction.
        """
        count = 0
        seq = [plyr_num] * leng
        for row in range(row_start, board.rows, row_step):
            for col in range(col_st, board.columns, col_step):
                if all(board.board[col + col_step * offset][row + row_step * offset] == plyr_num for offset in range(leng)):
                    count += 1
        return count

    @classmethod
    def count_sequences(cls, board, plyr_num, leng):
        """
        Counts sequences of a given length for a player on the board.

        Args:
            board (Board): The current state of the game board.
            plyr_num (int): The player number to check sequences for.
            leng (int): The length of the sequence to check.

        Returns:
            int: The total count of sequences of the given length for the player.
        """
        count = 0
        # Check rows
        count += cls.check_direction(board, plyr_num, leng, 0, 0, 1, 0)
        # Check columns
        count += cls.check_direction(board, plyr_num, leng, 0, 0, 0, 1)
        # Check right diagonals
        count += cls.check_direction(board, plyr_num, leng, 0, 0, 1, 1)
        # Check left diagonals
        count += cls.check_direction(board, plyr_num, leng, 0, board.columns - 1, 1, -1)
        return count

    def evaluate_board(self, board):
        """
        Evaluates the current state of the board for the AI.

        Args:
            board (Board): The current state of the game board.

        Returns:
            int: The evaluation score of the board.
        """
        # Calculate score for different sequence lengths
        ai_scores = [self.count_sequences(board, self.plyr_num, i) for i in range(2, 5)]
        opponent_scores = [self.count_sequences(board, 3 - self.plyr_num, i) for i in range(2, 5)]

        # Weights for different sequence lengths
        weights = [1, 100, 100000]

        # Calculate total score
        ai_total = sum(ai_scores[i] * weights[i] for i in range(3))
        opponent_total = sum(opponent_scores[i] * weights[i] for i in range(3))

        if opponent_scores[2] > 0:  # If opponent has a sequence of length 4
            return -math.inf
        else:
            return ai_total - opponent_total
