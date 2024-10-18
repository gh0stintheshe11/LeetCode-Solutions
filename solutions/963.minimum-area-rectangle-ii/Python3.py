from itertools import combinations
from collections import defaultdict

class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        # Map each pair of points to its midpoint and squared distance
        point_map = defaultdict(list)
        
        for (x1, y1), (x2, y2) in combinations(points, 2):
            midx, midy = (x1 + x2) / 2, (y1 + y2) / 2
            distance = (x1 - x2) ** 2 + (y1 - y2) ** 2
            point_map[(midx, midy, distance)].append((x1, y1, x2, y2))
        
        min_area = float('inf')
        
        for pairs in point_map.values():
            if len(pairs) > 1:
                for (x1, y1, x2, y2), (x3, y3, x4, y4) in combinations(pairs, 2):
                    # Calculate the area of the rectangle
                    d1 = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5
                    d2 = ((x1 - x4) ** 2 + (y1 - y4) ** 2) ** 0.5
                    area = d1 * d2
                    min_area = min(min_area, area)
        
        return min_area if min_area < float('inf') else 0