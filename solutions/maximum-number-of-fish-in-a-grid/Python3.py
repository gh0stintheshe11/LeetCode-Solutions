from typing import List

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]

        def dfs(r: int, c: int) -> int:
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0 or visited[r][c]:
                return 0
            visited[r][c] = True
            fish_count = grid[r][c]
            # Explore all 4 directions
            fish_count += dfs(r + 1, c)
            fish_count += dfs(r - 1, c)
            fish_count += dfs(r, c + 1)
            fish_count += dfs(r, c - 1)
            return fish_count

        max_fish = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0 and not visited[i][j]:
                    max_fish = max(max_fish, dfs(i, j))
        
        return max_fish