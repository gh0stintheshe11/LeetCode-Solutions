from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShipInDays(capacity: int) -> bool:
            total = 0
            days_needed = 1
            for weight in weights:
                if total + weight > capacity:
                    days_needed += 1
                    total = 0
                total += weight
            return days_needed <= days
        
        left, right = max(weights), sum(weights)
        
        while left < right:
            mid = (left + right) // 2
            if canShipInDays(mid):
                right = mid
            else:
                left = mid + 1
        
        return left