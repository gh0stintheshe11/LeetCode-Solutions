from typing import List
from bisect import bisect_left

class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums1)
        sorted_nums1 = sorted(nums1)
        initial_diff_sum = sum(abs(nums1[i] - nums2[i]) for i in range(n))
        max_improvement = 0
        
        for i in range(n):
            current_diff = abs(nums1[i] - nums2[i])
            pos = bisect_left(sorted_nums1, nums2[i])
            
            if pos < n:
                max_improvement = max(max_improvement, current_diff - abs(sorted_nums1[pos] - nums2[i]))
                
            if pos > 0:
                max_improvement = max(max_improvement, current_diff - abs(sorted_nums1[pos - 1] - nums2[i]))
        
        return (initial_diff_sum - max_improvement) % MOD