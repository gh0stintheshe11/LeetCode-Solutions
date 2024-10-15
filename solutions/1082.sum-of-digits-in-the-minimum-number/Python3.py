from typing import List

class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        min_num = min(nums)
        digit_sum = sum(int(digit) for digit in str(min_num))
        return 1 if digit_sum % 2 == 0 else 0