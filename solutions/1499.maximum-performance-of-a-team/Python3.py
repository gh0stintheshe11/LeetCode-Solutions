from typing import List
import heapq

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        engineers = sorted(zip(efficiency, speed), reverse=True)
        max_perf = 0
        speed_sum = 0
        min_heap = []

        for eff, spd in engineers:
            if len(min_heap) == k:
                speed_sum -= heapq.heappop(min_heap)
            heapq.heappush(min_heap, spd)
            speed_sum += spd
            max_perf = max(max_perf, speed_sum * eff)
        
        return max_perf % (10**9 + 7)