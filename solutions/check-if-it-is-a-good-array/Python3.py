from typing import List
import math

class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        gcd = nums[0]
        for num in nums:
            gcd = math.gcd(gcd, num)
            if gcd == 1:
                return True
        return gcd == 1