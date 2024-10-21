from collections import deque
from typing import List

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return
        
        INF = 2147483647
        m, n = len(rooms), len(rooms[0])
        queue = deque()

        # Collect all the gates' positions
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i, j))
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # BFS to find the shortest path to the nearest gate for each empty room
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and rooms[nx][ny] == INF:
                    rooms[nx][ny] = rooms[x][y] + 1
                    queue.append((nx, ny))