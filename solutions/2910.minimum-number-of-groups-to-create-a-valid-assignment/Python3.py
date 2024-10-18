from typing import List
from collections import Counter
from math import ceil

class Solution:
    def minGroupsForValidAssignment(self, balls: List[int]) -> int:
        cnt = Counter(balls)
        for max_group_size in range(min(cnt.values()) + 1, 0, -1):
            total_groups = 0
            for num in cnt.keys():
                groups = ceil(cnt[num] / max_group_size)
                if groups * max_group_size >= cnt[num] and groups * (max_group_size - 1) <= cnt[num]:
                    total_groups += groups
                else:
                    total_groups += 1e9
            if total_groups < 1e9:
                return total_groups