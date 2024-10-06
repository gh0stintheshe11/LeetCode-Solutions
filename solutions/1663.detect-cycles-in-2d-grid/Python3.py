class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        def dfs(x, y, px, py):
            if visited[x][y]:
                return True
            
            visited[x][y] = True
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == grid[x][y]:
                    if (nx, ny) != (px, py):
                        if dfs(nx, ny, x, y):
                            return True
            return False
        
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        for x in range(m):
            for y in range(n):
                if not visited[x][y]:
                    if dfs(x, y, -1, -1):
                        return True
        return False