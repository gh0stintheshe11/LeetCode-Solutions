class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        
        # DP array to store results
        dp = [[0] * (k + 1) for _ in range(n)]

        # Base cases
        for i in range(n):
            dp[i][0] = 1  # There's always one way to make 0 segments

        for j in range(1, k + 1):
            sum_dp = 0
            for i in range(j, n):
                sum_dp += dp[i - 1][j - 1]
                sum_dp %= MOD
                dp[i][j] = (dp[i - 1][j] + sum_dp) % MOD

        return dp[n - 1][k]