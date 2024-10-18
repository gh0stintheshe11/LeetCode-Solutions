from typing import List

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        events = []
        for start, end in intervals:
            events.append((start, 1))
            events.append((end + 1, -1))
        
        events.sort()
        
        current_groups = 0
        max_groups = 0
        
        for _, change in events:
            current_groups += change
            if current_groups > max_groups:
                max_groups = current_groups
        
        return max_groups