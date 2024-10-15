from heapq import heappush, heappop
from typing import List

class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        max_heap = []  # max heap to maintain size k
        results = []
        
        for x, y in queries:
            distance = abs(x) + abs(y)
            if len(max_heap) < k:
                heappush(max_heap, -distance)
            else:
                if -max_heap[0] > distance:
                    heappop(max_heap)
                    heappush(max_heap, -distance)
            
            if len(max_heap) < k:
                results.append(-1)
            else:
                results.append(-max_heap[0])
        
        return results