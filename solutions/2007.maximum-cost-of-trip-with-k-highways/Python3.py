from typing import List
from functools import lru_cache

class Solution:
    def maximumCost(self, n: int, highways: List[List[int]], k: int) -> int:
        adj_list = [[] for _ in range(n)]
        for city1, city2, toll in highways:
            adj_list[city1].append((city2, toll))
            adj_list[city2].append((city1, toll))
        
        @lru_cache(None)
        def dfs(city, visited_mask, remaining_edges):
            if remaining_edges == 0:
                return 0
            
            max_cost = -1
            for next_city, toll in adj_list[city]:
                if not (visited_mask & (1 << next_city)):
                    cost = dfs(next_city, visited_mask | (1 << next_city), remaining_edges - 1)
                    if cost != -1:
                        max_cost = max(max_cost, cost + toll)
            
            return max_cost
        
        result = -1
        for start_city in range(n):
            result = max(result, dfs(start_city, 1 << start_city, k))
        
        return result