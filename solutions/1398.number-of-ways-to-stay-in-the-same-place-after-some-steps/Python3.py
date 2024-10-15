class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10**9 + 7
        max_pos = min(steps // 2, arrLen - 1)
        
        dp = [0] * (max_pos + 1)
        dp[0] = 1
        
        for _ in range(steps):
            next_dp = [0] * (max_pos + 1)
            for i in range(max_pos + 1):
                next_dp[i] = dp[i]
                if i > 0:
                    next_dp[i] = (next_dp[i] + dp[i - 1]) % MOD
                if i < max_pos:
                    next_dp[i] = (next_dp[i] + dp[i + 1]) % MOD
            dp = next_dp
        
        return dp[0]