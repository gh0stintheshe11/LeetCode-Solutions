from typing import List

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        result = []
        
        while i < len(firstList) and j < len(secondList):
            start1, end1 = firstList[i]
            start2, end2 = secondList[j]
            
            # Check if these two intervals intersect
            if start1 <= end2 and start2 <= end1:
                start = max(start1, start2)
                end = min(end1, end2)
                result.append([start, end])
            
            # Move the pointer of the interval that finished first
            if end1 < end2:
                i += 1
            else:
                j += 1
        
        return result