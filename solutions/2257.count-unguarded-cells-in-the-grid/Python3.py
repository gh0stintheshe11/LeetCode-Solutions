from typing import List

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        
        # Mark guards and walls in the grid
        for x, y in guards:
            grid[x][y] = 2  # Guard
        for x, y in walls:
            grid[x][y] = 3  # Wall
        
        # Directions: right(0,1), left(0,-1), down(1,0), up(-1,0)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # Function to mark sight line from a guard
        def mark_from_guard(x, y):
            for dx, dy in directions:
                nx, ny = x, y
                while True:
                    nx += dx
                    ny += dy
                    if not (0 <= nx < m and 0 <= ny < n) or grid[nx][ny] == 3 or grid[nx][ny] == 2:
                        break
                    if grid[nx][ny] == 0:
                        grid[nx][ny] = 1  # Mark as guarded
        
        # Marking all guarded regions
        for x, y in guards:
            mark_from_guard(x, y)
        
        # Counting unguarded and unoccupied cells
        unguarded_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    unguarded_count += 1
        
        return unguarded_count