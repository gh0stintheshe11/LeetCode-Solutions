class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        mod = 12345
        
        pre, suf = [1], [1]
        for i in range(m):
            for j in range(n):
                pre.append((pre[-1] * grid[i][j]) % mod)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                suf.append((suf[-1] * grid[i][j]) % mod)
        suf.reverse()
        for i in range(m):
            for j in range(n):
                ans = i * n + j
                grid[i][j] = (pre[ans] * suf[ans + 1]) % mod
        return grid