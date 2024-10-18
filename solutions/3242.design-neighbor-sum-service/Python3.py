class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.position_map = {}
        n = len(grid)
        for i in range(n):
            for j in range(n):
                value = grid[i][j]
                self.position_map[value] = (i, j)

    def adjacentSum(self, value: int) -> int:
        i, j = self.position_map[value]
        n = len(self.grid)
        adj_sum = 0
        # Check top, bottom, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n:
                adj_sum += self.grid[ni][nj]
        return adj_sum

    def diagonalSum(self, value: int) -> int:
        i, j = self.position_map[value]
        n = len(self.grid)
        diag_sum = 0
        # Check top-left, top-right, bottom-left, bottom-right
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n:
                diag_sum += self.grid[ni][nj]
        return diag_sum