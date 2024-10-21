class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        # dp[i][j] means the maximum value we can get from the first i piles with choosing j coins
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            pile_prefix_sum = [0]  # cumulative sum of coins taken from the current pile
            current_pile = piles[i - 1]
            for coin in current_pile:
                pile_prefix_sum.append(pile_prefix_sum[-1] + coin)
                
            for j in range(k + 1):
                # not taking any coins from the current pile
                dp[i][j] = dp[i - 1][j]
                # try taking x coins from the current pile (1 ≤ x ≤ min(j, len(current_pile)))
                for x in range(1, min(j, len(current_pile)) + 1):
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - x] + pile_prefix_sum[x])
                    
        return dp[n][k]