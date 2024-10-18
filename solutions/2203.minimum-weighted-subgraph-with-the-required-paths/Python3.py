import heapq
from typing import List
from collections import defaultdict

class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        def dijkstra(start: int, graph: dict) -> List[int]:
            dist = [float('inf')] * n
            dist[start] = 0
            min_heap = [(0, start)]
            
            while min_heap:
                current_dist, u = heapq.heappop(min_heap)
                if current_dist > dist[u]:
                    continue
                for v, weight in graph[u]:
                    if dist[u] + weight < dist[v]:
                        dist[v] = dist[u] + weight
                        heapq.heappush(min_heap, (dist[v], v))
            return dist
        
        graph = defaultdict(list)
        reverse_graph = defaultdict(list)
        
        for u, v, w in edges:
            graph[u].append((v, w))
            reverse_graph[v].append((u, w))
        
        dist_src1 = dijkstra(src1, graph)
        dist_src2 = dijkstra(src2, graph)
        dist_dest = dijkstra(dest, reverse_graph)
        
        min_weight = float('inf')
        for i in range(n):
            if dist_src1[i] != float('inf') and dist_src2[i] != float('inf') and dist_dest[i] != float('inf'):
                min_weight = min(min_weight, dist_src1[i] + dist_src2[i] + dist_dest[i])
        
        return min_weight if min_weight != float('inf') else -1