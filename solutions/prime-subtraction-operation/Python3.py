from typing import List

class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        
        def sieve_of_eratosthenes(max_num):
            primes = []
            is_prime = [True] * (max_num + 1)
            is_prime[0] = is_prime[1] = False
            for start in range(2, max_num + 1):
                if is_prime[start]:
                    primes.append(start)
                    for multiple in range(start*start, max_num + 1, start):
                        is_prime[multiple] = False
            return primes
        
        primes = sieve_of_eratosthenes(1000)
        
        previous = 0
        for num in nums:
            for p in reversed(primes):
                if num - p > previous:
                    num -= p
                    break
            if num <= previous:
                return False
            previous = num
        
        return True