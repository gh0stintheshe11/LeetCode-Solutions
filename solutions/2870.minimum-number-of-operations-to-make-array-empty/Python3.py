from typing import List
from collections import Counter

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq = Counter(nums)
        
        operations = 0
        for count in freq.values():
            if count == 1:
                return -1
            operations += count // 3 + (1 if count % 3 != 0 else 0)
        
        return operations