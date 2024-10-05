from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = 0
        right = 0
        zeros_flipped = 0
        max_ones = 0
        
        while right < len(nums):
            if nums[right] == 0:
                zeros_flipped += 1
                
            while zeros_flipped > 1:
                if nums[left] == 0:
                    zeros_flipped -= 1
                left += 1
                
            max_ones = max(max_ones, right - left + 1)
            right += 1
            
        return max_ones