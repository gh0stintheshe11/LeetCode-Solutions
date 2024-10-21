from heapq import heappop, heappush
from typing import List, Tuple
import sys

class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        n = len(passingFees)
        graph = {i: [] for i in range(n)}
        for u, v, t in edges:
            graph[u].append((v, t))
            graph[v].append((u, t))

        # Dijkstra-like priority queue: (cost, time, node)
        pq = [(passingFees[0], 0, 0)]
        # Min cost to reach each city with given time
        min_cost_time = {i: [sys.maxsize] * (maxTime + 1) for i in range(n)}
        min_cost_time[0][0] = passingFees[0]

        while pq:
            cost, time, node = heappop(pq)
            if node == n - 1:
                return cost
            for nei, t in graph[node]:
                new_time = time + t
                if new_time <= maxTime:
                    new_cost = cost + passingFees[nei]
                    if new_cost < min_cost_time[nei][new_time]:
                        min_cost_time[nei][new_time] = new_cost
                        heappush(pq, (new_cost, new_time, nei))

        return -1