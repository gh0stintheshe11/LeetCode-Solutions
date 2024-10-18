from collections import defaultdict
from typing import List

class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)
        
        parent = list(range(n))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootY] = rootX
                
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        value_to_nodes = defaultdict(list)
        for i, value in enumerate(vals):
            value_to_nodes[value].append(i)
        
        good_paths = n
        
        sorted_values = sorted(value_to_nodes.keys())
        
        for value in sorted_values:
            nodes = value_to_nodes[value]
            
            for node in nodes:
                for neighbor in graph[node]:
                    if vals[neighbor] <= value:
                        union(node, neighbor)
            
            group_count = defaultdict(int)
            
            for node in nodes:
                root = find(node)
                group_count[root] += 1
            
            for count in group_count.values():
                good_paths += count * (count - 1) // 2
        
        return good_paths