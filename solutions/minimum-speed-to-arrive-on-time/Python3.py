from math import ceil
from typing import List

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def can_arrive_on_time(speed: int) -> bool:
            total_time = 0.0
            for i in range(len(dist) - 1):
                total_time += ceil(dist[i] / speed)
            total_time += dist[-1] / speed
            return total_time <= hour
        
        left, right = 1, 10**7
        result = -1
        
        while left <= right:
            mid = (left + right) // 2
            if can_arrive_on_time(mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return result
