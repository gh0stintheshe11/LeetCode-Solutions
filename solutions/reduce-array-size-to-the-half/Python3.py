from typing import List
from collections import Counter

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = Counter(arr)
        freq_values = sorted(freq.values(), reverse=True)
        total_removed = 0
        set_size = 0
        half_length = len(arr) // 2
        
        for count in freq_values:
            total_removed += count
            set_size += 1
            if total_removed >= half_length:
                return set_size
        
        return set_size