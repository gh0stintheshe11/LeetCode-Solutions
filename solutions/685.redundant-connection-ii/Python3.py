from typing import List

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        def find(parent, i):
            if parent[i] == i:
                return i
            parent[i] = find(parent, parent[i])
            return parent[i]
        
        def union(parent, rank, x, y):
            rootX = find(parent, x)
            rootY = find(parent, y)
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    parent[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    parent[rootX] = rootY
                else:
                    parent[rootY] = rootX
                    rank[rootX] += 1
        
        n = len(edges)
        parent = list(range(n + 1))
        rank = [0] * (n + 1)
        candidate1 = candidate2 = []
        child_parent = {}
        
        for u, v in edges:
            if v in child_parent:
                candidate1 = [child_parent[v], v]
                candidate2 = [u, v]
                break
            child_parent[v] = u
        
        parent = list(range(n + 1))
        rank = [0] * (n + 1)
        
        for u, v in edges:
            if [u, v] == candidate2:
                continue
            pu = find(parent, u)
            pv = find(parent, v)
            if pu == pv:
                if not candidate1:
                    return [u, v]
                return candidate1
            union(parent, rank, pu, pv)
        
        return candidate2