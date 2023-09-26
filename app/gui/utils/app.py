app = QApplication([])

# Show Game Over Window (assuming player 1 won)
game_over_window = GameOverWindow("Player 1")
game_over_window.show()

# Sample statistics for Game Statistics Window
stats = {
    'wins': 10,
    'losses': 5,
    'draws': 3,
    'player1': {'wins': 7, 'losses': 3},
    'player2': {'wins': 3, 'losses': 7}
}
game_stats_window = GameStatisticsWindow(stats)
game_stats_window.show()

app.exec()
