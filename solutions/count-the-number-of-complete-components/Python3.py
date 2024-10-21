from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        from collections import defaultdict, deque
        
        # Build the adjacency list for the graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = [False] * n
        
        def bfs(node):
            queue = deque([node])
            visited[node] = True
            nodes = 0
            edge_count = 0
            
            while queue:
                current = queue.popleft()
                nodes += 1
                for neighbor in graph[current]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
                    # Each edge is counted twice in an undirected graph
                    edge_count += 1
            
            # Make sure edge_count only counts each edge once
            edge_count //= 2
            return nodes, edge_count
        
        complete_components = 0
        
        for i in range(n):
            if not visited[i]:
                nodes, edge_count = bfs(i)
                # A connected component with m nodes has m*(m-1)//2 edges if it's complete
                if edge_count == nodes * (nodes - 1) // 2:
                    complete_components += 1
        
        return complete_components