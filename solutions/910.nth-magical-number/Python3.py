class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        import math
        
        MOD = 10**9 + 7
        
        def lcm(x, y):
            return x * y // math.gcd(x, y)
        
        lo, hi = 1, n * min(a, b)
        lcm_ab = lcm(a, b)
        
        while lo < hi:
            mid = (lo + hi) // 2
            if mid // a + mid // b - mid // lcm_ab < n:
                lo = mid + 1
            else:
                hi = mid
        
        return lo % MOD