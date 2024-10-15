from typing import List

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_value = nums[0]
        max_difference = -1
        
        for i in range(1, len(nums)):
            if nums[i] > min_value:
                max_difference = max(max_difference, nums[i] - min_value)
            else:
                min_value = nums[i]
        
        return max_difference