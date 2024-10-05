from typing import List
from collections import defaultdict, deque

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = defaultdict(list)
        in_degree = [0] * n
        
        for u, v in richer:
            graph[u].append(v)
            in_degree[v] += 1
        
        answer = list(range(n))
        
        queue = deque([i for i in range(n) if in_degree[i] == 0])
        
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if quiet[answer[u]] < quiet[answer[v]]:
                    answer[v] = answer[u]
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
        
        return answer