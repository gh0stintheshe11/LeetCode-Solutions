class Solution:
    def deleteString(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 0

        for i in range(n - 1, -1, -1):
            max_ops = 1
            for j in range(1, (n - i) // 2 + 1):
                if s[i:i + j] == s[i + j:i + 2 * j]:
                    max_ops = max(max_ops, 1 + dp[i + j])
            dp[i] = max_ops

        return dp[0]