from typing import List

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def canDistribute(max_per_store: int) -> bool:
            stores_needed = 0
            for qty in quantities:
                stores_needed += (qty + max_per_store - 1) // max_per_store
                if stores_needed > n:
                    return False
            return True
        
        left, right = 1, max(quantities)
        while left < right:
            mid = (left + right) // 2
            if canDistribute(mid):
                right = mid
            else:
                left = mid + 1
        return left