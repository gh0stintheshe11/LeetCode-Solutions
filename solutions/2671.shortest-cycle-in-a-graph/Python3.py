from typing import List, Dict
from collections import deque, defaultdict

class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        # Build the graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Function to find the shortest cycle starting from a given node
        def bfs(start: int) -> int:
            # Distance to each node (starting node has distance 0)
            dist = {start: 0}
            q = deque([(start, -1)])
            shortest = float('inf')
            
            while q:
                node, parent = q.popleft()
                
                for neighbor in graph[node]:
                    if neighbor not in dist:
                        dist[neighbor] = dist[node] + 1
                        q.append((neighbor, node))
                    elif neighbor != parent:
                        # Found a cycle
                        cycle_length = dist[node] + dist[neighbor] + 1
                        shortest = min(shortest, cycle_length)
            
            return shortest
        
        result = float('inf')
        
        # Check shortest cycle for each vertex
        for i in range(n):
            result = min(result, bfs(i))
        
        return result if result != float('inf') else -1