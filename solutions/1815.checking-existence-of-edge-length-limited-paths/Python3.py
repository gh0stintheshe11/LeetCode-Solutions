class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        edgeList.sort(key=lambda x: x[2])
        queries = sorted(enumerate(queries), key=lambda x: x[1][2])
        
        parent = list(range(n))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootX] = rootY
        
        answers = [False] * len(queries)
        edgeIndex = 0
        
        for idx, (p, q, limit) in queries:
            while edgeIndex < len(edgeList) and edgeList[edgeIndex][2] < limit:
                u, v, dist = edgeList[edgeIndex]
                union(u, v)
                edgeIndex += 1
            
            if find(p) == find(q):
                answers[idx] = True
        
        return answers