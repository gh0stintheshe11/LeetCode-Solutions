from typing import List

class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        max_sum = 0
        m, n = len(grid), len(grid[0])
        
        for i in range(m - 2):
            for j in range(n - 2):
                hourglass_sum = (
                    grid[i][j] + grid[i][j + 1] + grid[i][j + 2] +
                    grid[i + 1][j + 1] +
                    grid[i + 2][j] + grid[i + 2][j + 1] + grid[i + 2][j + 2]
                )
                max_sum = max(max_sum, hourglass_sum)
        
        return max_sum