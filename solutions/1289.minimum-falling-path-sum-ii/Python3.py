from typing import List

class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # DP initialization, we'll use the first row as initial costs.
        dp = grid[0]
        
        for i in range(1, n):
            # Current row's cost initialization
            current_row = [float('inf')] * n
            # Get the minimum and second minimum value of the previous row's dp array
            min1 = min2 = float('inf')
            for j in range(n):
                if dp[j] < min1:
                    min2 = min1
                    min1 = dp[j]
                elif dp[j] < min2:
                    min2 = dp[j]
                    
            # Calculate cost for the current row
            for j in range(n):
                # If current column is minimum, add the second minimum, else add the minimum
                if dp[j] == min1:
                    current_row[j] = grid[i][j] + min2
                else:
                    current_row[j] = grid[i][j] + min1
                    
            # Update dp to be current_row for next iteration
            dp = current_row
        
        # The answer is the minimum value in the last row of dp array
        return min(dp)