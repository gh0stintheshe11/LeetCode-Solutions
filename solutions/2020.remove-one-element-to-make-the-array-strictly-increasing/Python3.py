from typing import List

class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        def is_strictly_increasing(arr: List[int]) -> bool:
            return all(arr[i - 1] < arr[i] for i in range(1, len(arr)))
        
        for i in range(len(nums)):
            if is_strictly_increasing(nums[:i] + nums[i+1:]):
                return True
        
        return False