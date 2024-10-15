from typing import List

class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        max_index = 0
        for i in range(1, len(nums) - k + 1):
            if nums[i] > nums[max_index]:
                max_index = i
        return nums[max_index:max_index + k]