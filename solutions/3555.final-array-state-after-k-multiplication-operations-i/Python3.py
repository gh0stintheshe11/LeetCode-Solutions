from typing import List
import heapq

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [(nums[i], i) for i in range(len(nums))]
        heapq.heapify(heap)
        
        for _ in range(k):
            val, idx = heapq.heappop(heap)
            nums[idx] = val * multiplier
            heapq.heappush(heap, (nums[idx], idx))
        
        return nums