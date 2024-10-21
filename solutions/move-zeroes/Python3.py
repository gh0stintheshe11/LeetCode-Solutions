from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Pointer for the position of the next non-zero element
        last_non_zero_found_at = 0
        
        # Move all the non-zero elements to the beginning of the array
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_non_zero_found_at] = nums[i]
                last_non_zero_found_at += 1
        
        # Fill the remaining positions with zeros
        for i in range(last_non_zero_found_at, len(nums)):
            nums[i] = 0