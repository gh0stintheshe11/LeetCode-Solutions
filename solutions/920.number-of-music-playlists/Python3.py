class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        MOD = 10**9 + 7
        
        # Initialize the DP table
        dp = [[0] * (n + 1) for _ in range(goal + 1)]
        dp[0][0] = 1
        
        for i in range(1, goal + 1):
            for j in range(1, n + 1):
                # Add a new song
                dp[i][j] += dp[i - 1][j - 1] * (n - (j - 1))
                dp[i][j] %= MOD
                
                # Reuse an old song
                if j > k:
                    dp[i][j] += dp[i - 1][j] * (j - k)
                    dp[i][j] %= MOD
        
        return dp[goal][n]