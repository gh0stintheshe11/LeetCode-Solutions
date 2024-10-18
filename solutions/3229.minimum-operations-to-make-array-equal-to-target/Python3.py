from typing import List

class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        inc = 0
        dec = 0
        res = 0

        for i in range(len(nums)):
            d = target[i] - nums[i]

            if d > 0:
                if inc < d:
                    res += d - inc
                inc = d
                dec = 0
            elif d < 0:
                if dec < -d:
                    res += -d - dec
                dec = -d
                inc = 0
            else:
                inc = 0
                dec = 0

        return res