from typing import List
from collections import defaultdict

class Solution:
    def maximumSubtreeSize(self, edges: List[List[int]], colors: List[int]) -> int:
        def dfs(node: int, parent: int) -> int:
            # The current node contributes itself
            subtree_size = 1
            is_uniform = True

            for neighbor in tree[node]:
                if neighbor == parent:
                    continue
                size, uniform = dfs(neighbor, node)
                if not uniform or colors[neighbor] != colors[node]:
                    is_uniform = False
                subtree_size += size
            
            if is_uniform:
                nonlocal max_size
                max_size = max(max_size, subtree_size)
            
            return subtree_size, is_uniform

        # Construct the tree from edges
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        max_size = 1
        dfs(0, -1)
        return max_size