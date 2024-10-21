from typing import List
from collections import defaultdict
from math import gcd
from functools import lru_cache

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        def prime_factors(n):
            factors = set()
            d = 2
            while d * d <= n:
                while n % d == 0:
                    factors.add(d)
                    n //= d
                d += 1
            if n > 1:
                factors.add(n)
            return factors

        n = len(nums)
        if n == 1:
            return True

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

        prime_to_indices = defaultdict(list)

        for i, num in enumerate(nums):
            factors = prime_factors(num)
            for factor in factors:
                prime_to_indices[factor].append(i)

        for indices in prime_to_indices.values():
            for i in range(1, len(indices)):
                union(indices[0], indices[i])

        root = find(0)
        for i in range(n):
            if find(i) != root:
                return False

        return True