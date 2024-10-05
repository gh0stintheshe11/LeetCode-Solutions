class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        import collections
        
        def index(x, y):
            return x * n + y
        
        def neighbors(x, y):
            for i, j in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
                if 0 <= i < m and 0 <= j < n:
                    yield i, j
        
        def dfs(x, y):
            if not (0 <= x < m and 0 <= y < n and grid[x][y] == 1):
                return 0
            grid[x][y] = 2
            result = 1
            for i, j in neighbors(x, y):
                result += dfs(i, j)
            return result
        
        def is_connected_to_top(x, y):
            return x == 0 or any(0 <= i < m and 0 <= j < n and grid[i][j] == 2 for i, j in neighbors(x, y))
        
        m, n = len(grid), len(grid[0])
        result = [0] * len(hits)
        
        for x, y in hits:
            grid[x][y] -= 1
        
        for j in range(n):
            dfs(0, j)
        
        for k in range(len(hits) - 1, -1, -1):
            x, y = hits[k]
            grid[x][y] += 1
            if grid[x][y] == 1 and is_connected_to_top(x, y):
                result[k] = dfs(x, y) - 1
        
        return result