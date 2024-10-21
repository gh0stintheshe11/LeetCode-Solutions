from typing import List

class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10**9 + 7
        length = len(group)
        
        # Initialize the DP table
        dp = [[[0] * (minProfit + 1) for _ in range(n + 1)] for _ in range(length + 1)]
        dp[0][0][0] = 1
        
        for i in range(1, length + 1):
            g = group[i - 1]
            p = profit[i - 1]
            for j in range(n + 1):
                for k in range(minProfit + 1):
                    # If we don't take the current crime
                    dp[i][j][k] = dp[i - 1][j][k]
                    # If we take the current crime
                    if j >= g:
                        dp[i][j][k] += dp[i - 1][j - g][max(0, k - p)]
                        dp[i][j][k] %= MOD
        
        # Sum up all the ways to achieve at least minProfit with any number of members
        result = sum(dp[length][j][minProfit] for j in range(n + 1)) % MOD
        return result
