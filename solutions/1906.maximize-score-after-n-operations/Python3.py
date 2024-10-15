from math import gcd
from functools import lru_cache
from typing import List

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums) // 2
        gcd_values = {}
        
        # Precompute GCD for every pair
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                gcd_values[(i, j)] = gcd(nums[i], nums[j])
        
        @lru_cache(None)
        def dp(mask):
            # Count how many numbers have been used
            used_count = bin(mask).count('1')
            if used_count == len(nums):
                return 0
            
            max_score = 0
            operation = used_count // 2 + 1
            
            for i in range(len(nums)):
                if mask & (1 << i):
                    continue
                for j in range(i + 1, len(nums)):
                    if mask & (1 << j):
                        continue
                    new_mask = mask | (1 << i) | (1 << j)
                    score = operation * gcd_values[(i, j)] + dp(new_mask)
                    max_score = max(max_score, score)
            
            return max_score
        
        return dp(0)