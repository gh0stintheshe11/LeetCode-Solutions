from typing import List
from collections import defaultdict

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        
        # Compute prefix sums for each row
        for r in range(rows):
            for c in range(1, cols):
                matrix[r][c] += matrix[r][c-1]
        
        count = 0
        
        # Enumerate all pairs of columns
        for c1 in range(cols):
            for c2 in range(c1, cols):
                sums = defaultdict(int)
                sums[0] = 1
                current_sum = 0
                
                # Calculate sums of submatrices between columns c1 and c2 for all rows
                for r in range(rows):
                    current_sum += matrix[r][c2] - (matrix[r][c1-1] if c1 > 0 else 0)
                    count += sums[current_sum - target]
                    sums[current_sum] += 1
        
        return count