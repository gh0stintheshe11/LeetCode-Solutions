from typing import List
from collections import Counter
import heapq

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        # Count the frequency of each barcode
        frequency = Counter(barcodes)
        # Create a max heap based on the frequency of each barcode
        max_heap = [(-count, barcode) for barcode, count in frequency.items()]
        heapq.heapify(max_heap)
        
        # Initialize the previous element to a dummy value
        prev_count, prev_barcode = 0, 0
        result = []

        while max_heap:
            count, barcode = heapq.heappop(max_heap)
            result.append(barcode)
            
            # Since we used one instance of this barcode, we decrease its count
            if prev_count < 0:
                heapq.heappush(max_heap, (prev_count, prev_barcode))
            
            prev_count, prev_barcode = count + 1, barcode

        return result