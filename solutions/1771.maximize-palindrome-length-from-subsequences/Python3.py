class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        combined = word1 + word2
        n = len(combined)
        dp = [[0] * n for _ in range(n)]
        
        maxLength = 0
        m1, m2 = len(word1), len(word2)

        for i in range(n):
            dp[i][i] = 1

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if combined[i] == combined[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                    if i < m1 <= j:
                        maxLength = max(maxLength, dp[i][j])
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])

        return maxLength