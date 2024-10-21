from typing import List

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        count = 0
        end = 0
        for _, curr_end in intervals:
            if curr_end > end:
                count += 1
                end = curr_end
        return count