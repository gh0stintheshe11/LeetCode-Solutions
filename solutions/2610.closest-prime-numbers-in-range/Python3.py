from typing import List

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def sieve_of_eratosthenes(n):
            is_prime = [True] * (n + 1)
            p = 2
            while p * p <= n:
                if is_prime[p]:
                    for i in range(p * p, n + 1, p):
                        is_prime[i] = False
                p += 1
            primes = []
            for p in range(2, n + 1):
                if is_prime[p]:
                    primes.append(p)
            return primes

        if left < 2:
            left = 2
        
        primes = sieve_of_eratosthenes(right)
        primes_in_range = [p for p in primes if left <= p <= right]

        if len(primes_in_range) < 2:
            return [-1, -1]

        closest_pair = [primes_in_range[0], primes_in_range[1]]
        min_diff = closest_pair[1] - closest_pair[0]

        for i in range(1, len(primes_in_range) - 1):
            diff = primes_in_range[i + 1] - primes_in_range[i]
            if diff < min_diff:
                min_diff = diff
                closest_pair = [primes_in_range[i], primes_in_range[i + 1]]

        return closest_pair