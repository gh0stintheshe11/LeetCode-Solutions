from collections import Counter
from typing import List

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        count = Counter(arr)
        
        # Sorting the keys by absolute values to handle negative numbers properly
        for x in sorted(arr, key=abs):
            if count[x] == 0:
                continue
            if count[2 * x] == 0:
                return False
            count[x] -= 1
            count[2 * x] -= 1
            
        return True