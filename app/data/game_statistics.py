"""game_statistics.py

"""

import json

class GameStatistics:
    def __init__(self):
        self.total_games = 0
        self.player_wins = {}
        self.total_moves = 0

    def game_played(self, winner, moves):
        self.total_games += 1
        self.total_moves += len(moves)
        if winner is not None:
            if winner not in self.player_wins:
                self.player_wins[winner] = 0
            self.player_wins[winner] += 1

    def get_total_games(self):
        return self.total_games

    def get_player_wins(self):
        return self.player_wins

    def get_average_moves(self):
        if self.total_games == 0:
            return 0
        else:
            return self.total_moves / self.total_games

    def save_to_file(self, filename):
        data = {
            'total_games': self.total_games,
            'player_wins': self.player_wins,
            'total_moves': self.total_moves,
        }
        with open(filename, mode='w', encoding='utf-8') as f:
            json.dump(data, f)

    def load_from_file(self, filename):
        with open(filename, mode='r', encoding='utf-8') as f:
            data = json.load(f)
            self.total_games = data['total_games']
            self.player_wins = data['player_wins']
            self.total_moves = data['total_moves']