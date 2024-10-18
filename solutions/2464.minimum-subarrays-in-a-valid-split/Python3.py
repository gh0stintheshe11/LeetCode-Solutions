from typing import List
from math import gcd

class Solution:
    def validSubarraySplit(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # base case: no elements, no subarrays
        
        for i in range(1, n + 1):
            for j in range(i):
                if gcd(nums[j], nums[i - 1]) > 1:
                    dp[i] = min(dp[i], dp[j] + 1)
        
        return dp[n] if dp[n] != float('inf') else -1