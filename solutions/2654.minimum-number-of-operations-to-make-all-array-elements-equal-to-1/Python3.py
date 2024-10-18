from typing import List
from math import gcd

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if 1 in nums:
            return n - nums.count(1)
        
        min_operations = float('inf')

        for i in range(n):
            current_gcd = nums[i]
            for j in range(i + 1, n):
                current_gcd = gcd(current_gcd, nums[j])
                if current_gcd == 1:
                    min_operations = min(min_operations, j - i + n - 1)
                    break

        return min_operations if min_operations != float('inf') else -1