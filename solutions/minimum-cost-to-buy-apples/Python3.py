from heapq import heappop, heappush
from typing import List

class Solution:
    def minCost(self, n: int, roads: List[List[int]], appleCost: List[int], k: int) -> List[int]:
        # Create an adjacency list representation of the graph
        graph = [[] for _ in range(n + 1)]
        for u, v, cost in roads:
            graph[u].append((v, cost))
            graph[v].append((u, cost))
        
        def dijkstra(start: int) -> List[int]:
            min_cost = [float('inf')] * (n + 1)
            min_cost[start] = 0
            heap = [(0, start)]
            while heap:
                current_cost, node = heappop(heap)
                if current_cost > min_cost[node]:
                    continue
                for neighbor, road_cost in graph[node]:
                    new_cost = current_cost + road_cost
                    if new_cost < min_cost[neighbor]:
                        min_cost[neighbor] = new_cost
                        heappush(heap, (new_cost, neighbor))
            return min_cost
        
        results = []
        for start in range(1, n + 1):
            initial_dijkstra = dijkstra(start)
            min_total_cost = appleCost[start - 1]  # Cost of buying apple in the starting city
            for city in range(1, n + 1):
                if city != start:
                    round_trip_cost = initial_dijkstra[city] + appleCost[city - 1] + k * initial_dijkstra[city]
                    min_total_cost = min(min_total_cost, round_trip_cost)
            results.append(min_total_cost)
        
        return results