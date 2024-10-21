import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i: [] for i in range(1, n + 1)}
        for u, v, w in times:
            graph[u].append((v, w))
        
        min_heap = [(0, k)]
        visited = set()
        t = 0
        
        while min_heap:
            w1, n1 = heapq.heappop(min_heap)
            if n1 in visited:
                continue
            visited.add(n1)
            t = max(t, w1)
            
            for n2, w2 in graph[n1]:
                if n2 not in visited:
                    heapq.heappush(min_heap, (w1 + w2, n2))
                    
        return t if len(visited) == n else -1