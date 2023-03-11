class Score:

    def __init__(self):
        self.games = 0
        self.wins = 0
        self.losses = 0
        self.ties = 0

    def increase_games(self):
        self.games += 1

    def increase_wins(self):
        self.wins += 1

    def increase_losses(self):
        self.losses += 1

    def increase_ties(self):
        self.ties += 1

    def get_stats(self):
        return [self.games, self.wins, self.losses, self.ties]
