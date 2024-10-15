class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        # Initialize a 3D DP table with infinite cost
        dp = [[[[float('inf')] * n for _ in range(m)] for _ in range(n)] for _ in range(m)]
        
        # Base case when the piece is already 1x1
        for i in range(m):
            for j in range(n):
                dp[i][j][i][j] = 0

        # Iterate over all possible starting and ending points for the rectangle
        for sx in range(m - 1, -1, -1):
            for sy in range(n - 1, -1, -1):
                for tx in range(sx, m):
                    for ty in range(sy, n):
                        # Try making a horizontal cut
                        if tx > sx:
                            for x in range(sx, tx):
                                dp[sx][sy][tx][ty] = min(dp[sx][sy][tx][ty],
                                                         horizontalCut[x] + dp[sx][sy][x][ty] + dp[x + 1][sy][tx][ty])
                        # Try making a vertical cut
                        if ty > sy:
                            for y in range(sy, ty):
                                dp[sx][sy][tx][ty] = min(dp[sx][sy][tx][ty],
                                                         verticalCut[y] + dp[sx][sy][tx][y] + dp[sx][y + 1][tx][ty])
        
        # Return minimum cost to cut the whole cake from (0,0) to (m-1, n-1)
        return dp[0][0][m-1][n-1]