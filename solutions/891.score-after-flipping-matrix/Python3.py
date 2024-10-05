class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # Step 1: Ensure all rows start with 1
        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] ^= 1
        
        # Step 2: For each column, maximize the number of 1's
        for j in range(n):
            count_1 = sum(grid[i][j] for i in range(m))
            if count_1 < m - count_1:
                for i in range(m):
                    grid[i][j] ^= 1
        
        # Calculate the final score
        score = 0
        for i in range(m):
            row_value = 0
            for j in range(n):
                row_value = row_value * 2 + grid[i][j]
            score += row_value
        
        return score