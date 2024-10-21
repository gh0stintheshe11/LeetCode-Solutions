import bisect
from typing import List

class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        bigger_diff = []
        smaller_diff = []

        for i in range(n):
            if nums1[i] > nums2[i]:
                bigger_diff.append(nums1[i] - nums2[i])
            else:
                smaller_diff.append(nums2[i] - nums1[i])
        bigger_diff.sort()
        k = len(bigger_diff)

        ans = k * (k - 1) // 2

        for i in range(len(smaller_diff)):
            if smaller_diff[i] == 0:
                ans += k
            else:
                ans += k - bisect.bisect_right(bigger_diff, smaller_diff[i])
        return ans