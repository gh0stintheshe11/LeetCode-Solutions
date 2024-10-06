from typing import List

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # Disjoint Set data structure (Union-Find)
        parentA = list(range(n + 1))
        parentB = list(range(n + 1))
        rankA = [1] * (n + 1)
        rankB = [1] * (n + 1)
        
        def find(parent, x):
            if parent[x] != x:
                parent[x] = find(parent, parent[x])
            return parent[x]
        
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
                return True
            return False
        
        # Step 1: Add type 3 edges (usable by both Alice and Bob)
        usedEdges = 0
        for edgeType, u, v in edges:
            if edgeType == 3:
                if union(parentA, rankA, u, v) | union(parentB, rankB, u, v):
                    usedEdges += 1
        
        # Step 2: Add type 1 edges (only for Alice)
        for edgeType, u, v in edges:
            if edgeType == 1:
                if union(parentA, rankA, u, v):
                    usedEdges += 1
        
        # Step 3: Add type 2 edges (only for Bob)
        for edgeType, u, v in edges:
            if edgeType == 2:
                if union(parentB, rankB, u, v):
                    usedEdges += 1
        
        # Validate if both Alice and Bob can fully traverse the graph
        if sum(find(parentA, i) == find(parentA, 1) for i in range(1, n + 1)) == n and \
           sum(find(parentB, i) == find(parentB, 1) for i in range(1, n + 1)) == n:
            return len(edges) - usedEdges
        else:
            return -1