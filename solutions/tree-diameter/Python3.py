from typing import List, Dict
from collections import deque, defaultdict

class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        if not edges:
            return 0
        
        # Convert edges to an adjacency list
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        # Helper function to perform BFS and return the furthest node and its distance from start node
        def bfs_furthest(start: int) -> (int, int):
            q = deque([(start, 0)])  # (current_node, distance_from_start_node)
            visited = {start}
            furthest_node, max_distance = start, 0
            
            while q:
                current, distance = q.popleft()
                
                for neighbor in adj_list[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append((neighbor, distance + 1))
                        if distance + 1 > max_distance:
                            furthest_node, max_distance = neighbor, distance + 1
            
            return furthest_node, max_distance
        
        # Perform two BFS to find the tree diameter
        # Start with any node, say, node 0 (this works because guaranteed 1 <= n)
        node_A, _ = bfs_furthest(0)
        # Start from the furthest node found to get the furthest node from it which is the diameter
        node_B, diameter = bfs_furthest(node_A)
        
        return diameter