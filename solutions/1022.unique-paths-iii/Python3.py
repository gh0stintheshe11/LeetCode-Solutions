class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def dfs(x, y, remain):
            if not (0 <= x < m and 0 <= y < n) or grid[x][y] == -1:
                return 0
            if grid[x][y] == 2:
                return remain == 0
            grid[x][y] = -1
            paths = dfs(x + 1, y, remain - 1) + dfs(x - 1, y, remain - 1) + dfs(x, y + 1, remain - 1) + dfs(x, y - 1, remain - 1)
            grid[x][y] = 0
            return paths
        
        m, n = len(grid), len(grid[0])
        start_x = start_y = -1
        empty_count = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start_x, start_y = i, j
                elif grid[i][j] == 0:
                    empty_count += 1
        
        return dfs(start_x, start_y, empty_count + 1)