from typing import List

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        def dfs(x, y, direction):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 0:
                return
            grid[x][y] = 0
            path_signature.append(direction)
            dfs(x + 1, y, 'd')  # move down
            dfs(x - 1, y, 'u')  # move up
            dfs(x, y + 1, 'r')  # move right
            dfs(x, y - 1, 'l')  # move left
            path_signature.append('b')  # backtrack

        unique_islands = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    path_signature = []
                    dfs(i, j, 's')  # start direction
                    unique_islands.add(tuple(path_signature))
                    
        return len(unique_islands)