from typing import List
from collections import Counter

class Solution:
    def canDivideIntoSubsequences(self, nums: List[int], k: int) -> bool:
        freq = Counter(nums)
        max_freq = max(freq.values())
        return len(nums) >= max_freq * k