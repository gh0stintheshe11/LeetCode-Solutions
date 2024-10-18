class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        res = 0
        
        prefix = [[0] * (m + 1) for _ in range(n + 1)]
        hasX = [[False] * (m + 1) for _ in range(n + 1)]
        
        for i in range(n):
            for j in range(m):
                prefix[i + 1][j + 1] = prefix[i + 1][j] + prefix[i][j + 1] - prefix[i][j]
                hasX[i + 1][j + 1] = hasX[i + 1][j] or hasX[i][j + 1] or grid[i][j] == 'X'
                if grid[i][j] == 'X':
                    prefix[i + 1][j + 1] += 1
                if grid[i][j] == 'Y':
                    prefix[i + 1][j + 1] -= 1
                if prefix[i + 1][j + 1] == 0 and hasX[i + 1][j + 1]:
                    res += 1
        
        return res