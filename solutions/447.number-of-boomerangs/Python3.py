from typing import List
from collections import defaultdict

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        def getDistance(p1, p2):
            return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
        
        n = len(points)
        result = 0
        
        for i in range(n):
            distances = defaultdict(int)
            for j in range(n):
                if i != j:
                    dist = getDistance(points[i], points[j])
                    distances[dist] += 1
            
            for count in distances.values():
                if count > 1:
                    result += count * (count - 1)
        
        return result