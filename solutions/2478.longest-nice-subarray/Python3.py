from typing import List

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        max_length = 0
        start = 0
        used_bits = 0
        
        for end in range(len(nums)):
            while (used_bits & nums[end]) != 0:
                used_bits ^= nums[start]
                start += 1
            used_bits |= nums[end]
            max_length = max(max_length, end - start + 1)
        
        return max_length