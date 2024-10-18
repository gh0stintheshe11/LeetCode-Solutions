from collections import deque
from typing import List, Tuple

class Solution:
    def minimumSeconds(self, land: List[List[str]]) -> int:
        def is_valid(x: int, y: int, n: int, m: int) -> bool:
            return 0 <= x < n and 0 <= y < m
        
        def bfs_flood_time() -> List[List[int]]:
            flood_time = [[float('inf')] * m for _ in range(n)]
            queue = deque()
            
            for i in range(n):
                for j in range(m):
                    if land[i][j] == '*':
                        flood_time[i][j] = 0
                        queue.append((i, j, 0))
            
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            while queue:
                x, y, t = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if is_valid(nx, ny, n, m) and land[nx][ny] == '.' and flood_time[nx][ny] > t + 1:
                        flood_time[nx][ny] = t + 1
                        queue.append((nx, ny, t + 1))
            return flood_time
        
        def bfs_minimum_time(flood_time: List[List[int]]) -> int:
            queue = deque([(start_x, start_y, 0)])
            visited = [[False] * m for _ in range(n)]
            visited[start_x][start_y] = True
            
            while queue:
                x, y, t = queue.popleft()
                if (x, y) == (dest_x, dest_y):
                    return t
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if is_valid(nx, ny, n, m) and not visited[nx][ny] and land[nx][ny] != 'X':
                        if flood_time[nx][ny] > t + 1:
                            visited[nx][ny] = True
                            queue.append((nx, ny, t + 1))
            return -1

        n, m = len(land), len(land[0])
        start_x = start_y = dest_x = dest_y = -1

        for i in range(n):
            for j in range(m):
                if land[i][j] == 'S':
                    start_x, start_y = i, j
                elif land[i][j] == 'D':
                    dest_x, dest_y = i, j
        
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        flood_time = bfs_flood_time()
        return bfs_minimum_time(flood_time)