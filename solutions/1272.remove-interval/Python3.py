from typing import List

class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        result = []
        remove_start, remove_end = toBeRemoved
        
        for start, end in intervals:
            if end <= remove_start or start >= remove_end:
                result.append([start, end])
            else:
                if start < remove_start:
                    result.append([start, remove_start])
                if end > remove_end:
                    result.append([remove_end, end])
        
        return result