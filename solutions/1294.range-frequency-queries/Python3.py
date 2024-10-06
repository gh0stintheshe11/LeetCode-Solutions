from collections import defaultdict
from bisect import bisect_left, bisect_right
from typing import List

class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.index_map = defaultdict(list)
        for i, num in enumerate(arr):
            self.index_map[num].append(i)
        
    def query(self, left: int, right: int, value: int) -> int:
        if value not in self.index_map:
            return 0
        indices = self.index_map[value]
        left_idx = bisect_left(indices, left)
        right_idx = bisect_right(indices, right) - 1
        return max(0, right_idx - left_idx + 1)