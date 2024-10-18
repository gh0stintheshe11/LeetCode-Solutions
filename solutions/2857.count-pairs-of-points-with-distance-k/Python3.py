from typing import List
from collections import defaultdict

class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        count = 0
        freq = defaultdict(int)
        
        for x1, y1 in coordinates:
            for x in range(k + 1):
                y = k - x
                x2 = x1 ^ x
                y2 = y1 ^ y
                count += freq[(x2, y2)]
            
            freq[(x1, y1)] += 1
        
        return count