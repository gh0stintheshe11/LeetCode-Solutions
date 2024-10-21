from typing import List

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        result = []
        current_number = 0
        for num in nums:
            current_number = (current_number * 2 + num) % 5
            result.append(current_number == 0)
        return result