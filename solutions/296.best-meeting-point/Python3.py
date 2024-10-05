from typing import List

class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        def get_min_distance_1d(points):
            points.sort()
            i, j = 0, len(points) - 1
            distance = 0
            while i < j:
                distance += points[j] - points[i]
                i += 1
                j -= 1
            return distance
        
        m, n = len(grid), len(grid[0])
        rows = []
        cols = []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows.append(i)
                    
        for j in range(n):
            for i in range(m):
                if grid[i][j] == 1:
                    cols.append(j)

        return get_min_distance_1d(rows) + get_min_distance_1d(cols)