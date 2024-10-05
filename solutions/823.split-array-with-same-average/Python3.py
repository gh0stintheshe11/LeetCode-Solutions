from typing import List

class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        from functools import lru_cache
        import itertools
        
        n = len(nums)
        if n == 1:
            return False
        
        S = sum(nums)
        nums.sort()
        
        @lru_cache(None)
        def dp(k, n, target):
            if n == 0:
                return target == 0
            if n < 0 or k < 0:
                return False
            return dp(k-1, n-1, target-nums[k]) or dp(k-1, n, target)
        
        for length in range(1, n//2 + 1):
            if S * length % n == 0 and dp(n-1, length, S * length // n):
                return True
        
        return False