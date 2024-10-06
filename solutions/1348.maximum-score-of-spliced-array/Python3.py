from typing import List

class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        def kadane_diff(arr1, arr2):
            max_diff = current_diff = 0
            for x, y in zip(arr1, arr2):
                current_diff = max(0, current_diff + y - x)
                max_diff = max(max_diff, current_diff)
            return max_diff

        sum_nums1 = sum(nums1)
        sum_nums2 = sum(nums2)

        max_diff1 = kadane_diff(nums1, nums2)
        max_diff2 = kadane_diff(nums2, nums1)

        return max(sum_nums1 + max_diff1, sum_nums2 + max_diff2)