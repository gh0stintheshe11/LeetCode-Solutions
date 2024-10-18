class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def is_magic(g):
            return sorted(g) == list(range(1, 10)) and \
                   (g[0] + g[1] + g[2] == g[3] + g[4] + g[5] == g[6] + g[7] + g[8] == 15 and
                    g[0] + g[3] + g[6] == g[1] + g[4] + g[7] == g[2] + g[5] + g[8] == 15 and
                    g[0] + g[4] + g[8] == g[2] + g[4] + g[6] == 15)

        rows, cols = len(grid), len(grid[0])
        count = 0

        for r in range(rows - 2):
            for c in range(cols - 2):
                g = [grid[r + i][c + j] for i in range(3) for j in range(3)]
                if is_magic(g):
                    count += 1

        return count