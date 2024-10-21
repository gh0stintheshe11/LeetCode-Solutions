from collections import Counter
from typing import List

class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.nums2_count = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        old_value = self.nums2[index]
        new_value = old_value + val
        # Update the count of nums2
        self.nums2_count[old_value] -= 1
        if self.nums2_count[old_value] == 0:
            del self.nums2_count[old_value]
        self.nums2_count[new_value] += 1
        # Update nums2
        self.nums2[index] = new_value

    def count(self, tot: int) -> int:
        cnt = 0
        for num1 in self.nums1:
            cnt += self.nums2_count.get(tot - num1, 0)
        return cnt