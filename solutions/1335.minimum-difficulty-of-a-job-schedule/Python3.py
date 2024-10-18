from typing import List

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        
        # Initialize dp array with infinity
        dp = [[float('inf')] * (d + 1) for _ in range(n + 1)]
        dp[0][0] = 0  # Base case: 0 jobs in 0 days has 0 difficulty
        
        for day in range(1, d + 1):
            for i in range(day, n + 1):
                max_difficulty = 0
                for k in range(i, day - 1, -1):
                    max_difficulty = max(max_difficulty, jobDifficulty[k - 1])
                    dp[i][day] = min(dp[i][day], dp[k - 1][day - 1] + max_difficulty)
        
        return dp[n][d]
