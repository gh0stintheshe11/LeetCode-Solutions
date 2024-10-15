from collections import deque
from typing import List

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        queue = deque([(0, 0, health - grid[0][0])])
        visited = set([(0, 0, health - grid[0][0])])
        
        while queue:
            x, y, h = queue.popleft()
            
            if x == m - 1 and y == n - 1 and h > 0:
                return True
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < m and 0 <= ny < n:
                    nh = h - grid[nx][ny]
                    if nh > 0 and (nx, ny, nh) not in visited:
                        visited.add((nx, ny, nh))
                        queue.append((nx, ny, nh))
        
        return False