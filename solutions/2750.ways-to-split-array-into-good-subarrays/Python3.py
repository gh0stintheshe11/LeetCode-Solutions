from typing import List

class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        positions = [i for i, v in enumerate(nums) if v == 1]
        if len(positions) < 2:
            return 1 if len(positions) == 1 else 0
        result = 1
        for i in range(1, len(positions)):
            result *= (positions[i] - positions[i-1])
            result %= MOD
        return result