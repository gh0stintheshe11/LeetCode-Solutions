class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        
        dp = [[[0] * k for _ in range(n)] for _ in range(m)]
        dp[0][0][grid[0][0] % k] = 1

        for i in range(m):
            for j in range(n):
                for r in range(k):
                    if i > 0:
                        new_r = (r + grid[i][j]) % k
                        dp[i][j][new_r] = (dp[i][j][new_r] + dp[i-1][j][r]) % MOD
                    if j > 0:
                        new_r = (r + grid[i][j]) % k
                        dp[i][j][new_r] = (dp[i][j][new_r] + dp[i][j-1][r]) % MOD

        return dp[m-1][n-1][0]