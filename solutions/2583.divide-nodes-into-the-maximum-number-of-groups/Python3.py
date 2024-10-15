from typing import List
from collections import deque, defaultdict

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        def bfs(start):
            queue = deque([(start, 0)])
            visited = [-1] * (n + 1)
            visited[start] = 0
            max_depth = 0
            
            while queue:
                node, depth = queue.popleft()
                max_depth = max(max_depth, depth)
                
                for neighbor in graph[node]:
                    if visited[neighbor] == -1:
                        visited[neighbor] = depth + 1
                        queue.append((neighbor, depth + 1))
                    elif abs(visited[neighbor] - depth) != 1:
                        return -1, -1
            
            return max_depth, 1
        
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited_all = [False] * (n + 1)
        total_groups = 0
        
        for node in range(1, n + 1):
            if not visited_all[node]:
                component = []
                queue = deque([node])
                visited_all[node] = True
                while queue:
                    v = queue.popleft()
                    component.append(v)
                    for neighbor in graph[v]:
                        if not visited_all[neighbor]:
                            visited_all[neighbor] = True
                            queue.append(neighbor)
                
                max_groups = 0
                for v in component:
                    max_depth, valid = bfs(v)
                    if valid == -1: return -1
                    max_groups = max(max_groups, max_depth)
                
                total_groups += max_groups + 1
        
        return total_groups