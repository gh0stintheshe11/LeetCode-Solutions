from typing import List
import math

class Solution:
    def gcdSort(self, nums: List[int]) -> bool:
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootY] = rootX
        
        max_num = max(nums)
        parent = list(range(max_num + 1))
        
        # Sieve of Eratosthenes to find all prime numbers up to max_num
        is_prime = [True] * (max_num + 1)
        for i in range(2, int(math.sqrt(max_num)) + 1):
            if is_prime[i]:
                for j in range(i * i, max_num + 1, i):
                    is_prime[j] = False
        
        # Union all numbers with their prime factors
        for num in nums:
            original = num
            for factor in range(2, int(math.sqrt(num)) + 1):
                if num % factor == 0:
                    union(original, factor)
                    while num % factor == 0:
                        num //= factor
            if num > 1:  # Means num is a prime factor itself
                union(original, num)
        
        # Check if we can sort nums by comparing components
        sorted_nums = sorted(nums)
        for i in range(len(nums)):
            if find(nums[i]) != find(sorted_nums[i]):
                return False
        return True