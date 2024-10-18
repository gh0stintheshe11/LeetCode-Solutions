from typing import List
import collections
import heapq

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up
        pq = [(0, 0, 0)]  # cost, x, y
        visited = [[False] * n for _ in range(m)]
        
        while pq:
            cost, x, y = heapq.heappop(pq)
            if x == m - 1 and y == n - 1:
                return cost
            if visited[x][y]:
                continue
            visited[x][y] = True
            for i, (dx, dy) in enumerate(directions):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    new_cost = cost + (grid[x][y] != i + 1)
                    heapq.heappush(pq, (new_cost, nx, ny))