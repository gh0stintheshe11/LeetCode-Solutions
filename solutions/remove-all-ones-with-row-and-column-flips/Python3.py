from typing import List

class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        for row in grid:
            if row != grid[0] and row != [1 - val for val in grid[0]]:
                return False
        return True