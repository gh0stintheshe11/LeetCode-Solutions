class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = grid[0][:]

        for i in range(1, m):
            new_dp = [float('inf')] * n
            for j in range(n):
                for k in range(n):
                    new_dp[k] = min(new_dp[k], dp[j] + moveCost[grid[i-1][j]][k] + grid[i][k])
            dp = new_dp
        
        return min(dp)