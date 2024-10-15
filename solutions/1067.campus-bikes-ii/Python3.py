from typing import List

class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        from functools import lru_cache
        
        @lru_cache(None)
        def dp(pos, mask):
            if pos == len(workers):
                return 0
            minimum_distance = float('inf')
            for j in range(len(bikes)):
                if mask & (1 << j) == 0:
                    distance = abs(workers[pos][0] - bikes[j][0]) + abs(workers[pos][1] - bikes[j][1])
                    minimum_distance = min(minimum_distance, distance + dp(pos + 1, mask | (1 << j)))
            return minimum_distance
        
        return dp(0, 0)