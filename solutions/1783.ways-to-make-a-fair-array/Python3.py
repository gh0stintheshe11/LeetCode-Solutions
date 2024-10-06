from typing import List

class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        total_even, total_odd = 0, 0
        for i, num in enumerate(nums):
            if i % 2 == 0:
                total_even += num
            else:
                total_odd += num

        result = 0
        prefix_even, prefix_odd = 0, 0

        for i, num in enumerate(nums):
            if i % 2 == 0:
                total_even -= num
            else:
                total_odd -= num

            if prefix_even + total_odd == prefix_odd + total_even:
                result += 1

            if i % 2 == 0:
                prefix_even += num
            else:
                prefix_odd += num

        return result