from heapq import heappop, heappush
from collections import defaultdict
from typing import List

class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        for i, (u, v, w) in enumerate(edges):
            graph[u].append((v, w, i))
            graph[v].append((u, w, i))

        min_heap = [(0, 0)]
        distances = [float('inf')] * n
        distances[0] = 0
        predecessors = {i: [] for i in range(n)}

        while min_heap:
            dist, node = heappop(min_heap)
            if dist > distances[node]:
                continue
            for neighbor, weight, edge_idx in graph[node]:
                distance = dist + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    predecessors[neighbor] = [(node, edge_idx)]
                    heappush(min_heap, (distance, neighbor))
                elif distance == distances[neighbor]:
                    predecessors[neighbor].append((node, edge_idx))

        visited = [False] * len(edges)
        def dfs(node):
            if node == 0:
                return
            for pred, edge_idx in predecessors[node]:
                if not visited[edge_idx]:
                    visited[edge_idx] = True
                    dfs(pred)

        dfs(n - 1)
        return visited