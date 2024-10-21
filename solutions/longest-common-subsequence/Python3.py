class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Get the lengths of the two strings
        m, n = len(text1), len(text2)
        
        # Create a 2D array to store the lengths of LCS
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Fill the dp array
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        # The length of the longest common subsequence
        return dp[m][n]