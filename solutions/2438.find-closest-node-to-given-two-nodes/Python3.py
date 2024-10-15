from typing import List, Dict
from collections import deque

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def bfs_distance(start: int) -> Dict[int, int]:
            distance = {}
            queue = deque([(start, 0)])
            visited = set()
            
            while queue:
                node, dist = queue.popleft()
                if node in visited:
                    continue
                visited.add(node)
                distance[node] = dist
                next_node = edges[node]
                if next_node != -1 and next_node not in visited:
                    queue.append((next_node, dist + 1))
            
            return distance
        
        distance_from_node1 = bfs_distance(node1)
        distance_from_node2 = bfs_distance(node2)
        
        min_distance = float('inf')
        min_node = -1
        
        for node in range(len(edges)):
            if node in distance_from_node1 and node in distance_from_node2:
                max_dist = max(distance_from_node1[node], distance_from_node2[node])
                if max_dist < min_distance:
                    min_distance = max_dist
                    min_node = node
                elif max_dist == min_distance and node < min_node:
                    min_node = node
        
        return min_node