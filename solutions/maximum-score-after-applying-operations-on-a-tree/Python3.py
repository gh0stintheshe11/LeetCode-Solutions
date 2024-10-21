from typing import List
import collections

class Solution:
    def dfs(self, graph, node, values, visit):
        if len(graph[node]) == 1 and node != 0:
            return values[node]
        sums = 0
        for nei in graph[node]:
            if nei not in visit:
                visit.add(nei)
                sums += self.dfs(graph, nei, values, visit)
        return min(sums, values[node])
    
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visit = set()
        visit.add(0)
        return sum(values) - self.dfs(graph, 0, values, visit)