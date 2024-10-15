from typing import List
from math import gcd

class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        if len(stockPrices) <= 1:
            return 0

        stockPrices.sort()  # Sort by day increasing
        count = 0
        
        for i in range(1, len(stockPrices) - 1):
            x1, y1 = stockPrices[i - 1]
            x2, y2 = stockPrices[i]
            x3, y3 = stockPrices[i + 1]
            
            # Calculate the slope between (x1, y1) and (x2, y2) using cross product
            dy1 = y2 - y1
            dx1 = x2 - x1
            dy2 = y3 - y2
            dx2 = x3 - x2
            
            # Simplify slopes using cross product to avoid precision issues
            # (dy1/dx1) == (dy2/dx2) => dy1 * dx2 == dy2 * dx1
            if dy1 * dx2 != dy2 * dx1:
                count += 1
        
        return count + 1