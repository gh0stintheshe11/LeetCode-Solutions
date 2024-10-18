class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        parent = list(range(n + 1))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootX] = rootY
        
        if threshold < n:
            for i in range(threshold + 1, n + 1):
                for j in range(2 * i, n + 1, i):
                    union(i, j)
        
        result = []
        for a, b in queries:
            if find(a) == find(b):
                result.append(True)
            else:
                result.append(False)

        return result