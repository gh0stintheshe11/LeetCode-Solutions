class Solution:
    def minDays(self, n: int) -> int:
        from functools import lru_cache
        
        @lru_cache(None)
        def min_days(n):
            if n <= 1:
                return n
            return 1 + min(n % 2 + min_days(n // 2), n % 3 + min_days(n // 3))
        
        return min_days(n)