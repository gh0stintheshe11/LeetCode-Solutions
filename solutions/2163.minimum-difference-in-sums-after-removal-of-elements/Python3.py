from heapq import heappush, heappop
from typing import List

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3
        
        # Calculate prefix min sums for the first part using a max-heap
        min_first_part = [float('inf')] * (3 * n)
        max_heap = []
        current_sum = 0
        
        for i in range(3 * n):
            heappush(max_heap, -nums[i])
            current_sum += nums[i]
            if len(max_heap) > n:
                current_sum += heappop(max_heap)
            if len(max_heap) == n:
                min_first_part[i] = current_sum
        
        # Calculate suffix max sums for the second part using a min-heap
        max_second_part = [float('-inf')] * (3 * n)
        min_heap = []
        current_sum = 0
        
        for i in range(3 * n - 1, -1, -1):
            heappush(min_heap, nums[i])
            current_sum += nums[i]
            if len(min_heap) > n:
                current_sum -= heappop(min_heap)
            if len(min_heap) == n:
                max_second_part[i] = current_sum

        # Find the minimum difference
        min_difference = float('inf')
        for i in range(n - 1, 2 * n):
            min_difference = min(min_difference, min_first_part[i] - max_second_part[i + 1])

        return min_difference