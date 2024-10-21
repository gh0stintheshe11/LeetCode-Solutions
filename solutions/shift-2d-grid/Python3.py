from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        if not grid:
            return grid
        
        m, n = len(grid), len(grid[0])
        total = m * n
        k = k % total
        
        if k == 0:
            return grid
        
        def flatten(grid):
            result = []
            for row in grid:
                result.extend(row)
            return result
        
        flat_grid = flatten(grid)
        flat_grid = flat_grid[-k:] + flat_grid[:-k]
        
        result = []
        for i in range(m):
            result.append(flat_grid[i * n:(i + 1) * n])
        
        return result