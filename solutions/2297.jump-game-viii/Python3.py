from typing import List

class Solution:
    def minCost(self, nums: List[int], costs: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')] * n
        dp[0] = 0
        
        # Stack for increasing sequences
        inc_stack = []
        # Stack for decreasing sequences
        dec_stack = []
        
        for i in range(n):
            # Handle increasing condition
            while inc_stack and nums[inc_stack[-1]] <= nums[i]:
                j = inc_stack.pop()
                dp[i] = min(dp[i], dp[j] + costs[i])
            inc_stack.append(i)
            
            # Handle decreasing condition
            while dec_stack and nums[dec_stack[-1]] > nums[i]:
                j = dec_stack.pop()
                dp[i] = min(dp[i], dp[j] + costs[i])
            dec_stack.append(i)
        
        return dp[-1]