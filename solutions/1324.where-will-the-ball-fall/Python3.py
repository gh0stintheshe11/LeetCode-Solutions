class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        def drop_ball(column):
            for row in range(len(grid)):
                direction = grid[row][column]
                next_column = column + direction
                if next_column < 0 or next_column >= len(grid[0]) or grid[row][next_column] != direction:
                    return -1
                column = next_column
            return column

        return [drop_ball(col) for col in range(len(grid[0]))]