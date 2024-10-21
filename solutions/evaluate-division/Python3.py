from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        from collections import defaultdict, deque
        
        # Create a graph
        graph = defaultdict(dict)
        
        # Build the graph
        for (dividend, divisor), value in zip(equations, values):
            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1 / value
        
        # Function to find the result of a query using BFS
        def bfs(src, dest):
            if src not in graph or dest not in graph:
                return -1.0
            queue = deque([(src, 1.0)])
            visited = set()
            
            while queue:
                node, cur_product = queue.popleft()
                if node == dest:
                    return cur_product
                visited.add(node)
                
                for neighbor, value in graph[node].items():
                    if neighbor not in visited:
                        queue.append((neighbor, cur_product * value))
            
            return -1.0
        
        # Process each query
        results = []
        for dividend, divisor in queries:
            if dividend == divisor:
                results.append(1.0 if dividend in graph else -1.0)
            else:
                results.append(bfs(dividend, divisor))
        
        return results