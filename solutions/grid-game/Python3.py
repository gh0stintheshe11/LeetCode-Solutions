class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        
        # Compute prefix sums for both rows
        prefix_row1 = [0] * (n + 1)
        prefix_row2 = [0] * (n + 1)
        
        for i in range(1, n + 1):
            prefix_row1[i] = prefix_row1[i - 1] + grid[0][i - 1]
            prefix_row2[i] = prefix_row2[i - 1] + grid[1][i - 1]
        
        min_second_robot_points = float('inf')
        
        # Evaluate the maximum points the second robot can collect if the first
        # robot switches rows after each column index i
        for i in range(1, n + 1):
            # Points collected in row1 from i to n
            top_path_remainder = prefix_row1[n] - prefix_row1[i]
            # Points collected in row2 from 0 to i-1
            bottom_path_remainder = prefix_row2[i - 1] 
            
            # Second robot collects the max of two paths
            second_robot_points = max(top_path_remainder, bottom_path_remainder)
            # We want to minimize the maximum points that can be collected
            min_second_robot_points = min(min_second_robot_points, second_robot_points)
        
        return min_second_robot_points