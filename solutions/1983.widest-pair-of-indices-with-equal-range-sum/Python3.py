from typing import List

class Solution:
    def widestPairOfIndices(self, nums1: List[int], nums2: List[int]) -> int:
        prefix_sum1, prefix_sum2 = 0, 0
        max_width = 0
        diff_map = {0: -1}  # to account for prefix sums from the start
        
        for i in range(len(nums1)):
            prefix_sum1 += nums1[i]
            prefix_sum2 += nums2[i]
            diff = prefix_sum1 - prefix_sum2
            
            if diff in diff_map:
                max_width = max(max_width, i - diff_map[diff])
            else:
                diff_map[diff] = i
        
        return max_width