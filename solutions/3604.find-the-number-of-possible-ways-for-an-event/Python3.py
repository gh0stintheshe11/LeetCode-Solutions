class Solution:
    def numberOfWays(self, n: int, x: int, y: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [[0] * (x + 1) for _ in range(n)]
        for i in range(n):
            dp[i][1] = x
        for i in range(1, n):
            for j in range(1, x + 1):
                dp[i][j] = (dp[i - 1][j] * j + dp[i - 1][j - 1] * (x - j + 1)) % MOD
        res = 0
        for i in range(1, x + 1):
            res += dp[n - 1][i] * (y ** i)
        return res % MOD