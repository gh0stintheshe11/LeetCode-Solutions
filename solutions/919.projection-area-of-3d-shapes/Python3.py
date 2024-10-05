from typing import List

class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        xy_projection = sum(v > 0 for row in grid for v in row)
        yz_projection = sum(max(row) for row in grid)
        zx_projection = sum(max(grid[j][i] for j in range(n)) for i in range(n))
        
        return xy_projection + yz_projection + zx_projection