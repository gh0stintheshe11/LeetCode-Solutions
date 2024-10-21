from collections import defaultdict
from bisect import bisect_left, bisect_right
import random

class MajorityChecker:
    def __init__(self, arr: List[int]):
        self.arr = arr
        self.index_map = defaultdict(list)
        for i, num in enumerate(arr):
            self.index_map[num].append(i)

    def query(self, left: int, right: int, threshold: int) -> int:
        for _ in range(20):
            idx = random.randint(left, right)
            candidate = self.arr[idx]
            occurrences = self.index_map[candidate]
            left_pos = bisect_left(occurrences, left)
            right_pos = bisect_right(occurrences, right)
            
            if right_pos - left_pos >= threshold:
                return candidate

        return -1