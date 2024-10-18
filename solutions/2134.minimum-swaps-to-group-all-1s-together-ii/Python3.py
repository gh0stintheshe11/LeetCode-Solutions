from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        total_ones = sum(nums)
        double_nums = nums + nums
        min_swaps = float('inf')
        current_zeros = 0
        left = 0

        for right in range(len(double_nums)):
            if double_nums[right] == 0:
                current_zeros += 1

            if right - left + 1 > total_ones:
                if double_nums[left] == 0:
                    current_zeros -= 1
                left += 1

            if right - left + 1 == total_ones:
                min_swaps = min(min_swaps, current_zeros)

        return min_swaps