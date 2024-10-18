from collections import deque
from typing import List

class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        # Use a deque to store pairs (yi - xi, xi)
        deque_y_minus_x = deque()
        max_value = float('-inf')
        
        for xj, yj in points:
            # Remove points from the deque that do not satisfy the condition |xi - xj| <= k
            while deque_y_minus_x and xj - deque_y_minus_x[0][1] > k:
                deque_y_minus_x.popleft()
            
            # If the deque is not empty, calculate the potential maximum value
            if deque_y_minus_x:
                max_value = max(max_value, yj + xj + deque_y_minus_x[0][0])
            
            # Calculate yi - xi for the current point
            yi_minus_xi = yj - xj
            
            # Maintain deque in decreasing order of yi - xi
            while deque_y_minus_x and deque_y_minus_x[-1][0] <= yi_minus_xi:
                deque_y_minus_x.pop()
            
            # Add current point to deque
            deque_y_minus_x.append((yi_minus_xi, xj))
        
        return max_value