from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_linear(nums: List[int]) -> int:
            prev, curr = 0, 0
            for num in nums:
                prev, curr = curr, max(curr, prev + num)
            return curr
        
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))