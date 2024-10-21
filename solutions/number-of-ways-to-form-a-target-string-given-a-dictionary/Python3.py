from typing import List

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9 + 7
        m, n = len(words), len(words[0])
        t_len = len(target)
        
        # Step 1: Create a frequency count array
        freq = [[0] * 26 for _ in range(n)]
        for word in words:
            for i, char in enumerate(word):
                freq[i][ord(char) - ord('a')] += 1
        
        # Step 2: Initialize the DP table
        dp = [[0] * (n + 1) for _ in range(t_len + 1)]
        dp[0][0] = 1
        
        # Step 3: Fill the DP table
        for i in range(t_len + 1):
            for j in range(n):
                if i < t_len:
                    dp[i + 1][j + 1] = (dp[i + 1][j + 1] + dp[i][j] * freq[j][ord(target[i]) - ord('a')]) % MOD
                dp[i][j + 1] = (dp[i][j + 1] + dp[i][j]) % MOD
        
        # The answer is the number of ways to form the entire target string
        return dp[t_len][n]