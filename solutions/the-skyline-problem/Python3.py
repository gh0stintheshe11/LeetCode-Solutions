from heapq import heappush, heappop
from typing import List

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # Collect all the critical points
        points = []
        for left, right, height in buildings:
            points.append((left, -height, right))
            points.append((right, 0, 0))
        
        # Sort the points
        points.sort()
        
        # Result and heap to store the heights of the buildings
        result = [[0, 0]]
        heights = [(0, float("inf"))]
        
        # Process each point
        for x, h, r in points:
            if h != 0:
                heappush(heights, (h, r))
            while heights[0][1] <= x:
                heappop(heights)
            max_height = -heights[0][0]
            if result[-1][1] != max_height:
                result.append([x, max_height])

        return result[1:]