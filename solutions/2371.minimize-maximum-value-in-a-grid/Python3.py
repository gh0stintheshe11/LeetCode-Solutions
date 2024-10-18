class Solution:
    def minScore(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        pos = [(grid[i][j], i, j) for i in range(m) for j in range(n)]
        pos.sort()
        
        row_max = [0] * m
        col_max = [0] * n
        result = [[0] * n for _ in range(m)]
        
        for _, i, j in pos:
            result[i][j] = max(row_max[i], col_max[j]) + 1
            row_max[i] = result[i][j]
            col_max[j] = result[i][j]
        
        return result