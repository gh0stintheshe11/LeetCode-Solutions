class Solution:
    def numPermsDISequence(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        for j in range(n + 1):
            dp[0][j] = 1
        
        for i in range(1, n + 1):
            if s[i - 1] == 'I':
                cumulative_sum = 0
                for j in range(n - i + 1):
                    cumulative_sum = (cumulative_sum + dp[i - 1][j]) % MOD
                    dp[i][j] = cumulative_sum
            else:
                cumulative_sum = 0
                for j in range(n - i, -1, -1):
                    cumulative_sum = (cumulative_sum + dp[i - 1][j + 1]) % MOD
                    dp[i][j] = cumulative_sum
        
        return dp[n][0] % MOD