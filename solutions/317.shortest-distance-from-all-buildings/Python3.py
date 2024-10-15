from collections import deque
from typing import List, Tuple

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        totalDist = [[0] * n for _ in range(m)]
        reachCount = [[0] * n for _ in range(m)]
        buildingCount = sum(val == 1 for row in grid for val in row)

        def bfs(startRow: int, startCol: int) -> None:
            visited = [[False] * n for _ in range(m)]
            queue = deque([(startRow, startCol, 0)])
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            
            while queue:
                row, col, dist = queue.popleft()
                
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] == 0:
                        visited[nr][nc] = True
                        totalDist[nr][nc] += dist + 1
                        reachCount[nr][nc] += 1
                        queue.append((nr, nc, dist + 1))
        
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    bfs(row, col)
        
        minDist = float('inf')
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 0 and reachCount[row][col] == buildingCount:
                    minDist = min(minDist, totalDist[row][col])
        
        return minDist if minDist != float('inf') else -1