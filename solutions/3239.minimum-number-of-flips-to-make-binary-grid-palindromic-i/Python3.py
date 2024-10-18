class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        from collections import defaultdict

        def get_flip_count(lst):
            n = len(lst)
            count = 0
            for i in range(n // 2):
                if lst[i] != lst[n - i - 1]:
                    count += 1
            return count

        # Flips needed to make all rows palindromic
        row_flips = 0
        for row in grid:
            row_flips += get_flip_count(row)

        m, n = len(grid), len(grid[0])
        
        # Flips needed to make all columns palindromic
        col_flips = 0
        for j in range(n):
            col = [grid[i][j] for i in range(m)]
            col_flips += get_flip_count(col)

        return min(row_flips, col_flips)