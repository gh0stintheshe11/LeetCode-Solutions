class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        import math
        gcd = math.gcd(a, b)
        count = 0
        for i in range(1, gcd + 1):
            if gcd % i == 0:
                count += 1
        return count