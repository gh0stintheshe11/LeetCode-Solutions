class Solution:
    def numberOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        coins = [1, 2, 4, 6]
        
        # dp[i][j] will be the number of ways to make sum j with i or less types of coins
        dp = [[0] * (n + 1) for _ in range(len(coins) + 1)]
        dp[0][0] = 1
        
        for i in range(1, len(coins) + 1):
            coin = coins[i-1]
            for j in range(n + 1):
                dp[i][j] = dp[i-1][j]
                if coin == 4:
                    # Special handling for coin 4 as it can be used at most twice
                    if j >= 4:
                        dp[i][j] = (dp[i][j] + dp[i-1][j-4]) % MOD
                    if j >= 8:
                        dp[i][j] = (dp[i][j] + dp[i-1][j-8]) % MOD
                else:
                    if j >= coin:
                        dp[i][j] = (dp[i][j] + dp[i][j-coin]) % MOD
        
        return dp[len(coins)][n]