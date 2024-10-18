import heapq
from typing import List

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # Priority queue to maximize the gain of adding an extra student
        heap = []
        
        # Calculate initial priority (gain) for each class and add to the heap
        for passed, total in classes:
            current_ratio = passed / total
            new_ratio = (passed + 1) / (total + 1)
            potential_gain = new_ratio - current_ratio
            # Push negative gain because heapq in Python is a min-heap
            heapq.heappush(heap, (-potential_gain, passed, total))
        
        # Distribute the extra students optimally
        for _ in range(extraStudents):
            # Pop the class with maximum gain
            neg_gain, passed, total = heapq.heappop(heap)
            # Include the extra student in the class
            passed += 1
            total += 1
            # Recalculate the new potential gain
            current_ratio = passed / total
            new_ratio = (passed + 1) / (total + 1)
            potential_gain = new_ratio - current_ratio
            # Push the updated class back to the heap
            heapq.heappush(heap, (-potential_gain, passed, total))
        
        # Calculate the final average pass ratio
        total_ratio = sum(passed / total for _, passed, total in heap)
        return total_ratio / len(classes)