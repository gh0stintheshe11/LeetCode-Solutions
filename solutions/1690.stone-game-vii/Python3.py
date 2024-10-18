class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)
        prefix_sum = [0] * (n + 1)
        
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + stones[i]
        
        dp = [[0] * n for _ in range(n)]
        
        for length in range(2, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1
                total_sum = prefix_sum[r + 1] - prefix_sum[l]
                dp[l][r] = max(total_sum - stones[l] - dp[l + 1][r],
                               total_sum - stones[r] - dp[l][r - 1])
        
        return dp[0][n - 1]