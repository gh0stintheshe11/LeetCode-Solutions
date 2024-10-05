from typing import List
from heapq import heappop, heappush

class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        heap = [(-grid[0][0], 0, 0)]
        visited = set((0, 0))
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        while heap:
            score, x, y = heappop(heap)
            score = -score
            if x == m-1 and y == n-1:
                return score
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    heappush(heap, (-min(score, grid[nx][ny]), nx, ny))