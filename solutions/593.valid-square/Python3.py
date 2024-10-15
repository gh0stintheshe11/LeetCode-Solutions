import itertools
from typing import List

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def dist_squared(point1, point2):
            return (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2
        
        points = [p1, p2, p3, p4]
        distances = [dist_squared(points[i], points[j]) for i, j in itertools.combinations(range(4), 2)]
        distances.sort()
        
        return 0 < distances[0] == distances[1] == distances[2] == distances[3] and distances[4] == distances[5]