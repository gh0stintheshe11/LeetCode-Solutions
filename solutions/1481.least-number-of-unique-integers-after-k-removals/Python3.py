from typing import List
from collections import Counter

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = Counter(arr)
        freq_values = sorted(freq.values())
        
        unique_count = len(freq_values)
        
        for count in freq_values:
            if k >= count:
                k -= count
                unique_count -= 1
            else:
                break
        
        return unique_count