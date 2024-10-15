class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        last = {}
        
        for i in range(1, n + 1):
            dp[i] = (2 * dp[i - 1]) % MOD
            if s[i - 1] in last:
                dp[i] = (dp[i] - dp[last[s[i - 1]] - 1]) % MOD
            last[s[i - 1]] = i

        return (dp[n] - 1) % MOD