from typing import List

class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        # Step 1: Find the minimum element in each row
        min_in_rows = [min(row) for row in matrix]
        
        # Step 2: Find the maximum element in each column
        max_in_columns = [max(col) for col in zip(*matrix)]
        
        # Step 3: Find the lucky numbers
        lucky_numbers = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == min_in_rows[i] and matrix[i][j] == max_in_columns[j]:
                    lucky_numbers.append(matrix[i][j])
        
        return lucky_numbers