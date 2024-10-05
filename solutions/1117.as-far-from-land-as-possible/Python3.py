from collections import deque
from typing import List

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = deque()

        # Start by adding all land cells (1) to the queue
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j))

        # If there are no water cells or no land cells, return -1
        if len(queue) == 0 or len(queue) == n * n:
            return -1

        # Perform multi-source BFS
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        max_distance = -1
        
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
                    # Mark as visited by setting it to the current distance + 1
                    grid[nx][ny] = grid[x][y] + 1
                    max_distance = grid[nx][ny] - 1
                    queue.append((nx, ny))
        
        return max_distance