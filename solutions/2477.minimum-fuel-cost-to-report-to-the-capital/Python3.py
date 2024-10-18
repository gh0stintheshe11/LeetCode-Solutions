from typing import List
from collections import defaultdict
import math

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        if not roads:
            return 0

        graph = defaultdict(list)
        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)
        
        self.total_fuel = 0

        def dfs(node, parent):
            representatives = 1
            for neighbor in graph[node]:
                if neighbor != parent:
                    representatives += dfs(neighbor, node)
            if node != 0:
                self.total_fuel += math.ceil(representatives / seats)
            return representatives
        
        dfs(0, -1)
        return self.total_fuel