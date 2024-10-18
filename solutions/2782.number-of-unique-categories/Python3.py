# Definition for a category handler.
# class CategoryHandler:
#     def haveSameCategory(self, a: int, b: int) -> bool:
#         pass
class Solution:
    def numberOfCategories(self, n: int, categoryHandler: 'CategoryHandler') -> int:
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
        
        for i in range(n):
            for j in range(i):
                if categoryHandler.haveSameCategory(i, j):
                    union(i, j)
        
        unique_categories = set(find(i) for i in range(n))
        return len(unique_categories)