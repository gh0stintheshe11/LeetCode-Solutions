from typing import List
import heapq

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        # Convert odd numbers to even, and create a max-heap
        max_heap = []
        for num in nums:
            if num % 2 == 1:
                num *= 2
            max_heap.append(-num)  # Use negative to simulate max-heap
        
        heapq.heapify(max_heap)
        
        # Our minimum deviation initially is set between the max and min in the heap
        min_val = -max(max_heap)
        min_deviation = float('inf')
        
        while max_heap:
            current_max = -heapq.heappop(max_heap)
            min_deviation = min(min_deviation, current_max - min_val)
            if current_max % 2 == 1:
                break
            next_value = current_max // 2
            min_val = min(min_val, next_value)
            heapq.heappush(max_heap, -next_value)
        
        return min_deviation