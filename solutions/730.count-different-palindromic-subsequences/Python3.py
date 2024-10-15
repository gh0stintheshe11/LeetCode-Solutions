class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        
        dp = [[0] * n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = 1
        
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    low, high = i + 1, j - 1
                    while low <= j and s[low] != s[i]:
                        low += 1
                    while high >= i and s[high] != s[j]:
                        high -= 1
                    if low > high:  # No same characters found
                        dp[i][j] = 2 * dp[i + 1][j - 1] + 2
                    elif low == high:  # One same character found
                        dp[i][j] = 2 * dp[i + 1][j - 1] + 1
                    else:  # Two or more same characters found
                        dp[i][j] = 2 * dp[i + 1][j - 1] - dp[low + 1][high - 1]
                else:
                    dp[i][j] = dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]
                
                dp[i][j] = (dp[i][j] + MOD) % MOD
        
        return dp[0][n - 1]