from typing import List

class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single_digit_sum = sum(num for num in nums if num < 10)
        double_digit_sum = sum(num for num in nums if num >= 10)
        return single_digit_sum > double_digit_sum or double_digit_sum > single_digit_sum