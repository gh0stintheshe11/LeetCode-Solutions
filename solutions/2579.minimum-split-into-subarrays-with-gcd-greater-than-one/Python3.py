from typing import List
from math import gcd

class Solution:
    def minimumSplits(self, nums: List[int]) -> int:
        n = len(nums)
        subarrays_count = 1
        current_gcd = nums[0]

        for i in range(1, n):
            current_gcd = gcd(current_gcd, nums[i])
            if current_gcd == 1:
                subarrays_count += 1
                current_gcd = nums[i]

        return subarrays_count