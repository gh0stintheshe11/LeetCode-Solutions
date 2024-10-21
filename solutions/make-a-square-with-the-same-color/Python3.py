class Solution:
    def canMakeSquare(self, grid: list[list[str]]) -> bool:
        for i in range(2):
            for j in range(2):
                subgrid = [grid[i][j], grid[i][j+1], grid[i+1][j], grid[i+1][j+1]]
                if subgrid.count('B') != 2:
                    return True
        return False