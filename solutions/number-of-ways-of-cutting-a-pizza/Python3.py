from typing import List

class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        MOD = 10**9 + 7
        rows, cols = len(pizza), len(pizza[0])
        
        # Precompute the number of apples in submatrices using a prefix sum array
        apples = [[0] * (cols + 1) for _ in range(rows + 1)]
        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                apples[r][c] = (1 if pizza[r][c] == 'A' else 0) + apples[r + 1][c] + apples[r][c + 1] - apples[r + 1][c + 1]
        
        # Memoization table
        dp = [[[-1] * k for _ in range(cols)] for _ in range(rows)]
        
        def has_apple(r1, c1, r2, c2):
            return apples[r1][c1] - apples[r2][c1] - apples[r1][c2] + apples[r2][c2] > 0
        
        def dfs(r, c, cuts):
            if cuts == 0:
                return 1 if has_apple(r, c, rows, cols) else 0
            if dp[r][c][cuts] != -1:
                return dp[r][c][cuts]
            
            ways = 0
            # Try horizontal cuts
            for nr in range(r + 1, rows):
                if has_apple(r, c, nr, cols):
                    ways = (ways + dfs(nr, c, cuts - 1)) % MOD
            # Try vertical cuts
            for nc in range(c + 1, cols):
                if has_apple(r, c, rows, nc):
                    ways = (ways + dfs(r, nc, cuts - 1)) % MOD
            
            dp[r][c][cuts] = ways
            return ways
        
        return dfs(0, 0, k - 1)