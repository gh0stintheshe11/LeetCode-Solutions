from collections import defaultdict
from typing import List

class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        if len(votes) == 1:
            return votes[0]

        num_positions = len(votes[0])
        rank_count = defaultdict(lambda: [0] * num_positions)

        for vote in votes:
            for position, team in enumerate(vote):
                rank_count[team][position] -= 1

        sorted_teams = sorted(rank_count.keys(), key=lambda team: (rank_count[team], team))
        return ''.join(sorted_teams)