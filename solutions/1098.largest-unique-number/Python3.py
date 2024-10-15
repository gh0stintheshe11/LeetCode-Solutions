from typing import List
from collections import Counter

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        unique_nums = [num for num, cnt in count.items() if cnt == 1]
        return max(unique_nums) if unique_nums else -1