from typing import List

class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
            
        m, n = len(grid), len(grid[0])
        row_hits, col_hits = 0, [0] * n
        max_enemies = 0
        
        for i in range(m):
            for j in range(n):
                if j == 0 or grid[i][j-1] == 'W': # Calculate row_hits
                    row_hits = 0
                    for k in range(j, n):
                        if grid[i][k] == 'W':
                            break
                        elif grid[i][k] == 'E':
                            row_hits += 1
                
                if i == 0 or grid[i-1][j] == 'W': # Calculate col_hits
                    col_hits[j] = 0
                    for k in range(i, m):
                        if grid[k][j] == 'W':
                            break
                        elif grid[k][j] == 'E':
                            col_hits[j] += 1
                
                if grid[i][j] == '0': # Calculate max_enemies
                    max_enemies = max(max_enemies, row_hits + col_hits[j])
        
        return max_enemies