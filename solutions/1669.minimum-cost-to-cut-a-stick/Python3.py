from typing import List

class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        # Add the boundaries to the cuts array
        cuts = sorted(cuts)
        cuts = [0] + cuts + [n]
        
        # Number of cuts including the boundaries
        m = len(cuts)
        
        # Initialize the DP table
        dp = [[0] * m for _ in range(m)]
        
        # Fill the DP table
        for length in range(2, m):  # length is the distance between i and j
            for i in range(m - length):
                j = i + length
                dp[i][j] = float('inf')
                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + cuts[j] - cuts[i])
        
        # The result is the minimum cost to cut the stick from 0 to n
        return dp[0][m - 1]