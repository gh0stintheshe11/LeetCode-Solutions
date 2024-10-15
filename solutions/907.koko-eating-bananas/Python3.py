from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canFinish(piles, speed, h):
            hours = 0
            for pile in piles:
                hours += (pile + speed - 1) // speed  # Equivalent to math.ceil(pile / speed)
            return hours <= h
        
        left, right = 1, max(piles)
        while left <= right:
            mid = (left + right) // 2
            if canFinish(piles, mid, h):
                right = mid - 1
            else:
                left = mid + 1
        
        return left