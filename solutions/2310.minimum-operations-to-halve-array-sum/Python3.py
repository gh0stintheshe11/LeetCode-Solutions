import heapq
from typing import List

class Solution:
    def halveArray(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        target = total_sum / 2
        operations = 0
        
        # In Python, heapq is a min-heap. We can use negative values to simulate a max-heap.
        max_heap = [-x for x in nums]
        heapq.heapify(max_heap)
        
        reduced_sum = 0
        
        while reduced_sum < target:
            largest = -heapq.heappop(max_heap)
            reduced_largest = largest / 2
            reduced_sum += reduced_largest
            heapq.heappush(max_heap, -reduced_largest)
            operations += 1
            
        return operations