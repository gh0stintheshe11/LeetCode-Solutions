from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ops = 0
        i, j = 0, len(nums) - 1
        
        while i < j:
            if nums[i] == nums[j]:
                i += 1
                j -= 1
            elif nums[i] < nums[j]:
                nums[i + 1] += nums[i]
                i += 1
                ops += 1
            else:  # nums[i] > nums[j]
                nums[j - 1] += nums[j]
                j -= 1
                ops += 1
        
        return ops