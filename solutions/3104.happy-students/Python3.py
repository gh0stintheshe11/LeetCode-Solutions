from typing import List

class Solution:
    def countWays(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        count = 0
        
        for i in range(n):
            if (i == 0 or nums[i-1] < i) and i < nums[i]:
                count += 1
        
        if nums[-1] < n:
            count += 1
        
        return count