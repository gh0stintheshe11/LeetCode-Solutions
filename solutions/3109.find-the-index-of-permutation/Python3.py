from sortedcontainers import SortedList
from functools import lru_cache
from typing import List

class Solution:
    def getPermutationIndex(self, perm: List[int]) -> int:

        MOD = 10 ** 9 + 7

        count = [0] * len(perm) # values still available and also less than cur-value
        stack = SortedList()
        for i in range(len(perm)):
            index = stack.bisect_left(perm[i])
            count[i] = perm[i] - 1 - index
            stack.add(perm[i])

        @lru_cache(None)
        def frac(num):
            if num <= 1:
                return 1
            return num * frac(num - 1) % MOD

        ans = 0
        for i in range(len(perm)):
            ans += count[i] * frac(len(perm) - i - 1)
            ans = ans % MOD

        return ans