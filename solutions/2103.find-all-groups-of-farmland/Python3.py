from typing import List

class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        def dfs(r, c):
            stack = [(r, c)]
            farm_area = []
            while stack:
                x, y = stack.pop()
                if 0 <= x < m and 0 <= y < n and land[x][y] == 1:
                    land[x][y] = 0
                    farm_area.append((x, y))
                    stack.extend([(x+1, y), (x-1, y), (x, y+1), (x, y-1)])
            return farm_area
        
        m, n = len(land), len(land[0])
        result = []

        for i in range(m):
            for j in range(n):
                if land[i][j] == 1:
                    farm_area = dfs(i, j)
                    top_left = min(farm_area)
                    bottom_right = max(farm_area)
                    result.append([top_left[0], top_left[1], bottom_right[0], bottom_right[1]])
        
        return result