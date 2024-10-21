class Leaderboard:

    def __init__(self):
        self.player_scores = {}

    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.player_scores:
            self.player_scores[playerId] += score
        else:
            self.player_scores[playerId] = score

    def top(self, K: int) -> int:
        return sum(sorted(self.player_scores.values(), reverse=True)[:K])

    def reset(self, playerId: int) -> None:
        if playerId in self.player_scores:
            self.player_scores[playerId] = 0