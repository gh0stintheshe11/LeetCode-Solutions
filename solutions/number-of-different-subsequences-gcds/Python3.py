from typing import List
import math

class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        max_val = max(nums)
        presence = [False] * (max_val + 1)
        
        for num in nums:
            presence[num] = True
        
        count_gcds = 0
        
        for x in range(1, max_val + 1):
            current_gcd = 0
            for multiple in range(x, max_val + 1, x):
                if presence[multiple]:
                    current_gcd = math.gcd(current_gcd, multiple)
                if current_gcd == x:
                    break
            if current_gcd == x:
                count_gcds += 1
        
        return count_gcds