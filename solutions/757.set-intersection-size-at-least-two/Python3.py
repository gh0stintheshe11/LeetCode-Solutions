from typing import List

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))
        to_add = [-1, -1]
        result = 0

        for start, end in intervals:
            if to_add[0] < start <= to_add[1]:
                to_add = [to_add[1], end]
                result += 1
            elif start > to_add[1]:
                to_add = [end-1, end]
                result += 2
        return result