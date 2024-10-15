from typing import List
from collections import deque

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0
        queue = deque([(0, 0)])
        
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    new_dist = dist[x][y] + grid[nx][ny]
                    if new_dist < dist[nx][ny]:
                        dist[nx][ny] = new_dist
                        if grid[nx][ny] == 0:
                            queue.appendleft((nx, ny))
                        else:
                            queue.append((nx, ny))

        return dist[m - 1][n - 1]