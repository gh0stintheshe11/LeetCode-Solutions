from typing import List

class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        answer = [[0] * n for _ in range(m)]
        
        # Helper to count distinct values on the diagonal from (r, c) towards (dr, dc)
        def count_distinct(r, c, dr, dc):
            seen = set()
            while 0 <= r < m and 0 <= c < n:
                seen.add(grid[r][c])
                r += dr
                c += dc
            return len(seen)

        # Compute the number of distinct elements on diagonals
        for r in range(m):
            for c in range(n):
                leftAbove = count_distinct(r - 1, c - 1, -1, -1)
                rightBelow = count_distinct(r + 1, c + 1, 1, 1)
                answer[r][c] = abs(leftAbove - rightBelow)

        return answer