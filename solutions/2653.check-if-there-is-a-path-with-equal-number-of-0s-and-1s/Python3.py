from typing import List

class Solution:
    def isThereAPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # Initial boundary check for possibility
        if (m + n - 1) % 2 != 0:
            return False
        
        # Dynamic Programming table, using set of possible diffs
        dp = [[set() for _ in range(n)] for _ in range(m)]
        
        # Initialize starting point
        dp[0][0].add((1 if grid[0][0] == 1 else -1))
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                possible_diffs = set()
                
                if i > 0:
                    for diff in dp[i-1][j]:
                        new_diff = diff + (1 if grid[i][j] == 1 else -1)
                        possible_diffs.add(new_diff)
                
                if j > 0:
                    for diff in dp[i][j-1]:
                        new_diff = diff + (1 if grid[i][j] == 1 else -1)
                        possible_diffs.add(new_diff)
                
                dp[i][j] = possible_diffs
        
        # Final check for the possibility of reaching the destination with diff == 0
        return 0 in dp[m-1][n-1]