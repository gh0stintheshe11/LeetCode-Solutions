from typing import List
from itertools import permutations

class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        max_number = 0
        for perm in permutations(nums):
            # Concatenate the binary representations
            binary_str = ''.join(bin(num)[2:] for num in perm)
            # Convert the binary string back to an integer
            number = int(binary_str, 2)
            max_number = max(max_number, number)
        return max_number