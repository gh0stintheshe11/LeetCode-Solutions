class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 5
        
        dp = [0] * (n + 1)
        dp[1], dp[2], dp[3] = 1, 2, 5
        
        for i in range(4, n + 1):
            dp[i] = (2 * dp[i - 1] + dp[i - 3]) % MOD
        
        return dp[n]