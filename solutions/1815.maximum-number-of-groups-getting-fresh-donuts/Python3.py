from collections import defaultdict
from typing import List
from functools import lru_cache

class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        rem_count = [0] * batchSize
        happy_groups = 0

        for group in groups:
            rem = group % batchSize
            if rem == 0:
                happy_groups += 1
            else:
                rem_count[rem] += 1

        # Self self-pairing for the case where batchSize is even
        if batchSize % 2 == 0 and rem_count[batchSize // 2] > 0:
            happy_groups += rem_count[batchSize // 2] // 2
            rem_count[batchSize // 2] %= 2

        for i in range(1, (batchSize + 1) // 2):
            j = batchSize - i
            if i != j:
                pairs = min(rem_count[i], rem_count[j])
                happy_groups += pairs
                rem_count[i] -= pairs
                rem_count[j] -= pairs

        rem_tuple = tuple(rem_count)

        @lru_cache(None)
        def dfs(rem_tuple, start_rem):
            rem_count = list(rem_tuple)
            if sum(rem_count) == 0:
                return 0

            max_happy = 0
            for i in range(batchSize):
                if rem_count[i] > 0:
                    new_rem_count = list(rem_count)
                    new_rem_count[i] -= 1
                    add_happy = 1 if (start_rem == 0) else 0
                    new_start_rem = (start_rem + i) % batchSize
                    max_happy = max(max_happy, add_happy + dfs(tuple(new_rem_count), new_start_rem))

            return max_happy

        return happy_groups + dfs(rem_tuple, 0)