class Solution:
    def smallestValue(self, n: int) -> int:
        def prime_factors_sum(x):
            total = 0
            factor = 2
            while factor * factor <= x:
                while x % factor == 0:
                    total += factor
                    x //= factor
                factor += 1
            if x > 1:
                total += x
            return total
        
        while True:
            sum_of_factors = prime_factors_sum(n)
            if sum_of_factors == n:
                break
            n = sum_of_factors
        
        return n