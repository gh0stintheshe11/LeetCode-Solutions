from typing import List
from collections import defaultdict

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        parent = list(range(len(s)))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootY] = rootX
        
        for a, b in pairs:
            union(a, b)

        components = defaultdict(list)
        for i in range(len(s)):
            root = find(i)
            components[root].append(i)

        res = list(s)
        for indices in components.values():
            chars = sorted(res[i] for i in indices)
            for i, ch in zip(sorted(indices), chars):
                res[i] = ch

        return ''.join(res)