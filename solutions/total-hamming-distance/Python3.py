from typing import List

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)
        # there are at most 32 bits in a number (for 0 <= nums[i] <= 10^9)
        for i in range(32):
            count_ones = 0
            for num in nums:
                if num & (1 << i):
                    count_ones += 1
            count_zeros = n - count_ones
            total += count_ones * count_zeros
        return total