from typing import List

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(grid, x, y, visited):
            stack = [(x, y)]
            cells = []
            while stack:
                cx, cy = stack.pop()
                if (cx, cy) in visited:
                    continue
                visited.add((cx, cy))
                cells.append((cx, cy))
                for nx, ny in [(cx+1, cy), (cx-1, cy), (cx, cy+1), (cx, cy-1)]:
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1 and (nx, ny) not in visited:
                        stack.append((nx, ny))
            return cells
        
        visited2 = set()
        sub_island_count = 0
        
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1 and (i, j) not in visited2:
                    cells = dfs(grid2, i, j, visited2)
                    is_sub_island = all(grid1[x][y] == 1 for x, y in cells)
                    if is_sub_island:
                        sub_island_count += 1
        
        return sub_island_count
