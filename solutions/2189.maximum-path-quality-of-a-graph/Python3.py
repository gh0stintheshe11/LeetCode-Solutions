from typing import List, Dict
from collections import defaultdict

class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        graph = defaultdict(list)
        
        for u, v, time in edges:
            graph[u].append((v, time))
            graph[v].append((u, time))

        def dfs(node: int, time: int, visited: Dict[int, int], quality: int) -> None:
            nonlocal maxQuality
            if time < 0:
                return
            
            if visited[node] == 0:
                uniqueQuality = quality + values[node]
            else:
                uniqueQuality = quality
            
            visited[node] += 1
            
            if node == 0:
                maxQuality = max(maxQuality, uniqueQuality)
                
            for neighbor, travelTime in graph[node]:
                dfs(neighbor, time - travelTime, visited, uniqueQuality)
                
            visited[node] -= 1

        maxQuality = 0
        initialVisited = [0] * len(values)
        dfs(0, maxTime, initialVisited, 0)
        return maxQuality