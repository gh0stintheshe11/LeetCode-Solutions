from typing import List
from collections import defaultdict, deque

class Solution:
    def closestNode(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        def bfs(start):
            dist = [-1] * n
            dist[start] = 0
            q = deque([start])
            while q:
                u = q.popleft()
                for v in graph[u]:
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        q.append(v)
            return dist

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def bfs_path(start, end):
            q = deque([(start, [start])])
            visited = set()
            while q:
                node, path = q.popleft()
                if node == end:
                    return path
                if node not in visited:
                    visited.add(node)
                    for neighbor in graph[node]:
                        if neighbor not in visited:
                            q.append((neighbor, path + [neighbor]))
            return []

        results = []
        for start, end, k in query:
            path = bfs_path(start, end)
            distances = bfs(k)
            closest = path[0]
            for node in path:
                if distances[node] < distances[closest]:
                    closest = node
            results.append(closest)

        return results