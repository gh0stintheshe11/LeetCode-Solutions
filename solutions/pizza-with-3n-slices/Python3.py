from typing import List

class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        def getMaxSlices(slices: List[int], n: int) -> int:
            dp = [[0] * (n + 1) for _ in range(len(slices) + 1)]
            
            for i in range(1, len(slices) + 1):
                for j in range(1, min(i + 1, n + 1)):
                    dp[i][j] = max(dp[i - 1][j], (dp[i - 2][j - 1] + slices[i - 1]) if i > 1 else slices[i - 1])
                    
            return dp[len(slices)][n]
        
        n = len(slices) // 3
        # Since the slices are circular
        # Case 1: Take slices[0] to slices[n-2]
        # Case 2: Take slices[1] to slices[n-1]
        return max(getMaxSlices(slices[:-1], n), getMaxSlices(slices[1:], n))