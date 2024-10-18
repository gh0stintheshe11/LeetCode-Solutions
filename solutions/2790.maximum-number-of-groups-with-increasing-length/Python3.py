from typing import List

class Solution:
    def maxIncreasingGroups(self, usageLimits: List[int]) -> int:
        usageLimits.sort()
        n = len(usageLimits)
        total_available = 0
        k = 0
        for i in range(n):
            total_available += usageLimits[i]
            if total_available >= (k + 1) * (k + 2) // 2:
                k += 1
        return k