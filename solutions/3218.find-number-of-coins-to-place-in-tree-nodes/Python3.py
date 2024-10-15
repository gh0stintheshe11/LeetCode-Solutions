from typing import List, Tuple
from heapq import nlargest, nsmallest

class Solution:
    def placedCoins(self, edges: List[List[int]], cost: List[int]) -> List[int]:
        
        def max_product(arr: List[int]) -> int:
            top3_pos = nlargest(3, arr)
            if len(top3_pos) < 3:
                return 1
            min3_neg = nsmallest(3, arr)
            product_pos = top3_pos[0] * top3_pos[1] * top3_pos[2]
            product_neg = min3_neg[0] * min3_neg[1] * top3_pos[0] if len(min3_neg) > 1 else float('-inf')
            max_product = max(product_pos, product_neg)
            return max(max_product, 0)
        
        def dfs(node: int, parent: int):
            subtree_costs = [cost[node]]
            subtree_sizes[node] = 1
            
            for neighbor in tree[node]:
                if neighbor != parent:
                    sub_costs = dfs(neighbor, node)
                    subtree_sizes[node] += subtree_sizes[neighbor]
                    subtree_costs.extend(sub_costs)
            
            if subtree_sizes[node] < 3:
                coins[node] = 1
            else:
                coins[node] = max_product(subtree_costs)
            
            return subtree_costs
        
        n = len(cost)
        tree = [[] for _ in range(n)]
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)
        
        coins = [0] * n
        subtree_sizes = [0] * n
        
        dfs(0, -1)
        return coins