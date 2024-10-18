from typing import List
from collections import defaultdict

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        def calculate_p(x: int) -> int:
            p = 1
            i = 2
            while i * i <= x:
                count = 0
                while x % i == 0:
                    x //= i
                    count += 1
                if count % 2 == 1:
                    p *= i
                i += 1
            if x > 1:
                p *= x
            return p
        
        sum_dict = defaultdict(int)
        
        for i, num in enumerate(nums, 1):
            p = calculate_p(i)
            sum_dict[p] += num
        
        return max(sum_dict.values())