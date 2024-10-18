from typing import List
from collections import defaultdict

class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        n = len(prizePositions)
        # dp[i]: maximum number of prizes we can collect starting from i
        dp = [0] * (n + 1)
        
        # Using two pointers to calculate the maximum prizes that can be collected with one segment
        end = 0
        for start in range(n):
            # Move 'end' to include as many prizes as possible within a segment of length k
            while end < n and prizePositions[end] <= prizePositions[start] + k:
                end += 1
            dp[start] = end - start
            
        # Compute suffix maximums for dp
        for i in range(n - 1, -1, -1):
            dp[i] = max(dp[i], dp[i + 1])
        
        # Now find the maximum possible prizes with two segments
        max_prizes = 0
        end = 0
        for start in range(n):
            # Move 'end' to include as many prizes as possible within a segment of length k
            while end < n and prizePositions[end] <= prizePositions[start] + k:
                end += 1
            # Calculate prizes for one segment [start, end-1] and another anywhere else
            max_prizes = max(max_prizes, end - start + (dp[end] if end < n else 0))
        
        return max_prizes