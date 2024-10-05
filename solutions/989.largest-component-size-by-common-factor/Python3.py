from typing import List
import math
from collections import defaultdict

class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootX] = rootY
                size[rootY] += size[rootX]

        parent = {i: i for i in nums}
        size = {i: 1 for i in nums}
        
        def prime_factors(x):
            factors = set()
            while x % 2 == 0:
                factors.add(2)
                x //= 2
            for i in range(3, int(math.sqrt(x)) + 1, 2):
                while x % i == 0:
                    factors.add(i)
                    x //= i
            if x > 2:
                factors.add(x)
            return factors

        primes_to_index = defaultdict(list)
        
        for num in nums:
            factors = prime_factors(num)
            for factor in factors:
                primes_to_index[factor].append(num)
                
        for indices in primes_to_index.values():
            for i in range(1, len(indices)):
                union(indices[0], indices[i])
                
        return max(size.values())