from typing import List
import heapq

class Solution:
    def makePrefSumNonNegative(self, nums: List[int]) -> int:
        operations = 0
        prefix_sum = 0
        min_heap = []

        for num in nums:
            prefix_sum += num
            if prefix_sum < 0:
                heapq.heappush(min_heap, num)
                prefix_sum -= heapq.heappop(min_heap)
                operations += 1
            else:
                heapq.heappush(min_heap, num)
        
        return operations