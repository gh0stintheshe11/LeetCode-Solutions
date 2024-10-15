from typing import List
import heapq
import math

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        # Convert nums to a max-heap (Python has min-heap, so insert negative numbers)
        max_heap = [-x for x in nums]
        heapq.heapify(max_heap)

        score = 0
        for _ in range(k):
            # Extract the maximum element (in negated form)
            max_value = -heapq.heappop(max_heap)
            # Add it to the score
            score += max_value
            # Compute the new value as ceil(max_value / 3) and push it back in negated form
            new_value = math.ceil(max_value / 3)
            heapq.heappush(max_heap, -new_value)

        return score