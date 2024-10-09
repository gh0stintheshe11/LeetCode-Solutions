class Solution:
    def waysToDistribute(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                dp[i][j] = (j * dp[i - 1][j] + dp[i - 1][j - 1]) % MOD
        
        return dp[n][k]