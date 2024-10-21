from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        if not nums:
            return 1  # As there's problem constraints ensuring nums is not empty, this is just for safety.

        # Find the longest sequential prefix
        longest_prefix_sum = nums[0]
        current_sum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                current_sum += nums[i]
            else:
                break
        
        longest_prefix_sum = current_sum

        # Finding the smallest missing integer greater than or equal to longest_prefix_sum
        smallest_missing_integer = longest_prefix_sum
        
        while smallest_missing_integer in nums:
            smallest_missing_integer += 1
            
        return smallest_missing_integer