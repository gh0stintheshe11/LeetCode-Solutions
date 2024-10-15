from typing import List
from collections import Counter

class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        return all(count <= 2 for count in freq.values())