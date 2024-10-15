from typing import List, Dict
from collections import defaultdict, deque

class Solution:
    def lastMarkedNodes(self, edges: List[List[int]]) -> List[int]:
        def bfs(u: int) -> Dict[int, int]:
            queue = deque([u])
            distances = {u: 0}
            while queue:
                node = queue.popleft()
                current_distance = distances[node]
                for neighbor in graph[node]:
                    if neighbor not in distances:
                        distances[neighbor] = current_distance + 1
                        queue.append(neighbor)
            return distances

        n = len(edges) + 1
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        distances_from_any_node = bfs(0)
        farthest_from_any_node = max(distances_from_any_node, key=distances_from_any_node.get)

        distances_from_farthest_node = bfs(farthest_from_any_node)
        farthest_from_farthest_node = max(distances_from_farthest_node, key=distances_from_farthest_node.get)

        distances_from_other_far = bfs(farthest_from_farthest_node)

        result = []
        for i in range(n):
            if distances_from_farthest_node[i] > distances_from_other_far[i]:
                result.append(farthest_from_any_node)
            else:
                result.append(farthest_from_farthest_node)

        return result