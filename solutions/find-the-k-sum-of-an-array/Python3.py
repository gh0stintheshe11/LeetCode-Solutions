import heapq
from typing import List

class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        total_sum = sum(x for x in nums if x > 0)
        nums = sorted(abs(x) for x in nums)
        n = len(nums)
        heap = [(0, 0)]
        for _ in range(k - 1):
            s, i = heapq.heappop(heap)
            if i < n:
                heapq.heappush(heap, (s + nums[i], i + 1))
                if i > 0:
                    heapq.heappush(heap, (s + nums[i] - nums[i - 1], i + 1))
        return total_sum - heap[0][0]