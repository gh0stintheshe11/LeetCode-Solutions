from collections import defaultdict
from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row_counts = defaultdict(int)
        
        # Count the frequency of each row as a tuple
        for row in grid:
            row_counts[tuple(row)] += 1
        
        equal_pairs = 0
        
        # Compare each column converted to a tuple with the row_counts
        for col in range(n):
            column_tuple = tuple(grid[row][col] for row in range(n))
            equal_pairs += row_counts[column_tuple]
        
        return equal_pairs