from typing import List
from heapq import heappop, heappush

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        def dijkstra(start: int, end: int, n: int, roads: List[List[int]]) -> int:
            graph = [[] for _ in range(n)]
            for u, v in roads:
                graph[u].append(v)
            
            distances = [float('inf')] * n
            distances[start] = 0
            heap = [(0, start)]
            
            while heap:
                curr_dist, node = heappop(heap)
                if node == end:
                    return curr_dist
                for neighbor in graph[node]:
                    if curr_dist + 1 < distances[neighbor]:
                        distances[neighbor] = curr_dist + 1
                        heappush(heap, (distances[neighbor], neighbor))
            return float('inf')
        
        # Initial roads from city i to city i+1
        roads = [[i, i + 1] for i in range(n - 1)]
        answer = []
        
        for u, v in queries:
            roads.append([u, v])
            shortest_path_length = dijkstra(0, n - 1, n, roads)
            answer.append(shortest_path_length)
        
        return answer