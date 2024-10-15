class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        parent = list(range(n))
        rank = [0] * n
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    parent[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    parent[rootX] = rootY
                else:
                    parent[rootY] = rootX
                    rank[rootX] += 1
        
        result = []
        for u, v in requests:
            rootU = find(u)
            rootV = find(v)
            
            can_merge = True
            for x, y in restrictions:
                rootX = find(x)
                rootY = find(y)
                if (rootU == rootX and rootV == rootY) or (rootU == rootY and rootV == rootX):
                    can_merge = False
                    break
            
            if can_merge:
                union(u, v)
                result.append(True)
            else:
                result.append(False)
        
        return result