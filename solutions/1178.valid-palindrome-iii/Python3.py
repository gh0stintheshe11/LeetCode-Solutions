class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        def longest_palindromic_subsequence(s: str) -> int:
            n = len(s)
            dp = [[0] * n for _ in range(n)]
            for i in range(n):
                dp[i][i] = 1
            for length in range(2, n + 1):
                for i in range(n - length + 1):
                    j = i + length - 1
                    if s[i] == s[j]:
                        dp[i][j] = 2 + dp[i + 1][j - 1]
                    else:
                        dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
            return dp[0][n - 1]

        n = len(s)
        longest_palindrome_length = longest_palindromic_subsequence(s)
        return (n - longest_palindrome_length) <= k