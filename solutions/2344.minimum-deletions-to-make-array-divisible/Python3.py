from typing import List
from math import gcd
from functools import reduce

class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        # Calculate the gcd of all the elements in numsDivide
        target_gcd = reduce(gcd, numsDivide)
        
        # Sort the nums array to find the minimum deletions
        nums.sort()
        
        # Try to find the smallest element in sorted nums that divides the target_gcd
        for i, num in enumerate(nums):
            if target_gcd % num == 0:
                return i
        return -1