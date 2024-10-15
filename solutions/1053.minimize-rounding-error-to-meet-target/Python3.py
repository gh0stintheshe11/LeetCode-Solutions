from typing import List
import math

class Solution:
    def minimizeError(self, prices: List[str], target: int) -> str:
        floor_sum = 0
        ceilings = []
        
        for price in prices:
            float_price = float(price)
            floor_price = math.floor(float_price)
            ceiling_price = math.ceil(float_price)
            floor_sum += floor_price
            if floor_price != ceiling_price:
                ceilings.append(ceiling_price - float_price)
        
        if floor_sum > target or floor_sum + len(ceilings) < target:
            return "-1"
        
        num_ceilings_needed = target - floor_sum
        ceilings.sort()
        rounding_error = sum(ceilings[:num_ceilings_needed]) + sum(1 - c for c in ceilings[num_ceilings_needed:])
        
        return "{:.3f}".format(rounding_error)