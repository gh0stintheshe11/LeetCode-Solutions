class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        MOD = 10**9 + 7
        if primeFactors <= 3:
            return primeFactors
        
        def power(x, y, p):
            res = 1
            x = x % p
            while y > 0:
                if y & 1:
                    res = (res * x) % p
                y = y >> 1
                x = (x * x) % p
            return res

        if primeFactors % 3 == 0:
            return power(3, primeFactors // 3, MOD)
        elif primeFactors % 3 == 1:
            return (power(3, primeFactors // 3 - 1, MOD) * 4) % MOD
        else:
            return (power(3, primeFactors // 3, MOD) * 2) % MOD