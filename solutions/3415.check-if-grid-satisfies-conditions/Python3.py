from typing import List

class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # Check the column condition
        for j in range(n):
            for i in range(m - 1):
                if grid[i][j] != grid[i + 1][j]:
                    return False
        
        # Check the row condition
        for i in range(m):
            for j in range(n - 1):
                if grid[i][j] == grid[i][j + 1]:
                    return False
        
        return True