from typing import List

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        from collections import defaultdict
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # To track visited nodes
        visited = [False] * n
        result = 0

        def dfs(node):
            nonlocal result
            visited[node] = True
            total_value = values[node]

            for neighbor in graph[node]:
                if not visited[neighbor]:
                    total_value += dfs(neighbor)

            if total_value % k == 0:
                result += 1
                return 0
            else:
                return total_value
        
        dfs(0)
        
        return result