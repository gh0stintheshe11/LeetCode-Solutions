from typing import List

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        result = [[0] * (n - 2) for _ in range(n - 2)]
        
        for i in range(n - 2):
            for j in range(n - 2):
                local_max = 0
                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        local_max = max(local_max, grid[r][c])
                result[i][j] = local_max
        
        return result