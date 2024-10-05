class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        
        # Initialize the DP table
        dp = [[0] * n for _ in range(n)]
        
        # Base case: single character substrings
        for i in range(n):
            dp[i][i] = 1
        
        # Fill the DP table
        for length in range(2, n + 1):  # length of the substring
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = dp[i + 1][j] + 1  # Initial assumption
                for k in range(i + 1, j + 1):
                    if s[k] == s[i]:
                        dp[i][j] = min(dp[i][j], dp[i + 1][k - 1] + dp[k][j])
        
        return dp[0][n - 1]

# Example usage:
# sol = Solution()
# print(sol.strangePrinter("aaabbb"))  # Output: 2
# print(sol.strangePrinter("aba"))     # Output: 2
