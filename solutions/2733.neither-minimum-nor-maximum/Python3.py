from typing import List

class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return -1
        
        min_val = float('inf')
        max_val = float('-inf')
        
        for num in nums:
            if num < min_val:
                min_val = num
            if num > max_val:
                max_val = num
        
        for num in nums:
            if num != min_val and num != max_val:
                return num
        
        return -1