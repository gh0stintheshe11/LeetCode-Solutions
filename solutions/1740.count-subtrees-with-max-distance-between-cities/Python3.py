from typing import List

class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        from collections import defaultdict, deque
        import itertools
        
        def bfs(start, mask):
            q = deque([start])
            visited = {start}
            max_dist_node, max_dist = start, 0
            while q:
                node = q.popleft()
                for neighbor in graph[node]:
                    if neighbor not in visited and mask & (1 << (neighbor - 1)):
                        visited.add(neighbor)
                        q.append(neighbor)
                        if max_dist < dist[node] + 1:
                            max_dist = dist[node] + 1
                            max_dist_node = neighbor
                        dist[neighbor] = dist[node] + 1
            return max_dist_node, max_dist, visited
        
        def get_max_distance(subset):
            start = None
            for i in range(n):
                if subset & (1 << i):
                    start = i + 1
                    break
            dist[start] = 0
            farthest_node, _, visited = bfs(start, subset)
            if len(visited) != subset.bit_count():
                return -1
            dist[farthest_node] = 0
            _, max_diameter, _ = bfs(farthest_node, subset)
            return max_diameter

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        result = [0] * (n - 1)
        subsets = itertools.chain.from_iterable(itertools.combinations(range(n), r) for r in range(1, n + 1))
        
        dist = {}
        
        for subset in subsets:
            bitmask = sum(1 << i for i in subset)
            max_distance = get_max_distance(bitmask)
            if max_distance > 0:
                result[max_distance - 1] += 1
        
        return result