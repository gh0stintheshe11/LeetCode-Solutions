from collections import defaultdict, deque
from typing import List

class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def tree_diameter(edges, n):
            def bfs(start):
                queue = deque([start])
                distances = [-1] * n
                distances[start] = 0
                farthest, max_dist = start, 0
                while queue:
                    node = queue.popleft()
                    for neighbor in graph[node]:
                        if distances[neighbor] == -1:
                            distances[neighbor] = distances[node] + 1
                            queue.append(neighbor)
                            if distances[neighbor] > max_dist:
                                farthest, max_dist = neighbor, distances[neighbor]
                return farthest, max_dist

            graph = defaultdict(list)
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)

            farthest_node, _ = bfs(0)
            _, max_diameter = bfs(farthest_node)
            return max_diameter

        n1 = len(edges1) + 1
        n2 = len(edges2) + 1
        
        diameter1 = tree_diameter(edges1, n1)
        diameter2 = tree_diameter(edges2, n2)

        return max(diameter1, diameter2, (diameter1 + 1) // 2 + (diameter2 + 1) // 2 + 1)