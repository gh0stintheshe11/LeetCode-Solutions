from heapq import heappop, heappush
from typing import List
import sys

class Solution:
    def minimumDistance(self, n: int, edges: List[List[int]], s: int, marked: List[int]) -> int:
        # Create the adjacency list
        graph = {i: [] for i in range(n)}
        for u, v, w in edges:
            graph[u].append((v, w))
        
        # Initialize distances and priority queue
        dist = [sys.maxsize] * n
        dist[s] = 0
        min_heap = [(0, s)]  # (distance, node)
        
        # Dijkstra's algorithm
        while min_heap:
            current_dist, node = heappop(min_heap)
            if current_dist > dist[node]:
                continue
            for neighbor, weight in graph[node]:
                new_dist = current_dist + weight
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    heappush(min_heap, (new_dist, neighbor))
        
        # Calculate the minimum distance to any marked node
        min_distance = sys.maxsize
        for m in marked:
            if dist[m] < min_distance:
                min_distance = dist[m]
        
        return min_distance if min_distance != sys.maxsize else -1