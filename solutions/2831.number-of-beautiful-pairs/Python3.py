from typing import List
from math import gcd

class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        def first_digit(n):
            while n >= 10:
                n //= 10
            return n
        
        count = 0
        for i in range(len(nums) - 1):
            first_digit_i = first_digit(nums[i])
            for j in range(i + 1, len(nums)):
                last_digit_j = nums[j] % 10
                if gcd(first_digit_i, last_digit_j) == 1:
                    count += 1
        
        return count