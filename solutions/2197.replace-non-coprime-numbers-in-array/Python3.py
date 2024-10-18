from math import gcd
from typing import List

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        for num in nums:
            while stack:
                top = stack[-1]
                if gcd(top, num) > 1:
                    num = top * num // gcd(top, num)
                    stack.pop()
                else:
                    break
            stack.append(num)
        return stack