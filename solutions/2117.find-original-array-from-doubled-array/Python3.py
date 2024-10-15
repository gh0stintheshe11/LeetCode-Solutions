from collections import Counter
from typing import List

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []
        
        changed.sort()
        counter = Counter(changed)
        original = []
        
        for num in changed:
            if counter[num] == 0:
                continue
            if counter[num * 2] == 0:
                return []
            original.append(num)
            counter[num] -= 1
            counter[num * 2] -= 1
            
        return original