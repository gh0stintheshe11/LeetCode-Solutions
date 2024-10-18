from typing import List

class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        left = 0
        right = n // 2
        max_pairs = 0
        
        # Try to pair each smaller element with a larger one
        while left < n // 2 and right < n:
            if 2 * nums[left] <= nums[right]:
                max_pairs += 1
                left += 1
            right += 1
        
        return max_pairs * 2