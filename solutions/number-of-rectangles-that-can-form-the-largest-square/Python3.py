from typing import List

class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        maxLen = 0
        maxCount = 0

        for l, w in rectangles:
            sideLen = min(l, w)
            if sideLen > maxLen:
                maxLen = sideLen
                maxCount = 1
            elif sideLen == maxLen:
                maxCount += 1

        return maxCount