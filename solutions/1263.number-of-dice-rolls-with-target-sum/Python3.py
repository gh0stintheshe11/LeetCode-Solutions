class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        
        for dice in range(1, n + 1):
            for t in range(1, target + 1):
                for face in range(1, min(k, t) + 1):
                    dp[dice][t] = (dp[dice][t] + dp[dice - 1][t - face]) % MOD
        return dp[n][target]