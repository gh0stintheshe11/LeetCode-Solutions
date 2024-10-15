from typing import List
from itertools import combinations

class Solution:
    def goodSubsetofBinaryMatrix(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        
        # Check for a single zero row
        for i, row in enumerate(grid):
            if sum(row) == 0:
                return [i]
        
        # Check for a pair of rows that form a good subset
        # Using bitmask representation
        bit_mask_map = {tuple(row): i for i, row in enumerate(grid)}
        
        # We only need to check at most 2 rows due to constraints
        for row1, index1 in bit_mask_map.items():
            for row2, index2 in bit_mask_map.items():
                if index1 < index2:
                    # Check if the pair of rows fulfill the condition
                    if all(row1[k] + row2[k] <= 1 for k in range(n)):
                        return [index1, index2]
        
        return []