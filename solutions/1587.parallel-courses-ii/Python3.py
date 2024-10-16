from itertools import combinations
from collections import defaultdict
from functools import lru_cache
from typing import List

class Solution:
    @lru_cache(None)
    def recurse(self, mask, in_degrees):
        if not mask:
            return 0
        
        nodes = [i for i in range(self.n) if mask & (1 << i) and in_degrees[i] == 0]
        
        ans = float('inf')
        for k_nodes in combinations(nodes, min(self.k, len(nodes))):
            new_mask, new_in_degrees = mask, list(in_degrees)
            
            for node in k_nodes:
                new_mask ^= 1 << node
                for child in self.graph[node]:
                    new_in_degrees[child] -= 1
            
            ans = min(ans, 1 + self.recurse(new_mask, tuple(new_in_degrees)))
        return ans

    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        self.n = n
        self.k = k
        in_degrees = [0] * self.n
        self.graph = defaultdict(list)
        for prev_course, next_course in relations:
            in_degrees[next_course - 1] += 1
            self.graph[prev_course - 1].append(next_course - 1)
        
        return self.recurse((1 << self.n) - 1, tuple(in_degrees))