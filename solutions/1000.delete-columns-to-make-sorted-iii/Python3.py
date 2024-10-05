from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs[0])
        dp = [1] * n  # dp[i] : length of longest increasing subsequence ending at column i
        
        # Fill the dp array
        for i in range(n):
            for j in range(i):
                if all(row[j] <= row[i] for row in strs):
                    dp[i] = max(dp[i], dp[j] + 1)
                    
        # The minimum number of deletions required
        return n - max(dp)