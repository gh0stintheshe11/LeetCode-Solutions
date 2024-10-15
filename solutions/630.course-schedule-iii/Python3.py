import heapq
from typing import List

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        max_heap = []
        time = 0
        
        for duration, last_day in courses:
            if time + duration <= last_day:
                heapq.heappush(max_heap, -duration)
                time += duration
            elif max_heap and -max_heap[0] > duration:
                time += duration + heapq.heappop(max_heap)
                heapq.heappush(max_heap, -duration)
                
        return len(max_heap)