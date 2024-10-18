from typing import List
import heapq

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        # Convert all piles to negative numbers to use min heap as max heap
        max_heap = [-pile for pile in piles]
        heapq.heapify(max_heap)
        
        for _ in range(k):
            # Pop the largest element
            largest_pile = -heapq.heappop(max_heap)
            # Remove floor(largest_pile / 2)
            reduced_pile = largest_pile - largest_pile // 2
            # Push the reduced pile back into the heap
            heapq.heappush(max_heap, -reduced_pile)
        
        # Return the sum of elements left in the heap
        return -sum(max_heap)