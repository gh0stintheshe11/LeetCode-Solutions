from typing import List
from collections import defaultdict

class Solution:
    def countPalindromePaths(self, parent: List[int], s: str) -> int:
        n = len(parent)
        tree = defaultdict(list)
        for i in range(1, n):
            tree[parent[i]].append(i)
        
        # To store the xor mask of characters from root to each node
        mask = [0] * n
        
        def dfs(node: int, current_mask: int):
            # Update current node's mask
            current_mask ^= 1 << (ord(s[node]) - ord('a'))
            mask[node] = current_mask
            for child in tree[node]:
                dfs(child, current_mask)
        
        # Begin DFS traversal
        dfs(0, 0)
        
        # Count the number of paths with the same mask or masks differing by only a single bit
        count = defaultdict(int)
        result = 0
        for node_mask in mask:
            result += count[node_mask]
            # Considering paths differing by one bit
            for bit in range(26):
                result += count[node_mask ^ (1 << bit)]
            count[node_mask] += 1
        
        return result