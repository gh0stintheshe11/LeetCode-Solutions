from typing import List
from collections import Counter

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        result = set()
        digit_count = Counter(digits)
        
        for i in range(100, 1000):
            if i % 2 == 0:  # The number must be even
                str_i = str(i)
                needed_count = Counter(map(int, str_i))
                
                if all(digit_count[d] >= needed_count[d] for d in needed_count):
                    result.add(i)
        
        return sorted(result)