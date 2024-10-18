from typing import List

class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        
        # count of increasing subarrays ending at the current position
        count = 0
        total = 0
        
        for i in range(n):
            if i == 0 or nums[i] > nums[i - 1]:
                count += 1
            else:
                count = 1
            total += count
        
        return total