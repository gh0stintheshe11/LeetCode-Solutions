from typing import List
import heapq
from collections import defaultdict

class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.graph = defaultdict(list)
        for u, v, w in edges:
            self.graph[u].append((v, w))

    def addEdge(self, edge: List[int]) -> None:
        u, v, w = edge
        self.graph[u].append((v, w))
        
    def shortestPath(self, node1: int, node2: int) -> int:
        # Dijkstra's algorithm
        heap = [(0, node1)]  # (cost, node)
        min_cost = {i: float('inf') for i in range(self.n)}
        min_cost[node1] = 0
        
        while heap:
            cost, node = heapq.heappop(heap)
            
            if node == node2:
                return cost
            
            if cost > min_cost[node]:
                continue
            
            for neighbor, weight in self.graph[node]:
                new_cost = cost + weight
                if new_cost < min_cost[neighbor]:
                    min_cost[neighbor] = new_cost
                    heapq.heappush(heap, (new_cost, neighbor))
        
        return -1