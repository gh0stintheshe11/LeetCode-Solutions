class Solution:
    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:
        n = len(present)
        profit = [future[i] - present[i] for i in range(n)]
        
        # Knapsack DP table initialization
        dp = [0] * (budget + 1)
        
        for i in range(n):
            if profit[i] > 0:
                for j in range(budget, present[i] - 1, -1):
                    dp[j] = max(dp[j], dp[j - present[i]] + profit[i])
        
        return dp[budget]