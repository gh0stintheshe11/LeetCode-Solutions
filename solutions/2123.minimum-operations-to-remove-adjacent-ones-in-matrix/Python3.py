from typing import List

class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        cnt = 0
        D = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Directions for traversing (up, down, left, right)
        
        # Initialize matching and visited arrays
        match = [[-1 for _ in range(n)] for _ in range(m)]
        vis = [[-1 for _ in range(n)] for _ in range(m)]

        def dfs(i: int, j: int, v: int) -> int:
            for di, dj in D:
                x, y = i + di, j + dj
                if 0 <= x < m and 0 <= y < n and grid[x][y] and vis[x][y] != v:
                    vis[x][y] = v
                    # Found an augmenting path
                    if match[x][y] == -1 or dfs(match[x][y] // n, match[x][y] % n, v):
                        match[x][y] = i * n + j
                        match[i][j] = x * n + y
                        return 1
            return 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and match[i][j] == -1:
                    cnt += dfs(i, j, i * n + j)
        
        return cnt