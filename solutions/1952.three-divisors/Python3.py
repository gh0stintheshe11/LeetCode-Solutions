class Solution:
    def isThree(self, n: int) -> bool:
        import math
        if n < 4:
            return False
        sqrt_n = int(math.sqrt(n))
        if sqrt_n * sqrt_n != n:
            return False
        for i in range(2, sqrt_n):
            if n % i == 0:
                return False
        return True