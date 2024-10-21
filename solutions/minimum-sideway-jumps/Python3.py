from typing import List

class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        n = len(obstacles) - 1
        dp = [1, 0, 1]  # Initial jumps for lanes 1, 2, and 3 at point 0

        for i in range(1, n + 1):
            # Set impossibility for lanes with obstacles
            for lane in range(3):
                if obstacles[i] == lane + 1:
                    dp[lane] = float('inf')

            # Calculate sideway jumps where there are no obstacles
            min_jumps = min(dp)
            for lane in range(3):
                if obstacles[i] != lane + 1:
                    dp[lane] = min(dp[lane], min_jumps + 1)
        
        return min(dp)