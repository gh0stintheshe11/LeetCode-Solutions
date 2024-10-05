import heapq
from typing import List

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly_numbers = [1] * n
        indices = [0] * len(primes)
        next_multiple = primes[:]
        
        for i in range(1, n):
            next_ugly = min(next_multiple)
            ugly_numbers[i] = next_ugly

            for j in range(len(primes)):
                if next_ugly == next_multiple[j]:
                    indices[j] += 1
                    next_multiple[j] = ugly_numbers[indices[j]] * primes[j]
        
        return ugly_numbers[-1]