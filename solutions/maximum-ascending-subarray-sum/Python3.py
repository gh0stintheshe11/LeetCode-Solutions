from typing import List

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maximum_sum = 0
        current_sum = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                current_sum += nums[i]
            else:
                maximum_sum = max(maximum_sum, current_sum)
                current_sum = nums[i]
        
        return max(maximum_sum, current_sum)