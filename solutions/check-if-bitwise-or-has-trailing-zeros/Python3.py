from typing import List

class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        even_count = sum(1 for num in nums if num % 2 == 0)
        return even_count >= 2