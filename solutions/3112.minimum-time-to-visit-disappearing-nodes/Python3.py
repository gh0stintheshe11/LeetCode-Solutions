from heapq import heappop, heappush
from typing import List

class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        # Create adjacency list for the graph
        graph = {i: [] for i in range(n)}
        for u, v, length in edges:
            graph[u].append((v, length))
            graph[v].append((u, length))
        
        # Min-heap for Dijkstra's algorithm
        min_heap = [(0, 0)]  # (time, node)
        # Distance from node 0 to each node, initialized to infinity
        min_time = [float('inf')] * n
        # Starting point
        min_time[0] = 0

        while min_heap:
            curr_time, u = heappop(min_heap)
            
            # If this is not the shortest path to u, continue
            if curr_time > min_time[u]:
                continue
            
            # Explore neighbors
            for v, length in graph[u]:
                new_time = curr_time + length
                # Only consider this new path if it's shorter than any known path and the node can be reached before disappearing
                if new_time < disappear[v] and new_time < min_time[v]:
                    min_time[v] = new_time
                    heappush(min_heap, (new_time, v))
        
        # Transform unreachable node times to -1
        return [time if time != float('inf') else -1 for time in min_time]