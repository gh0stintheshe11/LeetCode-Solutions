from typing import List

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        from collections import defaultdict
        
        reserved = defaultdict(set)
        for row, col in reservedSeats:
            reserved[row].add(col)

        result = 0
        for row in reserved:
            current = 0
            occupied = reserved[row]
            
            # Check possibility for each bloc
            left = all(pos not in occupied for pos in range(2, 6))
            middle = all(pos not in occupied for pos in range(4, 8))
            right = all(pos not in occupied for pos in range(6, 10))
            
            if left:
                current += 1
            if right:
                current += 1
            if middle and current == 0:  # Only if no left or right are occupied, use the middle
                current += 1

            result += current
        
        # Rows that are not in the reserved list can fully accommodate two families
        empty_rows = n - len(reserved)
        result += empty_rows * 2
        
        return result