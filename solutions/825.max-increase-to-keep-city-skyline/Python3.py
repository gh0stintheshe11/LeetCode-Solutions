from typing import List

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # Determine the max heights for each row and column
        max_row_heights = [max(row) for row in grid]
        max_col_heights = [max(grid[row][col] for row in range(n)) for col in range(n)]
        
        # Calculate the total sum of the possible increases
        total_increase = 0
        for r in range(n):
            for c in range(n):
                allowed_height = min(max_row_heights[r], max_col_heights[c])
                total_increase += allowed_height - grid[r][c]
        
        return total_increase