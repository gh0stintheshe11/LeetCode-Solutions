from heapq import heappush, heappop
from typing import List

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = sorted(zip(nums2, nums1), reverse=True)
        min_heap = []
        current_sum = 0
        max_score = 0

        for value2, value1 in pairs:
            heappush(min_heap, value1)
            current_sum += value1
            if len(min_heap) > k:
                current_sum -= heappop(min_heap)
            if len(min_heap) == k:
                max_score = max(max_score, current_sum * value2)

        return max_score