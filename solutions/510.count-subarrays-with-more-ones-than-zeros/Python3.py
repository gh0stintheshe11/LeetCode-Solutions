from typing import List
from collections import Counter

class Solution:
    def subarraysWithMoreZerosThanOnes(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        counts = Counter({0: 1})
        res = s = dp = 0
        for n in nums:
            if n == 1:
                s += 1
                dp += counts[s - 1]
            else:
                s -= 1
                dp -= counts[s]
            res = (res + dp) % MOD
            counts[s] += 1
        return res % MOD