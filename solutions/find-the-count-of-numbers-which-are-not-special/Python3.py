class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        from math import isqrt

        # Maximum limit to find primes up to the square root of the max possible value (10^9)
        MAX_LIMIT = isqrt(10**9) + 1
        is_prime = [True] * (MAX_LIMIT + 1)
        primes = []
        
        # Sieve of Eratosthenes to find all prime numbers up to sqrt(10^9)
        is_prime[0] = is_prime[1] = False
        for i in range(2, MAX_LIMIT + 1):
            if is_prime[i]:
                primes.append(i)
                for j in range(i * i, MAX_LIMIT + 1, i):
                    is_prime[j] = False
        
        # Find special numbers in the range [l, r]
        special_count = 0
        for prime in primes:
            p_squared = prime * prime
            if p_squared > r:
                break
            if p_squared >= l:
                special_count += 1
        
        # Calculate the number of non-special numbers
        return (r - l + 1) - special_count