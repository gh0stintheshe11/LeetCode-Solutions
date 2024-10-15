from typing import List
from collections import deque

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # BFS to calculate the minimum distance of each cell to the nearest thief
        dist = [[float('inf')] * n for _ in range(n)]
        queue = deque()
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    queue.append((r, c))
                    dist[r][c] = 0
        
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == float('inf'):
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))
        
        # Use binary search to find the maximum safeness factor
        def canReach(safe_factor):
            if dist[0][0] < safe_factor or dist[n-1][n-1] < safe_factor:
                return False
            
            visited = [[False] * n for _ in range(n)]
            queue = deque([(0, 0)])
            visited[0][0] = True
            
            while queue:
                x, y = queue.popleft()
                if (x, y) == (n-1, n-1):
                    return True
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and dist[nx][ny] >= safe_factor:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
            return False
        
        left, right = 0, n * 2
        while left < right:
            mid = (left + right + 1) // 2
            if canReach(mid):
                left = mid
            else:
                right = mid - 1
        
        return left