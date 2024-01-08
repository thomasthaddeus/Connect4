""" main.py

_summary_

_extended_summary_
"""

from models import AI, Board, Connect4, Player

class GameBackend:
    """
     _summary_

    _extended_summary_
    """
    def __init__(self):
        """
        __init__ _summary_

        _extended_summary_
        """
        self.board = Board()
        self.game = Connect4()
        self.players = [Player("Player 1", 1), Player("Player 2", 2, is_ai=True)]
        self.ai = AI(2)  # Assuming Player 2 is the AI

    def start_game(self):
        """
        start_game _summary_

        _extended_summary_
        """
        while not self.board.is_full() and not self.board.get_winner():
            current_player = self.players[self.board.current_player - 1]
            if current_player.is_ai_player():
                best_move = self.ai.find_best_move(self.board)
                self.game.play_turn(best_move)
            else:
                # For now, we'll just get input from the console for the human player
                move = int(input(f"{current_player.get_name()}, enter your move (0-6): "))
                self.game.play_turn(move)

            # Display the board
            self.game.draw_board()

        winner = self.board.get_winner()
        if winner:
            print(f"Player {winner} wins!")
        else:
            print("It's a draw!")

if __name__ == "__main__":
    game_backend = GameBackend()
    game_backend.start_game()
