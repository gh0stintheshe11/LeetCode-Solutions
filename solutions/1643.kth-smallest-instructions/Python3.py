from typing import List
from math import comb

class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        row, column = destination
        total_steps = row + column
        result = []
        
        for _ in range(total_steps):
            if column > 0:
                count_h = comb(row + column - 1, row)
                if k <= count_h:
                    result.append('H')
                    column -= 1
                else:
                    result.append('V')
                    row -= 1
                    k -= count_h
            else:
                result.append('V')
                row -= 1
        
        return ''.join(result)