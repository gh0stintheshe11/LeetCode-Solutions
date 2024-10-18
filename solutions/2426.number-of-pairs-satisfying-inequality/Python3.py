from typing import List
from sortedcontainers import SortedList

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        n = len(nums1)
        sl = SortedList()
        count = 0
        
        for i in range(n):
            target = nums1[i] - nums2[i]
            count += sl.bisect_right(target + diff)
            sl.add(target)
        
        return count