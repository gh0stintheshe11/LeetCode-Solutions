from typing import List
import heapq

class Solution:
    def shortestPathWithHops(self, n: int, edges: List[List[int]], s: int, d: int, k: int) -> int:
        graph = {}
        for u, v, w in edges:
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        pq = [(0, s, 0)]  # (current cost, node, used hops)
        dist = {}
        
        while pq:
            cost, node, hops = heapq.heappop(pq)

            if (node, hops) in dist and dist[(node, hops)] <= cost:
                continue
            dist[(node, hops)] = cost

            if node == d:  # Early exit if we've reached destination
                return cost

            for neighbor, weight in graph[node]:
                # Normal edge without hopping
                if (neighbor, hops) not in dist or cost + weight < dist[(neighbor, hops)]:
                    heapq.heappush(pq, (cost + weight, neighbor, hops))

                # Hopped edge
                if hops < k:
                    if (neighbor, hops + 1) not in dist or cost < dist[(neighbor, hops + 1)]:
                        heapq.heappush(pq, (cost, neighbor, hops + 1))
        
        return -1