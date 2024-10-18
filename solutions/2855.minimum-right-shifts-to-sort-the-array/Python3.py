from typing import List

class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        n = len(nums)
        violation_index = -1

        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                if violation_index != -1:
                    return -1
                violation_index = i

        if violation_index == -1:
            return 0

        if nums[-1] > nums[0]:
            return -1

        return n - violation_index