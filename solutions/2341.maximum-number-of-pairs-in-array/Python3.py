from typing import List
from collections import Counter

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        pairs = 0
        leftovers = 0
        
        for freq in count.values():
            pairs += freq // 2
            leftovers += freq % 2
        
        return [pairs, leftovers]