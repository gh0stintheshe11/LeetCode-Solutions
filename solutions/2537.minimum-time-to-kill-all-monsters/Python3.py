from typing import List
from functools import lru_cache

class Solution:
    def minimumTime(self, power: List[int]) -> int:
        power.sort()
        
        @lru_cache(None)
        def dp(mask: int, mana_gain: int) -> int:
            if mask == 0:
                return 0
            
            min_days = float('inf')
            
            for i in range(len(power)):
                if mask & (1 << i):
                    new_mask = mask & ~(1 << i)
                    additional_days = (power[i] - 1) // mana_gain + 1
                    min_days = min(min_days, additional_days + dp(new_mask, mana_gain + 1))
            return min_days

        initial_mask = (1 << len(power)) - 1
        return dp(initial_mask, 1)