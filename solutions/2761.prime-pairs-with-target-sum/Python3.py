from typing import List

class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        def sieve_of_eratosthenes(limit: int) -> List[bool]:
            is_prime = [True] * (limit + 1)
            is_prime[0] = is_prime[1] = False
            
            for start in range(2, int(limit**0.5) + 1):
                if is_prime[start]:
                    for multiple in range(start*start, limit + 1, start):
                        is_prime[multiple] = False
            return is_prime
        
        is_prime = sieve_of_eratosthenes(n)
        prime_pairs = []
        
        for x in range(2, n // 2 + 1):
            y = n - x
            if is_prime[x] and is_prime[y]:
                prime_pairs.append([x, y])
        
        return prime_pairs