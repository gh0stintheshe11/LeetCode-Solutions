from collections import Counter
from typing import List

class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        freq = list(Counter(nums).values())
        quantity.sort(reverse=True)
        
        def can_distribute(i: int) -> bool:
            if i == len(quantity):
                return True
            for j in range(len(freq)):
                if freq[j] >= quantity[i]:
                    freq[j] -= quantity[i]
                    if can_distribute(i + 1):
                        return True
                    freq[j] += quantity[i]
            return False
        
        return can_distribute(0)