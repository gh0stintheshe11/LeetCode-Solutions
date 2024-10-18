from typing import List
from math import gcd
from collections import defaultdict

class Solution:
    def findValidSplit(self, nums: List[int]) -> int:
        def prime_factors(n):
            factors = set()
            d = 2
            while d * d <= n:
                while (n % d) == 0:
                    factors.add(d)
                    n //= d
                d += 1
            if n > 1:
                factors.add(n)
            return factors

        n = len(nums)
        
        left_factors = defaultdict(int)
        right_factors = defaultdict(int)

        # Initialize right_factors with factors of all elements
        for num in nums:
            pf = prime_factors(num)
            for f in pf:
                right_factors[f] += 1

        # Iterate through the array and maintain prime factors count
        for i in range(n - 1):
            pf = prime_factors(nums[i])
            
            # Update left_factors and decrease from right_factors
            for f in pf:
                left_factors[f] += 1
                right_factors[f] -= 1
                if right_factors[f] == 0:
                    del right_factors[f]
            
            # Check if there's no common prime factor between left and right side
            if not any(f in right_factors for f in left_factors):
                return i

        return -1