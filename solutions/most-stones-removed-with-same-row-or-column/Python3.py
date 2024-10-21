class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = {}
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootY] = rootX
        
        for x, y in stones:
            if x not in parent:
                parent[x] = x
            if ~y not in parent:
                parent[~y] = ~y
            union(x, ~y)
        
        return len(stones) - len({find(x) for x in parent})