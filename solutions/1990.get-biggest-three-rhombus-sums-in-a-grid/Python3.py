from typing import List

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        sums = set()
        
        def add_rhombus_sum(x, y, size):
            total = 0
            if size == 0:
                total = grid[x][y]
            else:
                for i in range(size):
                    total += grid[x - size + i][y + i]    # Top right to right
                    total += grid[x + i][y + size - i]    # Right to bottom
                    total += grid[x + size - i][y - i]    # Bottom to left
                    total += grid[x - i][y - size + i]    # Left to top
            sums.add(total)

        for i in range(m):
            for j in range(n):
                add_rhombus_sum(i, j, 0)  # Add single cell rhombus
                max_size = min(i, j, m - i - 1, n - j - 1)
                for size in range(1, max_size + 1):
                    add_rhombus_sum(i, j, size)

        return sorted(sums, reverse=True)[:3]