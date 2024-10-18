from typing import List

class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        
        # Directions for moving up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Memoization table
        memo = [[-1] * n for _ in range(m)]
        
        def dfs(x, y):
            # If already computed, return the stored result
            if memo[x][y] != -1:
                return memo[x][y]
            
            # Start with the path of length 1 (the cell itself)
            count = 1
            
            # Explore all 4 possible directions
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] > grid[x][y]:
                    count += dfs(nx, ny)
                    count %= MOD
            
            # Store the result in memo table
            memo[x][y] = count
            return count
        
        # Total number of increasing paths
        total_paths = 0
        
        # Compute the number of increasing paths starting from each cell
        for i in range(m):
            for j in range(n):
                total_paths += dfs(i, j)
                total_paths %= MOD
        
        return total_paths