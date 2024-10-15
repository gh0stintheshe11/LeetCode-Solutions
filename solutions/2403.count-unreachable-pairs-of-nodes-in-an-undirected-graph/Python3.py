from typing import List

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        # Helper function for DFS to find the size of each component
        def dfs(node):
            stack = [node]
            size = 0
            while stack:
                node = stack.pop()
                if not visited[node]:
                    visited[node] = True
                    size += 1
                    stack.extend(graph[node])
            return size
        
        # Create the adjacency list
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Use DFS to find all connected components
        visited = [False] * n
        component_sizes = []
        
        for i in range(n):
            if not visited[i]:
                component_size = dfs(i)
                component_sizes.append(component_size)
        
        # Calculate the number of unreachable pairs
        total_pairs = n * (n - 1) // 2
        reachable_pairs = sum(size * (size - 1) // 2 for size in component_sizes)
        
        return total_pairs - reachable_pairs