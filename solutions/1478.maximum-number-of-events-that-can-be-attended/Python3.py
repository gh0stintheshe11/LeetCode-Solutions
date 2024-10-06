from typing import List
import heapq

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        min_heap = []
        event_index = 0
        max_events_attended = 0
        n = len(events)

        for day in range(1, 100001):
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)
            
            while event_index < n and events[event_index][0] == day:
                heapq.heappush(min_heap, events[event_index][1])
                event_index += 1
            
            if min_heap:
                heapq.heappop(min_heap)
                max_events_attended += 1
            
            if event_index >= n and not min_heap:
                break
        
        return max_events_attended