from typing import List
from collections import defaultdict

class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        event_points = defaultdict(int)

        for start, end, color in segments:
            event_points[start] += color
            event_points[end] -= color
        
        sorted_points = sorted(event_points.keys())
        results = []
        current_sum = 0
        current_start = sorted_points[0]
        
        for i in range(1, len(sorted_points)):
            current_end = sorted_points[i]
            current_sum += event_points[sorted_points[i-1]]
            
            if current_sum != 0:
                results.append([current_start, current_end, current_sum])
            
            current_start = current_end
        
        return results