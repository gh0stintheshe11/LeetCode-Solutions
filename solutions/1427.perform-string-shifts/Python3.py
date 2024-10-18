from typing import List

class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        net_shift = 0
        for direction, amount in shift:
            if direction == 0:
                net_shift -= amount
            else:
                net_shift += amount
        
        net_shift %= len(s)
        
        return s[-net_shift:] + s[:-net_shift] if net_shift != 0 else s