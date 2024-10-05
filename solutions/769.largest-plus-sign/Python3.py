class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        grid = [[n] * n for _ in range(n)]
        for x, y in mines:
            grid[x][y] = 0
        
        for i in range(n):
            l, r, u, d = [0] * n, [0] * n, [0] * n, [0] * n
            for j in range(n):
                l[j] = (l[j-1] if j > 0 else 0) + 1 if grid[i][j] != 0 else 0
                r[n-1-j] = (r[n-j] if j > 0 else 0) + 1 if grid[i][n-1-j] != 0 else 0
                u[j] = (u[j-1] if j > 0 else 0) + 1 if grid[j][i] != 0 else 0
                d[n-1-j] = (d[n-j] if j > 0 else 0) + 1 if grid[n-1-j][i] != 0 else 0

            for j in range(n):
                grid[i][j] = min(grid[i][j], l[j], r[j])
                grid[j][i] = min(grid[j][i], u[j], d[j])
        
        result = 0
        for i in range(n):
            for j in range(n):
                result = max(result, grid[i][j])
        return result