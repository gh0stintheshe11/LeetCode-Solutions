from collections import deque
from typing import List

class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Find the start position
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '*':
                    start = (r, c)
                    break
        
        # BFS initialization
        queue = deque([(start[0], start[1], 0)])
        visited = set((start[0], start[1]))
        
        # Perform BFS
        while queue:
            x, y, step = queue.popleft()
            
            # Check if we reached a food cell
            if grid[x][y] == '#':
                return step
            
            # Explore neighbors
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and grid[nx][ny] != 'X':
                    queue.append((nx, ny, step + 1))
                    visited.add((nx, ny))
        
        return -1