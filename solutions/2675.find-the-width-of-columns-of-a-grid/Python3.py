from typing import List

class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        n = len(grid[0])  # number of columns
        result = [0] * n
        
        for col in range(n):
            max_length = 0
            for row in grid:
                number_len = len(str(row[col]))
                max_length = max(max_length, number_len)
            result[col] = max_length
            
        return result