from math import factorial

class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        MOD = 10**9 + 7
        
        def is_prime(num):
            if num <= 1:
                return False
            if num <= 3:
                return True
            if num % 2 == 0 or num % 3 == 0:
                return False
            i = 5
            while i * i <= num:
                if num % i == 0 or num % (i + 2) == 0:
                    return False
                i += 6
            return True

        prime_count = sum(is_prime(i) for i in range(1, n + 1))
        non_prime_count = n - prime_count
        
        return (factorial(prime_count) * factorial(non_prime_count)) % MOD