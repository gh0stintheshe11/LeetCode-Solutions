class Solution:
    def countComponents(self, n: int, edges: [[int]]) -> int:
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootY] = rootX
        
        parent = [i for i in range(n)]
        
        for x, y in edges:
            union(x, y)
        
        return len(set(find(x) for x in range(n)))