from typing import List

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        # Pair up ages and scores and sort them
        players = sorted(zip(ages, scores))
        
        # Initialize the DP array
        n = len(players)
        dp = [0] * n
        
        # Fill the DP array
        for i in range(n):
            dp[i] = players[i][1]  # Start with the player's own score
            for j in range(i):
                if players[j][1] <= players[i][1]:  # No conflict condition
                    dp[i] = max(dp[i], dp[j] + players[i][1])
        
        # The result is the maximum value in the DP array
        return max(dp)
