from math import gcd

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def lcm(x, y):
            return x * y // gcd(x, y)

        def count_ugly_numbers(x):
            # Count the number of integers <= x that are divisible by a, b, or c
            return (x // a + x // b + x // c
                    - x // ab - x // ac - x // bc
                    + x // abc)
        
        ab = lcm(a, b)
        ac = lcm(a, c)
        bc = lcm(b, c)
        abc = lcm(ab, c)
        
        left, right = 1, 2 * 10**9
        while left < right:
            mid = (left + right) // 2
            if count_ugly_numbers(mid) < n:
                left = mid + 1
            else:
                right = mid
        
        return left