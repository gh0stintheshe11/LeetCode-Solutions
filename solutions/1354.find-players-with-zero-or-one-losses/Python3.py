from typing import List
from collections import defaultdict

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loss_counts = defaultdict(int)
        players = set()
        
        for winner, loser in matches:
            loss_counts[loser] += 1
            players.add(winner)
            players.add(loser)
        
        no_losses = [player for player in players if loss_counts[player] == 0]
        one_loss = [player for player in players if loss_counts[player] == 1]
        
        return [sorted(no_losses), sorted(one_loss)]