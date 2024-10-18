from typing import List

class Solution:
    def findMaximalUncoveredRanges(self, n: int, ranges: List[List[int]]) -> List[List[int]]:
        ranges.sort()
        result = []
        current_end = -1
        
        for start, end in ranges:
            if start > current_end + 1:
                result.append([current_end + 1, start - 1])
            current_end = max(current_end, end)
        
        if current_end < n - 1:
            result.append([current_end + 1, n - 1])
        
        return result