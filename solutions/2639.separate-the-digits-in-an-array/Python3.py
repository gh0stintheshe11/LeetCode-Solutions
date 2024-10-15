from typing import List

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = []
        for num in nums:
            answer.extend(int(digit) for digit in str(num))
        return answer