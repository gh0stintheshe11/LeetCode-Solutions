from typing import List
from collections import defaultdict
from math import gcd

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def slope(p1, p2):
            dx = p1[0] - p2[0]
            dy = p1[1] - p2[1]
            if dx == 0:
                return (0, p1[0])
            if dy == 0:
                return (p1[1], 0)
            d = gcd(dx, dy)
            return (dy // d, dx // d)
        
        max_points = 1
        n = len(points)
        if n <= 1:
            return n
        
        for i in range(n):
            slopes = defaultdict(int)
            for j in range(n):
                if i != j:
                    slopes[slope(points[i], points[j])] += 1
            max_points = max(max_points, max(slopes.values(), default=0) + 1)
        
        return max_points