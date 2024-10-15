class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        # Count the number of consecutive ones in each column
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i-1][j]
        
        max_area = 0
        # Calculate the maximum submatrix area for each row
        for row in matrix:
            # Sort the row in descending order to simulate rearranging columns
            row.sort(reverse=True)
            # Area calculation for the possible largest rectangle in this configuration
            for j in range(len(row)):
                max_area = max(max_area, row[j] * (j + 1))
        
        return max_area