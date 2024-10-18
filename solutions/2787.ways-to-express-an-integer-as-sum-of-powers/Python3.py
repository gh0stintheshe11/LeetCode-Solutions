class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10**9 + 7

        powers = []
        i = 1
        while i ** x <= n:
            powers.append(i ** x)
            i += 1

        dp = [0] * (n + 1)
        dp[0] = 1

        for power in powers:
            for j in range(n, power - 1, -1):
                dp[j] = (dp[j] + dp[j - power]) % MOD

        return dp[n]