from typing import List

class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        def canDivide(mid: int) -> bool:
            current_sum = 0
            pieces = 0
            for sweet in sweetness:
                current_sum += sweet
                if current_sum >= mid:
                    pieces += 1
                    current_sum = 0
            return pieces >= k + 1
        
        low, high = min(sweetness), sum(sweetness) // (k + 1)
        
        while low < high:
            mid = (low + high + 1) // 2
            if canDivide(mid):
                low = mid
            else:
                high = mid - 1
        
        return low