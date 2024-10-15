class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        MOD = 1000000007
        dp = [1] * n
        
        for _ in range(k):
            for i in range(1, n):
                dp[i] = (dp[i] + dp[i - 1]) % MOD
        
        return dp[-1]