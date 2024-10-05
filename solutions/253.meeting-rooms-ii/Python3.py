import heapq
from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        # Sort the intervals by the start time
        intervals.sort(key=lambda x: x[0])
        
        # Initialize a heap to keep track of the end time of meetings
        heap = []
        
        # Add the first meeting's end time to the heap
        heapq.heappush(heap, intervals[0][1])
        
        for interval in intervals[1:]:
            # If the room due to free up the earliest is free, assign that room to this meeting
            if heap[0] <= interval[0]:
                heapq.heappop(heap)
            
            # If a new room is to be assigned, add the ending time to the heap
            heapq.heappush(heap, interval[1])
        
        # The size of the heap is the number of rooms needed
        return len(heap)