from typing import List
import sys

class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        houses.sort()
        n = len(houses)
        
        # Precompute the cost for putting a mailbox in a section of houses
        cost = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                median = houses[(i + j) // 2]
                for l in range(i, j + 1):
                    cost[i][j] += abs(houses[l] - median)
        
        # DP array
        dp = [[sys.maxsize] * (k + 1) for _ in range(n)]
        
        # Base case, one mailbox
        for i in range(n):
            dp[i][1] = cost[0][i]
        
        # Fill the DP table
        for j in range(2, k + 1):
            for i in range(n):
                for m in range(i):
                    dp[i][j] = min(dp[i][j], dp[m][j-1] + cost[m+1][i])
        
        return dp[n-1][k]