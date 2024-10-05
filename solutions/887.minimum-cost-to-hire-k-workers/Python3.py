from typing import List
import heapq

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers = sorted((w / q, q) for w, q in zip(wage, quality))
        heap = []
        total_quality = 0
        min_cost = float('inf')
        
        for ratio, q in workers:
            heapq.heappush(heap, -q)
            total_quality += q
            
            if len(heap) > k:
                total_quality += heapq.heappop(heap)
                
            if len(heap) == k:
                min_cost = min(min_cost, total_quality * ratio)
        
        return min_cost