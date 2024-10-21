from typing import List

class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        n = len(nums)
        dp = [-float('inf')] * n
        dp[0] = nums[0]
        
        max_even = dp[0] if nums[0] % 2 == 0 else -float('inf')
        max_odd = dp[0] if nums[0] % 2 != 0 else -float('inf')
        
        for i in range(1, n):
            if nums[i] % 2 == 0:
                dp[i] = max(dp[i], max_even + nums[i])
                if max_odd != -float('inf'):
                    dp[i] = max(dp[i], max_odd + nums[i] - x)
            else:
                dp[i] = max(dp[i], max_odd + nums[i])
                if max_even != -float('inf'):
                    dp[i] = max(dp[i], max_even + nums[i] - x)
            
            if nums[i] % 2 == 0:
                max_even = max(max_even, dp[i])
            else:
                max_odd = max(max_odd, dp[i])
        
        return max(dp)