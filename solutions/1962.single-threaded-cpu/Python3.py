from heapq import heappop, heappush
from typing import List

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # Annotate each task with its index and create tuples
        indexed_tasks = [(enqueueTime, processingTime, i) for i, (enqueueTime, processingTime) in enumerate(tasks)]
        
        # Sort tasks by their enqueue time
        indexed_tasks.sort(key=lambda x: x[0])
        
        # Min-heap for available tasks
        min_heap = []
        i, time = 0, 0
        order = []
        
        # Process all tasks
        while i < len(indexed_tasks) or min_heap:
            # Enqueue all tasks that can start at current time
            while i < len(indexed_tasks) and indexed_tasks[i][0] <= time:
                heappush(min_heap, (indexed_tasks[i][1], indexed_tasks[i][2]))  # (processingTime, index)
                i += 1
            
            if min_heap:
                # Pick the task with the smallest processing time (and smallest index)
                proc_time, index = heappop(min_heap)
                time += proc_time
                order.append(index)
            else:
                # No available tasks, move time forward to the next task's enqueue time
                time = indexed_tasks[i][0]
        
        return order