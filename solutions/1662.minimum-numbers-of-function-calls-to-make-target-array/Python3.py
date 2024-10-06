from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        total_add = 0
        max_double = 0
        
        for num in nums:
            add = 0
            double = 0
            while num > 0:
                if num % 2 == 1:
                    num -= 1
                    add += 1
                else:
                    num //= 2
                    double += 1
            total_add += add
            max_double = max(max_double, double)
        
        return total_add + max_double