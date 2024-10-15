from typing import List

class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        
        # Precompute the prefix sums
        prefix_sum = [[0] * n for _ in range(m)]
        prefix_sum[0][0] = grid[0][0]
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    prefix_sum[i][j] = prefix_sum[i][j-1] + grid[i][j]
                elif j == 0:
                    prefix_sum[i][j] = prefix_sum[i-1][j] + grid[i][j]
                else:
                    prefix_sum[i][j] = grid[i][j] + prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1]
        
        # Only consider submatrices with the top-left corner at (0,0)
        for end_row in range(m):
            for end_col in range(n):
                submatrix_sum = prefix_sum[end_row][end_col]
                if submatrix_sum <= k:
                    count += 1
        
        return count