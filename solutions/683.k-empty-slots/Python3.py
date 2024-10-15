from typing import List

class Solution:
    def kEmptySlots(self, bulbs: List[int], k: int) -> int:
        days = [0] * len(bulbs)
        for day, bulb in enumerate(bulbs):
            days[bulb - 1] = day + 1
        
        left, right = 0, k + 1
        res = float('inf')
        
        for i in range(1, len(days)):
            if right >= len(days):
                break
            
            if i == right:
                res = min(res, max(days[left], days[right]))
                left, right = i, i + k + 1
            elif days[i] < days[left] or days[i] < days[right]:
                left, right = i, i + k + 1
                
        return res if res != float('inf') else -1