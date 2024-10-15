from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start=0):
            # If we've reached the end of the array, we have a complete permutation
            if start == len(nums):
                result.append(nums[:])
                return
            
            for i in range(start, len(nums)):
                # Swap the current element with the start element
                nums[start], nums[i] = nums[i], nums[start]
                # Recurse on the next part of the array
                backtrack(start + 1)
                # Backtrack (undo the swap)
                nums[start], nums[i] = nums[i], nums[start]
        
        result = []
        backtrack()
        return result