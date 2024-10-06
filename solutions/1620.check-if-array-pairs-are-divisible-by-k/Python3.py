from typing import List
from collections import defaultdict

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainder_count = defaultdict(int)
        
        for num in arr:
            remainder = num % k
            remainder_count[remainder] += 1
        
        for r in range(k):
            if r == 0:
                if remainder_count[r] % 2 != 0:
                    return False
            elif r * 2 == k:
                if remainder_count[r] % 2 != 0:
                    return False
            else:
                if remainder_count[r] != remainder_count[k - r]:
                    return False
                
        return True