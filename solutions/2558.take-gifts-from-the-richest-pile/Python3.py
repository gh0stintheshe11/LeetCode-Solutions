import heapq
import math
from typing import List

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # Negate values to simulate a max-heap using Python's min-heap
        max_heap = [-g for g in gifts]
        heapq.heapify(max_heap)
        
        for _ in range(k):
            # Pop the largest element, revert the sign
            max_gift = -heapq.heappop(max_heap)
            # Calculate the remaining gifts after removing the floor of sqrt
            remaining_gifts = int(math.sqrt(max_gift))
            # Push the remaining gifts back into the heap
            heapq.heappush(max_heap, -remaining_gifts)
        
        # The resulting sum of the heap, revert signs to return to original positive
        return -sum(max_heap)