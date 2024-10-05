import heapq
from typing import List

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        pq = [(grid[0][0], 0, 0)]  # PriorityQueue (water level, x, y)
        visited = set((0, 0))
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while pq:
            level, x, y = heapq.heappop(pq)
            if x == n - 1 and y == n - 1:
                return level
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    heapq.heappush(pq, (max(level, grid[nx][ny]), nx, ny))