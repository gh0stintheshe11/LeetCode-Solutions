class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        # dp[i][j] will store the length of the longest palindromic subsequences starting at i and at j that are good
        dp = [[[0] * 26 for _ in range(n)] for _ in range(n)]

        for length in range(2, n + 1):  # Starting with length 2 to n
            for i in range(n - length + 1):  # Start index of substring
                j = i + length - 1  # End index of substring
                for char in range(26):  # a to z
                    c = chr(char + ord('a'))
                    if s[i] == s[j] == c:
                        if length == 2:  # If we have a pair
                            dp[i][j][char] = 2
                        else:
                            # Take max of inside precomputed value and this new pair
                            for k in range(26):
                                if c != chr(k + ord('a')):
                                    dp[i][j][char] = max(dp[i][j][char], 2 + dp[i + 1][j - 1][k])
                    else:
                        # Update based on previously computed values
                        dp[i][j][char] = max(dp[i][j][char], dp[i + 1][j][char], dp[i][j - 1][char])

        max_len = 0
        for char in range(26):
            max_len = max(max_len, dp[0][n - 1][char])

        return max_len