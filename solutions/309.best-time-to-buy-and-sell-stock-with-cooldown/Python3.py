from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        n = len(prices)
        if n == 1:
            return 0
        
        # dp[i][0]: The maximum profit on day i with no stock in hand (rest or after selling)
        # dp[i][1]: The maximum profit on day i with stock in hand
        dp = [[0]*2 for _ in range(n)]
        
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], (dp[i-2][0] if i > 1 else 0) - prices[i])
        
        return dp[n-1][0]