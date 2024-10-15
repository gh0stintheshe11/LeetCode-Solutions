class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        m, n = len(s1), len(s2)
        
        if n > m:
            return ""
        
        # Initialize the dp array
        dp = [[-1] * (m + 1) for _ in range(n + 1)]

        # Base case: an empty s2 can be matched in any prefix of s1
        for j in range(m + 1):
            dp[0][j] = j

        # Fill the dp array
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s2[i - 1] == s1[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]

        # Find the minimum window
        start, length = 0, float('inf')
        for j in range(1, m + 1):
            if dp[n][j] != -1:
                if j - dp[n][j] < length:
                    start = dp[n][j]
                    length = j - dp[n][j]

        return s1[start:start + length] if length != float('inf') else ""