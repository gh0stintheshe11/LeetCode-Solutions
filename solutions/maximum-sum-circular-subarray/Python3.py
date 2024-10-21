from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def kadane(arr):
            max_ending_here = max_so_far = arr[0]
            for x in arr[1:]:
                max_ending_here = max(x, max_ending_here + x)
                max_so_far = max(max_so_far, max_ending_here)
            return max_so_far

        max_kadane = kadane(nums)
        
        # Edge case handling for the situation where all elements are negative
        if max_kadane < 0:
            return max_kadane
        
        total_sum = sum(nums)
        max_wrap = total_sum + kadane([-x for x in nums])
        
        return max(max_kadane, max_wrap)