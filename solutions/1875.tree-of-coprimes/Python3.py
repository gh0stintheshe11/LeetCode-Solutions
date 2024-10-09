from typing import List
from math import gcd
from collections import defaultdict

class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        n = len(nums)
        
        # Build the adjacency list for the tree
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        # This will be used to store the result
        result = [-1] * n
        
        # Keep track of the depth of each node and the path of coprime ancestors
        last_seen = defaultdict(list)
        
        # DFS to find the closest coprime ancestor for each node
        def dfs(node, parent, depth):
            # Find the closest coprime ancestor
            val = nums[node]
            max_depth = -1
            ancestor = -1
            
            for i in range(1, 51):
                if gcd(i, val) == 1 and last_seen[i]:
                    d, anc = last_seen[i][-1]
                    if d > max_depth:
                        max_depth = d
                        ancestor = anc
            
            result[node] = ancestor

            # Add current node to the path
            last_seen[val].append((depth, node))
            
            # Continue DFS
            for neighbor in tree[node]:
                if neighbor != parent:
                    dfs(neighbor, node, depth + 1)

            # Remove current node from the path
            last_seen[val].pop()

        # Start DFS
        dfs(0, -1, 0)
        
        return result