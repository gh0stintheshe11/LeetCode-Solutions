from typing import List
from collections import deque, defaultdict

class Solution:
    def distanceToCycle(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Detect cycle using DFS and finding back edges
        def dfs(node, parent):
            nonlocal found_cycle
            if found_cycle:
                return []
            visited[node] = True
            path.append(node)
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if visited[neighbor]:
                    found_cycle = True
                    cycle_index = path.index(neighbor)
                    cycle_nodes.extend(path[cycle_index:])
                    return cycle_nodes
                result = dfs(neighbor, node)
                if found_cycle:
                    return result
            path.pop()
            return []
        
        visited = [False] * n
        cycle_nodes = []
        found_cycle = False
        path = []
        
        for i in range(n):
            if not visited[i]:
                dfs(i, -1)
                if found_cycle:
                    break
        
        # BFS from cycle nodes to find distances
        distance = [-1] * n
        queue = deque(cycle_nodes)
        
        for cn in cycle_nodes:
            distance[cn] = 0
        
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if distance[neighbor] == -1:
                    distance[neighbor] = distance[node] + 1
                    queue.append(neighbor)
        
        return distance