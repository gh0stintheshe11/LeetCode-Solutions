from typing import List

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        
        # Maps to store positions of each value in the matrix
        value_to_position = {}
        
        for r in range(m):
            for c in range(n):
                value_to_position[mat[r][c]] = (r, c)
        
        # Arrays to track the count of painted cells per row and column
        row_count = [0] * m
        col_count = [0] * n
        
        # Iterate through arr and paint accordingly
        for i, num in enumerate(arr):
            r, c = value_to_position[num]
            row_count[r] += 1
            col_count[c] += 1
            
            # Check if either row or column is fully painted
            if row_count[r] == n or col_count[c] == m:
                return i

        return -1