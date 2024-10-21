from typing import List
from collections import defaultdict
import heapq

class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        adjacency_list = defaultdict(list)
        
        # Build adjacency list
        for a, b in edges:
            adjacency_list[a].append(vals[b])
            adjacency_list[b].append(vals[a])
        
        max_star_sum = float('-inf')
        
        # Evaluate max star sum using each node as the center
        for node in range(len(vals)):
            # Get the node's value and its neighbors' values
            node_value = vals[node]
            neighbors = adjacency_list[node]
            
            # Extract k largest positive neighbors
            largest_neighbors = heapq.nlargest(k, [v for v in neighbors if v > 0])
            
            # Calculate star sum
            star_sum = node_value + sum(largest_neighbors)
            max_star_sum = max(max_star_sum, star_sum)
        
        return max_star_sum