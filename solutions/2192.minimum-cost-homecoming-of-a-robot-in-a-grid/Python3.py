from typing import List

class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        startRow, startCol = startPos
        homeRow, homeCol = homePos
        
        total_cost = 0
        
        # Calculate the cost for row movements
        if startRow < homeRow:
            for r in range(startRow + 1, homeRow + 1):
                total_cost += rowCosts[r]
        else:
            for r in range(startRow - 1, homeRow - 1, -1):
                total_cost += rowCosts[r]
        
        # Calculate the cost for column movements
        if startCol < homeCol:
            for c in range(startCol + 1, homeCol + 1):
                total_cost += colCosts[c]
        else:
            for c in range(startCol - 1, homeCol - 1, -1):
                total_cost += colCosts[c]
        
        return total_cost