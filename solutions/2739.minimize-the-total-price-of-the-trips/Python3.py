from typing import List
from collections import defaultdict, Counter

class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        # Create adjacency list for the tree
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        # Function to find the path between two nodes using DFS
        def dfs_path(start, target, path):
            if start == target:
                return path + [start]
            seen.add(start)
            path.append(start)
            for neighbor in tree[start]:
                if neighbor not in seen:
                    result = dfs_path(neighbor, target, path)
                    if result is not None:
                        return result
            path.pop()
            return None

        # Count the frequency of each node being on the path of any trip
        freq = Counter()
        for start, end in trips:
            seen = set()
            path = dfs_path(start, end, [])
            for node in path:
                freq[node] += 1

        # Dynamic programming on trees
        # dp[node][0] = minimum total price if we do not halve the price at this node
        # dp[node][1] = minimum total price if we halve the price at this node

        dp = [[0, 0] for _ in range(n)]

        def tree_dp(node, parent):
            no_halve = freq[node] * price[node]  # cost if this node's price is not halved
            
            halve = (freq[node] * price[node]) // 2  # cost if this node's price is halved

            for neighbor in tree[node]:
                if neighbor == parent:
                    continue
                tree_dp(neighbor, node)
                # Add the minimal cost of child nodes, choosing to halve or not to halve
                no_halve += min(dp[neighbor][0], dp[neighbor][1])
                halve += dp[neighbor][0]  # child must not halve if current node is halved
            
            dp[node][0] = no_halve
            dp[node][1] = halve

        # We begin the DP calculation with any root node, here node 0
        tree_dp(0, -1)
        return min(dp[0][0], dp[0][1])