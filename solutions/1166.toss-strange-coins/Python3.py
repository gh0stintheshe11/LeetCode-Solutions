from typing import List

class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        n = len(prob)
        dp = [[0.0] * (target + 1) for _ in range(n + 1)]
        
        # Base case: probability of getting 0 heads with 0 coins is 1
        dp[0][0] = 1.0
        
        for i in range(1, n + 1):
            for j in range(target + 1):
                # If the i-th coin is heads
                if j > 0:
                    dp[i][j] += dp[i - 1][j - 1] * prob[i - 1]
                # If the i-th coin is tails
                dp[i][j] += dp[i - 1][j] * (1 - prob[i - 1])
        
        return dp[n][target]