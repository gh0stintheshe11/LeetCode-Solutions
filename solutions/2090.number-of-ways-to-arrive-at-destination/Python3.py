import heapq
from typing import List

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7

        # Create graph as adjacency list
        graph = {i: [] for i in range(n)}
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))
        
        # Dijkstra's algorithm to find shortest paths from node 0
        dist = [float('inf')] * n
        dist[0] = 0
        ways = [0] * n
        ways[0] = 1
        
        min_heap = [(0, 0)]  # (distance, node)
        
        while min_heap:
            current_time, u = heapq.heappop(min_heap)
            
            if current_time > dist[u]:
                continue
            
            for v, time in graph[u]:
                if dist[u] + time < dist[v]:
                    dist[v] = dist[u] + time
                    ways[v] = ways[u]
                    heapq.heappush(min_heap, (dist[v], v))
                elif dist[u] + time == dist[v]:
                    ways[v] = (ways[v] + ways[u]) % MOD
        
        return ways[n - 1]