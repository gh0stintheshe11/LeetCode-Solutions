from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        flat = [num for row in grid for num in row]
        flat.sort()
        n = len(flat)
        
        # Check if it's possible
        remainder = flat[0] % x
        for num in flat:
            if num % x != remainder:
                return -1
        
        # Find median
        median = flat[n // 2]
        
        # Calculate the total operations required
        operations = sum(abs(num - median) // x for num in flat)
        
        return operations