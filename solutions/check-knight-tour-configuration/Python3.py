from typing import List

class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        moves = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]

        # Start from the top-left corner
        if grid[0][0] != 0:
            return False
        
        # Create a mapping from visit order to position
        position_by_order = {}
        for r in range(n):
            for c in range(n):
                position_by_order[grid[r][c]] = (r, c)
        
        # Verify each step in the tour
        for step in range(n * n - 1):
            r1, c1 = position_by_order[step]
            r2, c2 = position_by_order[step + 1]
            
            # Check if the step is a valid knight move
            if not any(r1 + dr == r2 and c1 + dc == c2 for dr, dc in moves):
                return False
        
        return True