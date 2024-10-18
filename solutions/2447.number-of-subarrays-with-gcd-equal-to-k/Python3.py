from math import gcd
from typing import List

class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        
        for i in range(n):
            current_gcd = 0
            for j in range(i, n):
                current_gcd = gcd(current_gcd, nums[j])
                if current_gcd == k:
                    count += 1
                elif current_gcd < k:
                    break
                
        return count