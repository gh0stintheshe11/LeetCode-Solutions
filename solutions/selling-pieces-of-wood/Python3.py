class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        # Initialize the dp array
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Set prices into the dp array
        for h, w, price in prices:
            dp[h][w] = max(dp[h][w], price)
        
        # Use dynamic programming to fill in dp table
        for height in range(1, m + 1):
            for width in range(1, n + 1):
                for k in range(1, height // 2 + 1):
                    dp[height][width] = max(dp[height][width], dp[k][width] + dp[height - k][width])
                for k in range(1, width // 2 + 1):
                    dp[height][width] = max(dp[height][width], dp[height][k] + dp[height][width - k])
        
        return dp[m][n]