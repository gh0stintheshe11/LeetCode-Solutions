from typing import List
import math

class Solution:
    def numPoints(self, darts: List[List[int]], r: int) -> int:
        def count_points(xc: float, yc: float) -> int:
            count = 0
            for x, y in darts:
                if (x - xc) ** 2 + (y - yc) ** 2 <= r * r + 1e-7:
                    count += 1
            return count
        
        def get_circle_centers(x1: int, y1: int, x2: int, y2: int):
            d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            if d > 2 * r:
                return []
            mid_x = (x1 + x2) / 2
            mid_y = (y1 + y2) / 2
            offset = math.sqrt(r ** 2 - (d / 2) ** 2)
            angle = math.atan2(y2 - y1, x2 - x1)
            offset_x = offset * math.cos(angle + math.pi / 2)
            offset_y = offset * math.sin(angle + math.pi / 2)
            return [(mid_x + offset_x, mid_y + offset_y), (mid_x - offset_x, mid_y - offset_y)]
        
        max_darts = 1
        n = len(darts)
        
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = darts[i]
                x2, y2 = darts[j]
                for xc, yc in get_circle_centers(x1, y1, x2, y2):
                    max_darts = max(max_darts, count_points(xc, yc))
        
        return max_darts