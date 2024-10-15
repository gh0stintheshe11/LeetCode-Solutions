class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        
        # Initialize the previous_row with the values in the first row of points
        prev_row = points[0]
        
        for i in range(1, m):
            left_max = [0] * n
            right_max = [0] * n
            
            # Calculate left_max
            left_max[0] = prev_row[0]
            for j in range(1, n):
                left_max[j] = max(left_max[j-1] - 1, prev_row[j])
            
            # Calculate right_max
            right_max[n-1] = prev_row[n-1]
            for j in range(n-2, -1, -1):
                right_max[j] = max(right_max[j+1] - 1, prev_row[j])
            
            # Update current row scores using left_max and right_max
            for j in range(n):
                points[i][j] += max(left_max[j], right_max[j])
            
            # Move to the next row
            prev_row = points[i]
        
        # Return the max value from the last row
        return max(prev_row)