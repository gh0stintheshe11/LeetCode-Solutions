from sortedcontainers import SortedList
from typing import List

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        pos_in_nums2 = [0] * n
        # Create position array for nums2
        for idx, val in enumerate(nums2):
            pos_in_nums2[val] = idx

        # Transform nums1 to its positions in nums2
        transformed = [pos_in_nums2[val] for val in nums1]

        # Count of elements less than current position
        left = [0] * n
        sorted_set = SortedList()
        for i in range(n):
            left[i] = sorted_set.bisect_left(transformed[i])
            sorted_set.add(transformed[i])

        # Count of elements greater than current position
        right = [0] * n
        sorted_set = SortedList()
        for i in range(n - 1, -1, -1):
            right[i] = len(sorted_set) - sorted_set.bisect_right(transformed[i])
            sorted_set.add(transformed[i])

        count_good_triplets = 0
        for i in range(n):
            count_good_triplets += left[i] * right[i]

        return count_good_triplets