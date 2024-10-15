from typing import List

class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        max_xor = 0
        for num in nums:
            max_xor |= num
        return max_xor