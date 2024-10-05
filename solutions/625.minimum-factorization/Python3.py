class Solution:
    def smallestFactorization(self, num: int) -> int:
        if num < 10:
            return num
        
        factors = []
        
        for i in range(9, 1, -1):
            while num % i == 0:
                factors.append(i)
                num //= i
        
        if num != 1:
            return 0
        
        result = 0
        for factor in reversed(factors):
            result = result * 10 + factor
            if result > 2**31 - 1:
                return 0
        
        return result