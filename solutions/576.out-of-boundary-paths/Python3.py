class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7
        dp = [[[0] * (maxMove+1) for _ in range(n)] for _ in range(m)]
        dp[startRow][startColumn][0] = 1
        
        result = 0
        for moves in range(1, maxMove + 1):
            for r in range(m):
                for c in range(n):
                    if dp[r][c][moves - 1] > 0:
                        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < m and 0 <= nc < n:
                                dp[nr][nc][moves] = (dp[nr][nc][moves] + dp[r][c][moves - 1]) % MOD
                            else:
                                result = (result + dp[r][c][moves - 1]) % MOD
        
        return result