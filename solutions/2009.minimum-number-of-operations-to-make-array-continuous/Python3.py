from typing import List
import bisect

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums = sorted(nums)
        unique_sorted_nums = sorted(set(nums))
        n = len(nums)
        min_ops = float('inf')
        
        for i in range(len(unique_sorted_nums)):
            target = unique_sorted_nums[i] + n - 1
            j = bisect.bisect_right(unique_sorted_nums, target)
            continuous_length = j - i
            ops_needed = n - continuous_length
            min_ops = min(min_ops, ops_needed)
        
        return min_ops